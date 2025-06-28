import unittest
import time
import os
import wordlists
from mutations import (
    mutation_engine, prefixes, suffixes, base_words,
    leetspeak_mutations, prefix_mutations,
    suffix_mutations, capitalization_mutations,
    base_words_mutation
)
with open("mutation_performance_log.txt", "w") as f:
    f.write("=== Mutation Performance Log ===\n")


class TestMutationEngineCorrectness(unittest.TestCase):

    def setUp(self):
        self.test_pw = "test"
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.base_words = base_words

    def test_includes_original_password(self):
        mutations = mutation_engine(self.test_pw, self.suffixes, self.prefixes, self.base_words, max_mutations=100)
        self.assertIn("test", mutations)

    def test_generates_at_least_one_mutation(self):
        mutations = mutation_engine(self.test_pw, self.suffixes, self.prefixes, self.base_words, max_mutations=100)
        self.assertTrue(any(m != "test" for m in mutations))

    def test_handles_empty_string(self):
        mutations = mutation_engine("", self.suffixes, self.prefixes, self.base_words, max_mutations=100)
        self.assertIn("", mutations)
        self.assertTrue(len(mutations) > 1)  # Should still generate something

class TestMutationPerformance(unittest.TestCase):

    def setUp(self):
        wordlists_dict = wordlists.load_all_wordlists()
        self.test_password = "password123"
        self.prefixes = list(set(wordlists_dict['prefix']))
        self.suffixes = list(set(wordlists_dict['suffix']))
        self.base_words = list(set(wordlists_dict['baseword']))
        self.limits = [100, 500, 1000, 2500, 5000, 10000]
        self.logfile = "mutation_performance_log.txt"

    def time_test(self, func, *args, **kwargs):
        max_mutations = kwargs.get("max_mutations", None)
        start = time.time()
        results = func(*args, **kwargs)
        elapsed = time.time() - start
        count = len(results) if hasattr(results, '__len__') else 'unknown'

        log_line = (
            f"{func.__name__} with max_mutations={max_mutations} "
            f"took {elapsed:.4f}s, produced {count} results"
        )

        print(f"\n=== {func.__name__} ===")
        print(log_line)

        # Optional: log to file
        with open(self.logfile, "a") as f:
            f.write(log_line + "\n")
        return results


    def test_leetspeak_performance(self):
        for limit in self.limits:
            self.time_test(leetspeak_mutations, self.test_password, max_mutations=limit)

    def test_prefix_performance(self):
        self.time_test(prefix_mutations, self.test_password, self.prefixes)

    def test_suffix_performance(self):
        self.time_test(suffix_mutations, self.test_password, self.suffixes)

    def test_capitalization_performance(self):
        self.time_test(capitalization_mutations, self.test_password)

    def test_base_words_performance(self):
        self.time_test(base_words_mutation, self.test_password, self.base_words)

    def test_mutation_engine_performance(self):
        for limit in self.limits:
            self.time_test(
                mutation_engine,
                self.test_password,
                self.suffixes,
                self.prefixes,
                self.base_words,
                depth=1,
                max_mutations=limit
            )

if __name__ == '__main__':
    unittest.main(verbosity=2)