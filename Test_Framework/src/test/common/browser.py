import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH

#driver配置，可自己添加
CHROME_DRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IE_DRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJS_DRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firfox':'wires', 'chrome': CHROME_DRIVER_PATH, 'ie':IE_DRIVER_PATH, 'phantomjs': PHANTOMJS_DRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

#配置浏览器
class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持s%!' % ','.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    #保存截图png到report目录下
    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screen_shot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screen_shot_path):
            os.makedirs(screen_shot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screen_shot = self.driver.save_screenshot(screen_shot_path + '\\%s_%s.png' % (name, tm))
        return screen_shot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

