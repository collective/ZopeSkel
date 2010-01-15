# -*- coding: utf-8 -*-

import unittest

from zopeskel.zopeskel_script import checkdots

class test_zopeskel(unittest.TestCase):
    """Tests for ZopeSkel script.
    """

    def test_checkdots_none(self):
        """Verify that checkdots works with templates without ndots hint."""

        class FauxTemplate: pass
        t = FauxTemplate()

        checkdots(t, "anything is legal; not a package")

    def test_checkdots_two(self):
        """Verify that checkdots validates templates with ndots hint."""

        class FauxTemplate: pass
        t = FauxTemplate()

        t.ndots = 2

        self.assertRaises(ValueError, checkdots, t, "nodots")
        self.assertRaises(ValueError, checkdots, t, "one.dot")
        self.assertRaises(ValueError, checkdots, t, "three.dots.in.this")
        self.assertRaises(ValueError, checkdots, t, "two.dots.but not legal")

        checkdots(t, "two.dots.legal")


def test_suite():
    suite = unittest.TestSuite([
        unittest.makeSuite(test_zopeskel)])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
