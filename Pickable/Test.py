import unittest
from os import remove
from os.path import isfile
from .Pickable import Pickable


class TestPickable(unittest.TestCase):
    def setUp(self):
        # Before each test
        self.pickable = Pickable()

    def tearDown(self):
        # After each test
        pass

    def test_isinstance(self):
        self.assertTrue(isinstance(self.pickable, Pickable))

    def test_dump_load(self):
        self.pickable.dump("test.pickle")
        pickled = Pickable.load("test.pickle")
        self.assertTrue(isfile("test.pickle"))
        self.assertTrue(isinstance(pickled, Pickable))
        remove("test.pickle")

    def test_dumps_loads(self):
        pickled = Pickable.loads(self.pickable.dumps())
        self.assertTrue(isinstance(pickled, Pickable))


if __name__ == "__main__":
    unittest.main()
