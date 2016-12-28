#coding=utf-8
import os,unittest
from appium	import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppSet(unittest.TestCase):
	def setUp(self):
		caps = {}
		caps['platformName'] = 'Android'
		caps['platformVersion'] = '6.0'
		caps['deviceName'] = 'x3'
		caps['appPackage'] = 'bf.cloud.bfclouddemowithui'
		caps['appActivity'] = 'bf.cloud.demo.MainActivity'
		caps['unicodeKeyboard'] = False
		caps['resetKeyboard'] = False
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
		self.driver.implicitly_wait(10)

	def tearDown(self):
		self.driver.quit()
