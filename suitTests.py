from unittest import TestLoader, TestSuite, TextTestRunner
from pages.login_page import Login_Page

if __name__ == '__main__':
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Login_Page),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
