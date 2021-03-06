#! /usr/bin/env python
# ______________________________________________________________________
'''test_all

Grand unified unit test script for Numba.
'''
# ______________________________________________________________________

import unittest
import __builtin__
__builtin__.__noskip__ = True

from test_all import *

# ______________________________________________________________________

if __name__ == "__main__":
    import sys, logging
    if '-d' in sys.argv:
        logging.getLogger().setLevel(logging.DEBUG)
        sys.argv.remove('-d')
    unittest.main()

# ______________________________________________________________________
# End of test_all_noskip.py
