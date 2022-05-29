from unittest import TestLoader, TestSuite, TextTestRunner
from pages.login_page import Login_Page
from pages.inventory_page import Inventory_Page
from pages.checkout_page import Checkout_Page

import testtools as testtools

if __name__ == '__main__':
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Login_Page),
        test_loader.loadTestsFromTestCase(Inventory_Page),
        test_loader.loadTestsFromTestCase(Checkout_Page),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
