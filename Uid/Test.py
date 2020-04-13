from unittest import TestCase
from Uid import Uid, uid


class TestUidClass(TestCase):
    def test_has_id(self):
        self.assertTrue(hasattr(Uid(), "_Uid__id"))

    def test_eq(self):
        a = Uid()
        b = Uid()
        # Force `b` to have the same id as `a`
        b._Uid__id = a.id
        self.assertEqual(a, b)

    def test_hash(self):
        self.assertTrue(hash(Uid()))


class TestUidFunction(TestCase):
    def test_run(self):
        self.assertTrue(uid())
