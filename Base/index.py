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

class Button(object):
	id             = 'bf.cloud.bfclouddemowithui:id/'
	vod            = id + 'vod' # 点播按钮ID
	live           = id + 'live'
	play_url       = id + 'play_url'  # 播放地址输入框ID
	start          = id + 'start'
	full_screen    = id + 'full_screen'
	change_video   = id + 'change_video'
	definitionID   = id + 'definitionID'
	getdefinitions = id + 'getdefinitions'
	change_decode  = id + 'change_decode'
	live_delay     = id + 'change_live_delay_mode'
	stop           = id + 'stop'
	resume         = id + 'resume'
	definition     = id + 'definition'
	live_confirm   = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]'

class url(object):
	H265      = 'servicetype=2&uid=5263465&fid=12345678901234567890123456789012345ABCDE'
	Canvas    = 'servicetype=1&uid=34803807&fid=B2A803B8BECC47E0EB77DC487A5AB1B3'  # Canvas播放地址  4K_VR
	qstp_vod  = 'qstp://qkvp/pGp/bmxleqg/qey:XDXZ.s?jp=GGJ&jd=XADBAQJG0E0AZAQ11JWGDFZCTMAXFGTDAWWWJD0E&vd=DQGFTQJJDMWZGGWZEAJ1XBWAAATXEDTMTBETQMXW&lh=X1JQBZM&fz=DQQZ0E&pi=DT&pr=WM0XX&pps=A&ppk=A&pyp=X1JQBWE&blzd=JXA1&vk=A&pah=MCJMGEBWEJQFAGADD0QW0Z0GJFT1TAWZ&ped=pov'
	qstp_live = 'qstp://qkvp/five/bmxleqg/qey:XDZD.s?jp=GAAAQ&jd=QTTEZQ01ZZDFMZAQ0ZJQMF1BMGQEWF1ZFFMTZ1GT&vd=QTTEZQ01ZZDFMZAQ0ZJQMF1BMGQEWF1ZFFMTZ1GT&lh=WFFFFFFFFFFFFFFF&pr=JEXAAA&pk=DCMTQFJTDZTAMA1MBMTWCZFJEJJ1BGCQ&ds=A&vpz=qkvpq/five/bmxleqg/qey&vpp=XDZD&pah=D1DGJQBCMJFQWX0MCQJ0CMGJ00TZMG01&ped=bfv'

class command(object):
	# tcpdump -i en1 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420' and dst host 103.15.200.120
	cmdnclog  = ['tcpdump', '-i', 'en1', 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420', 'and', 'dst', 'host','103.15.200.120', '-l']

class defini(object):
	vod360p   = '0'
	vod480p   = '1'
	vod720p   = '2'
	vod1080p  = '3'
	live360p  = '10'
	live480p  = "20"
	live720p  = '30'
	live1080p = '40'