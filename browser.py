from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Browser():
    def __init__(self):
        # Chrome设置
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("–no-sandbox")
        # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("blink-settings=imagesEnabled=false")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def get_url_page(self, url):
        return self.browser.get(url)
