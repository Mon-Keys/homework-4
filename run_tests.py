# -*- coding: utf-8 -*-

import sys
import unittest

from tests.feed_test import feed_page_test

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(feed_page_test),
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
