import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        # app = os.path.abspath('../../apps/TestApp/build/release-iphonesimulator/TestApp.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': 'com.81.player',
                'platformName': 'iOS',
                'platformVersion': '8.4.1',
                'deviceName': 'iPhone 5',
                'udid': 'dfdb2e87d35495b664c570dd13e112b84c12dda6'
            })

    def tearDown(self):
        self.driver.quit()