#coding=utf-8
import os,subprocess,unittest,time
from Base.index import AppSet

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

vod = 'bf.cloud.bfclouddemowithui:id/vod' # 点播按钮ID
live = 'bf.cloud.bfclouddemowithui:id/live'
play_url = 'bf.cloud.bfclouddemowithui:id/play_url' # 播放地址输入框ID
start = 'bf.cloud.bfclouddemowithui:id/start'
full_screen = 'bf.cloud.bfclouddemowithui:id/full_screen'
change_video = 'bf.cloud.bfclouddemowithui:id/change_video'
definitionID = 'bf.cloud.bfclouddemowithui:id/definitionID'
getdefinitions = 'bf.cloud.bfclouddemowithui:id/getdefinitions'
change_decode = 'bf.cloud.bfclouddemowithui:id/change_decode_mode'
live_delay = 'bf.cloud.bfclouddemowithui:id/change_live_delay_mode'
stop = 'bf.cloud.bfclouddemowithui:id/stop'
resume = 'bf.cloud.bfclouddemowithui:id/resume'
definition = 'bf.cloud.bfclouddemowithui:id/definition'
live_confirm = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]'

Canvas = 'servicetype=1&uid=34803807&fid=B2A803B8BECC47E0EB77DC487A5AB1B3' # Canvas播放地址
qstp_vod = 'qstp://qkvp/pGp/bmxleqg/qey:XDXZ.s?jp=GGJ&jd=XADBAQJG0E0AZAQ11JWGDFZCTMAXFGTDAWWWJD0E&vd=DQGFTQJJDMWZGGWZEAJ1XBWAAATXEDTMTBETQMXW&lh=X1JQBZM&fz=DQQZ0E&pi=DT&pr=WM0XX&pps=A&ppk=A&pyp=X1JQBWE&blzd=JXA1&vk=A&pah=MCJMGEBWEJQFAGADD0QW0Z0GJFT1TAWZ&ped=pov'
qstp_live = 'qstp://qkvp/five/bmxleqg/qey:XDZD.s?jp=GAAAQ&jd=QTTEZQ01ZZDFMZAQ0ZJQMF1BMGQEWF1ZFFMTZ1GT&vd=QTTEZQ01ZZDFMZAQ0ZJQMF1BMGQEWF1ZFFMTZ1GT&lh=WFFFFFFFFFFFFFFF&pr=JEXAAA&pk=DCMTQFJTDZTAMA1MBMTWCZFJEJJ1BGCQ&ds=A&vpz=qkvpq/five/bmxleqg/qey&vpp=XDZD&pah=D1DGJQBCMJFQWX0MCQJ0CMGJ00TZMG01&ped=bfv'

looptime = 5

live360p = '10'
live480p = "20"
live720p = '30'
live1080p = '40'


class AppTestCase(AppSet):

	def test_001(self):
		'''获取手机的分辨率'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print u'手机的分辨率为:',width,'*',height
		subprocess.call(["ls -l"],shell=True)

	def test_002(self):
		'''点播seek'''
		self.driver.find_element_by_id(vod).click()

		self.driver.find_element_by_id(play_url).send_keys(Canvas)

		self.driver.find_element_by_id(start).click()

		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		time.sleep(3)

		self.driver.swipe(width/3,height/4,width*2/3,height/4,1000)
		time.sleep(10)

	def test_003(self):
		'''点播切片'''
		time.sleep(1)
		self.driver.find_element_by_id(vod).click()

		for i in range(looptime):
			self.driver.find_element_by_id(change_video).click()
			time.sleep(3)

	def	test_004(self):
		'''直播清晰度'''
		self.driver.find_element_by_id(live).click()

		self.driver.find_element_by_id(start).click()
		time.sleep(1)

		self.driver.find_element_by_id(definitionID).send_keys(live360p)

		self.driver.find_element_by_xpath(live_confirm).click()
		time.sleep(2)

if __name__=='__main__':
	unittest.main(verbosity=2)

	# suite=unittest.TestSuite()
	# suite.addTest(AppTestCase('test_002'))
	# unittest.TextTestRunner(verbosity=2).run(suite)
