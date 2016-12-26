#coding=utf-8
import os
import unittest
from appium	import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppTestCase(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'x3'
		desired_caps['appPackage'] = 'bf.cloud.bfclouddemowithui'
		desired_caps['appActivity'] = 'bf.cloud.demo.MainActivity'
		desired_caps['unicodeKeyboard'] = False
		desired_caps['resetKeyboard'] = False
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
		self.driver.implicitly_wait(10)

	def test_001(self):
		'''获取手机的分辨率'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		print u'手机的分辨率为:',width,'*',height

	def test_002(self):
		'''点播seek'''
		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/vod').click()

		Canvas='servicetype=1&uid=34803807&fid=B2A803B8BECC47E0EB77DC487A5AB1B3'
		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/play_url').send_keys(Canvas)

		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/start').click()
		# self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/full_screen').click()
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		sleep(3)
		self.driver.swipe(width/3,height/4,width*2/3,height/4,1000)
		sleep(10)

	def test_003(self):
		'''点播切片'''
		sleep(1)
		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/vod').click()

		num = 5
		for i in range(num):
			self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/change_video').click()
			sleep(3)

	def	test_004(self):
		'''直播清晰度'''
		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/live').click()

		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/start').click()
		sleep(1)
		self.driver.find_element_by_id('bf.cloud.bfclouddemowithui:id/definitionID').send_keys('10')

		self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
		sleep(1)


	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestSuite()
	suite.addTest(AppTestCase('test_004'))
	unittest.TextTestRunner(verbosity=2).run(suite)

	# unittest.main(verbosity=2)