from selenium import webdriver
from time import sleep

# my comment
my_driver = webdriver.Chrome(executable_path="c:/Users/User/Desktop/chromedriver.exe")
my_driver.get("c:/Users/User/Desktop/tip_calc/index.html")
my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("5")
my_driver.find_element(by="id", value="music").send_keys("5")
my_driver.find_element(by="id", value="calculate").click()
expected = "3.05"
actual = my_driver.find_element(by="id", value="tip").text

if expected == actual:
    print("Great")
else:
    print("Not Great")
