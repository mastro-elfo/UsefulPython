from unittest import TestCase

from chunks import chunks

class Test(TestCase):
    def testChunks(self):
        self.assertEqual(
            list(chunks("abcdef", 1)),
            ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(list(chunks("abcdef", 2)), ["ab", "cd", "ef"])
        self.assertEqual(list(chunks("abcdef", 3)), ["abc", "def"])
        self.assertEqual(list(chunks("abcdef", 6)), ["abcdef"])
