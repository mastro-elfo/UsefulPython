from unittest import TestCase

from .Chunks import chunks

# chunks returns a generator, so the output must be cast
class Test(TestCase):
    def testChunks(self):
        self.assertEqual(list(chunks("abcdef", 1)), ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(list(chunks("abcdef", 2)), ["ab", "cd", "ef"])
        self.assertEqual(list(chunks("abcdef", 3)), ["abc", "def"])
        self.assertEqual(list(chunks("abcdef", 6)), ["abcdef"])

    def testList(self):
        self.assertEqual(list(chunks(["a", "b", "c", "d", "e", "f"], 1)), [["a"], ["b"], ["c"], ["d"], ["e"], ["f"]])
        self.assertEqual(list(chunks(["a", "b", "c", "d", "e", "f"], 2)), [["a","b"], ["c","d"], ["e","f"]])
        self.assertEqual(list(chunks(["a", "b", "c", "d", "e", "f"], 3)), [["a","b","c"], ["d","e","f"]])
        self.assertEqual(list(chunks(["a", "b", "c", "d", "e", "f"], 6)), [["a", "b", "c", "d", "e", "f"]])

if __name__ == '__main__':
    unittest.main()
