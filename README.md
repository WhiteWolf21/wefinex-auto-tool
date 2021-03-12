# Wefinex Auto Tool
Auto Trading On Wefinex - Huỳnh Ngọc Thiện

### Execution Steps

First open terminal and get into directory wefinex-auto-tool

1. Config parameters:

- Download Chrome browser and extract suitable chromedriver for your OS (check zip files in the project directory):

- Change account name:

~~~bash
ActionChains(driver).move_to_element(email).click(email).send_keys('<put-your-account-name-here>').perform()
~~~

- Change account password:

~~~bash
ActionChains(driver).move_to_element(password).click(password).send_keys('<put-your-account-password-here>').perform()
~~~

- Change trading money:

~~~bash
ActionChains(driver).move_to_element(bet).click(bet).send_keys('<put-your-trading-number-in-integer-number>').perform()
~~~

- Change session ID:

~~~bash
if result[-1]["session"] == <put-your-session-id-in-integer-number>:
~~~

- Change buy/sell status:

~~~bash
action = driver.find_element_by_xpath("//button[@class='" + <buy-or-sell> + "']")
~~~

2. Run the tool:

~~~bash
python3 wefinex.py
~~~

- When the browser popup, the tool will login and recaptcha v2 will appear. At that moment, please solve it and after finishing, remember to input y in the terminal to continue the process.

3. Exit the tool:

- While running the tool, if you want to edit different parameters or there are some errors, please use CTRL+C in the terminal and re-run the execution steps.

# Thank You Everyone Very Much For Spending Time Looking Through This Project !!!
