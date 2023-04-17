import traceback

from selenium.webdriver.common.by import By
from config.prod_config import qt_index_url, account, password
# from config.dev_config import qt_index_url, account, password
from time import sleep
import json
from browser import Browser
from qqmail import sendEmail
from config.qq_email_config import (
    from_addr,from_name,from_password,
    to_addr,to_name,smtp_server
)
from datetime import datetime
from utils.is_workday import isWorkdays
import random

email_client=sendEmail(
    from_addr,from_name,from_password,to_addr,to_name,smtp_server
)

try:
    date_ = datetime.now().date()
    if isWorkdays(date_):
        num = random.randint(1, 600)
        sleep(num)
        WebBrowser = Browser()
        WebBrowser.get_url_page(qt_index_url)
        browser = WebBrowser.browser
        sleep(10)

        # 签到
        # 输入账号
        try:
            acount_element = browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[4]/div[1]/div[2]"
            )
        except:
            browser.refresh()
            sleep(10)
        finally:
            browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[4]/div[1]/div[2]"
            ).click()
            sleep(1)
            browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[4]/div[1]/div[2]/input"
            ).send_keys(account)
            sleep(3)

            # 输入密码
            browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]"
            ).click()
            sleep(1)
            browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/input"
            ).send_keys(password)
            sleep(3)

            # 点击登录
            browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[6]/button"
            ).click()
            sleep(20)

        try:
            alert = browser.switch_to.alert
        except:
            browser.refresh()
            sleep(30)
            alert = browser.switch_to.alert
        finally:
            alert_dict = json.loads(alert.text)
            code = alert_dict.get("code")
            status = alert_dict.get("status")
            alert.accept()
            browser.close()
        if code == 200 or status:
            subject="签退成功"
            msg=f"签退成功,时间：{datetime.now()},msg:{alert_dict}"
        else:
            subject="签退失败"
            msg=f"签退失败,时间：{datetime.now()},msg:{alert_dict}"
    else:
        subject = "今天不是工作日，无需签到"
        msg = f"今天不是工作日,无需签到,时间：{datetime.now()}"
except:
    message=str(traceback.format_exc())
    subject = "错误"
    msg = f"程序错误,时间：{datetime.now()},msg:{message}"
finally:
    email_client.log_in()
    email_client.send_msg(subject, msg)
    email_client.close()
