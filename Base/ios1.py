"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        # http://appium.io/slate/cn/master/?ruby#appium

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'iOS',
                'platformVersion': '10.2',
                'deviceName': 'iPhone 6',
                'automationName': 'XCUITest',
                'bundleId': 'com.harry.HHH',
                'udid': '623d2e79504c1983aef1253583667066f4bf7a8b',
            })

#    def tearDown(self):
##        self.driver.quit()

    def test_scroll(self):
        self.driver.find_element_by_accessibility_id('button').click()

        sleep(1)
        try:
            sleep(1)
        except:
            pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
