# -*- coding: utf-8 -*-

from .context import skeleton
# Import other stuff here

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        """Pre-test activities."""
        pass
    
    def test_X(self):
        """ Add tests here. """
        pass

if __name__ == '__main__':
    unittest.main()