# 載入套件
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

#禁用自動化框
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

#在物件中添加禁用瀏覽器通知的功能
chrome_options.add_argument("--disable-notifications")

# 開啟瀏覽器視窗(Chrome)
# 執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome(options=chrome_options)

# 更改網址以前往不同網頁
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm") # 更改網址以前往不同網頁

time.sleep(3)

#輸入姓
first_name = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[1]/td[2]/input')
first_name.send_keys("呂")

#輸入名
last_name = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[2]/td[2]/input')
last_name.send_keys("沛綸")

#勾選性別
sex = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[3]/td[2]/input[1]')
sex.click()

#Years of Experience
YOE = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[4]/td[2]/span[1]/input')
YOE.click()

#Date
DATE = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[5]/td[2]/input')
DATE.send_keys("1121222")

#Profession(checkbox)
Profession = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[6]/td[2]/span[2]/input')
Profession.click()

#Profile Picture
Picture = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[7]/td[2]/input')
Picture.send_keys("C:\\Users\\USER\\Desktop\\IMG_2381.png")

#Flavours of (checkbox)
Flavours = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[8]/td[2]/span[3]/input')
Flavours.click()

#Continents
Continents = Select(driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[9]/td[2]/select'))
Continents.select_by_index(5)

#Commands
Commands = Select(driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[10]/td[2]/select'))
Commands.select_by_index(4)

#button
But = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/form/div/table/tbody/tr[11]/td[2]/button')
But.send_keys(Keys.RETURN)

# 等待警告框出現
alert = Alert(driver)

# 獲取警告框的文本
alert_text = alert.text
print("Alert Text:", alert_text)

# 確認警告框（點擊確定按鈕）
alert.accept()

input("Press Enter to close the browser...")
#driver.close() # 關閉# 找到帳號和密碼的輸入框
