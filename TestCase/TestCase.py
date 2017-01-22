#coding=utf-8
import time
import subprocess
from Base.index import *
from appium.webdriver.connectiontype import ConnectionType


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppTestCase(AppSet):

	def test_001(self):
		'''获取手机的分辨率'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		print u'手机的分辨率为:',width,'*',height

		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		delay_time = time.strftime('%H-%M-%S',time.localtime(time.time()))

		self.driver.get_screenshot_as_file(delay_time)

		self.driver.set_network_connection(ConnectionType.DATA_ONLY)
		print self.driver.network_connection
		'''Sets the network connection type. Android only.
		    Possible values:
		        Value (Alias)      | Data | Wifi | Airplane Mode
		        -------------------------------------------------
		        0 (None)           | 0    | 0    | 0
		        1 (Airplane Mode)  | 0    | 0    | 1
		        2 (Wifi only)      | 0    | 1    | 0
		        4 (Data only)      | 1    | 0    | 0
		        6 (All network on) | 1    | 1    | 0
		    '''

		subprocess.call(["ls -l"],shell=True)

	def test_002(self):
		'''点播seek'''
		self.driver.find_element_by_id(Button.vod).click()

		self.driver.find_element_by_id(Button.play_url).send_keys(url.Canvas)

		self.driver.find_element_by_id(Button.start).click()

		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		time.sleep(3)

		self.driver.swipe(width/3,height/4,width*2/3,height/4,1000)
		time.sleep(10)

	def test_003(self):
		'''点播切片'''
		time.sleep(1)
		self.driver.find_element_by_id(Button.vod).click()
		self.driver.find_element_by_id(Button.start).click()

		p = subprocess.Popen(command.cmdnclog, stdout=subprocess.PIPE)

		for row in iter(p.stdout.readline, b''):
			self.driver.find_element_by_id(Button.change_video).click()
			time.sleep(3)
			print row.rstrip()  # process here

	def	test_004(self):
		'''直播清晰度'''
		self.driver.find_element_by_id(Button.live).click()

		self.driver.find_element_by_id(Button.start).click()
		time.sleep(1)

		self.driver.find_element_by_id(Button.definitionID).send_keys(defini.live360p)

		self.driver.find_element_by_xpath(Button.live_confirm).click()
		time.sleep(2)

if __name__=='__main__':
	# unittest.main(verbosity=2)

	suite=unittest.TestSuite()
	suite.addTest(AppTestCase('test_002'))
	unittest.TextTestRunner(verbosity=2).run(suite)
