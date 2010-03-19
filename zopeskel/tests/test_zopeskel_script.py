# -*- coding: utf-8 -*-

import unittest
import sys

from zopeskel.zopeskel_script import checkdots, process_args, run
from zopeskel.tests.test_zopeskeldocs import read_sh

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
        
    def test_process_args(self):
        """Ensure that process_args correctly processes command-line arguments"""
        oldargv = sys.argv
        
        sys.argv = ['zopskel']
        self.assertRaises(SyntaxError, process_args)
        
        sys.argv.append('archetype')
        processed = process_args()
        self.failUnlessEqual(processed[0], 'archetype')
        self.failIf(processed[1])
        self.failIf(processed[2])
        
        sys.argv.append('my.project')
        processed = process_args()
        self.failUnlessEqual(processed[0], 'archetype')
        self.failUnlessEqual(processed[1], 'my.project')
        self.failIf(processed[2])
        
        sys.argv.append('--bob=kate')
        processed = process_args()
        self.failUnlessEqual(processed[0], 'archetype')
        self.failUnlessEqual(processed[1], 'my.project')
        self.failUnlessEqual(processed[2]['--bob'], 'kate')

        # process_args will allow us to skip the project name argument
        sys.argv.pop(2)
        processed = process_args()
        self.failUnlessEqual(processed[0], 'archetype')
        self.failIf(processed[1])
        self.failUnlessEqual(processed[2]['--bob'], 'kate')
        
        # providing arguments in '-name val' form is _not_ allowed
        sys.argv = ['zopeskel', 'archetype', 'my.project', '-bob', 'kate']
        self.assertRaises(SyntaxError, process_args)
        
        # the --svn-repository argument is _not_ allowed in any form
        sys.argv = sys.argv[:3] + ['--svn-repository=svn://svn.junk.org/svn/blah']
        self.assertRaises(SyntaxError, process_args)
        
        sys.argv[3] = 'svn-repository=svn://svn.junk.org/svn/blah'
        self.assertRaises(SyntaxError, process_args)
        
        # providing args in a '-name val' format is not supported
        sys.argv = sys.argv[:3] + ['bob', 'kate']
        self.assertRaises(SyntaxError, process_args)
        
        sys.argv = oldargv

    def test_script_errors(self):
        """Verify that the run method catches errors correctly"""
        
        # non-existent templates are not caught until in 'run'
        output = read_sh('zopeskel no-template my.package')
        self.failUnless('ERROR: No such template' in output)
        

def test_suite():
    suite = unittest.TestSuite([
        unittest.makeSuite(test_zopeskel)])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
