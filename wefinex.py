from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import json
import pprint

def process_browser_logs_for_network_events(logs):
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if (
            # "Network.response" in log["method"]
            # or "Network.request" in log["method"] or
            "Network.webSocket" in log["method"]
        ):
            yield log

try:
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    driver = webdriver.Chrome('./chromedriver', desired_capabilities=capabilities,)
    driver.get("https://wefinex.net/")

    time.sleep(1)

    sign_in_button = driver.find_element_by_xpath("//span[@class='font-18 text-capitalize']")

    sign_in_button.click()

    time.sleep(1)

    inputs = driver.find_elements_by_xpath("//input")

    for each in inputs:
        if 'email' in each.get_attribute('outerHTML'):
            email = each

    ActionChains(driver).move_to_element(email).click(email).send_keys('khanhlinh20123@gmail.com').perform()

    time.sleep(1)

    password = driver.find_element_by_xpath("//input[@name='password']")

    ActionChains(driver).move_to_element(password).click(password).send_keys('!kL01214264564').perform()

    time.sleep(1)

    sign_in_submit = driver.find_element_by_xpath("//button[@class='button btn-large wbtn btn-radius w-100 siginButton']")

    sign_in_submit.click()

    recaptcha = "n"

    while recaptcha != "y":
        recaptcha = input("Finish Recaptcha (y/n): ")

    driver.get("https://wefinex.net/")

    time.sleep(5)

    bet = driver.find_element_by_xpath("//input[@id='InputNumber']")

    ActionChains(driver).move_to_element(bet).click(bet).send_keys('5').perform()

    while True:
        logs = driver.get_log("performance")
        events = process_browser_logs_for_network_events(logs)
        with open("log_entries.txt", "a+") as out:
            for event in events:

                pprint.pprint(event, stream=out)

                if event["method"] == "Network.webSocketFrameReceived" and event["params"]["response"].get("payloadData", '') != '': 
                    pay_load_data = event["params"]["response"]["payloadData"]

                    if "[" in pay_load_data:

                        pay_load_data = pay_load_data[pay_load_data.index("["):]

                        print(pay_load_data)

                        result = json.loads(pay_load_data)

                        if result[0] == "BO_PRICE":
                            if result[-1]["isBetSession"] == True:
                                if result[-1]["session"] == 988395:

                                    buy = "btn button btnSuccess w-100"
                                    sell = "btn button btnDown w-100"

                                    action = driver.find_element_by_xpath("//button[@class='" + buy + "']")

                                    ActionChains(driver).move_to_element(action).click(action).perform()


except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    driver.close()