import unittest

from zopeskel.tests.test_zopeskeldocs import test_suite as doc_test_suite

def test_suite():
    """ it appears that the order here makes a difference, ensure that doc_test_suite
        is always added last
    """
    suite = unittest.TestSuite([
        doc_test_suite(),
    ])
    return suite
    
if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')