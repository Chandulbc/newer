from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
browser=webdriver.Chrome()
browser.get('https://www.keka.com/')
browser.implicitly_wait(20)
print(browser.find_element(By.XPATH,'//*[@id="navbarCollapse"]/ul[2]/li[1]/a'))
#login page
browser.find_element(By.XPATH,'//*[@id="navbarCollapse"]/ul[2]/li[1]/a').click()
#username
browser.find_element(By.XPATH,'//*[@id="email"]').send_keys("cakurathi@msystechnologies.com")
#click
browser.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[2]/form[1]/div/button').click()
#continue
browser.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/div[2]/button").click()
#pasww
browser.find_element(By.XPATH,'//*[@id="password"]').send_keys("Chandu321//")
#click
browser.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/form/div/button").click()
t.sleep(10)
element=browser.find_element(By.XPATH,'/html/body/xhr-app-root/div/xhr-left-nav/nav/div/ul/li[2]/a')
webdriver.ActionChains(browser).move_to_element(element).perform()
t.sleep(5)
element2=browser.find_element(By.XPATH,'/html/body/xhr-app-root/div/xhr-left-nav/nav/div/ul/li[2]/div/ul/li[2]/a')
webdriver.ActionChains(browser).move_to_element(element2).click().perform()
t.sleep(5)
element3=browser.find_element(By.XPATH,'/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[2]/a[1]')
webdriver.ActionChains(browser).move_to_element(element3).click().perform()
t.sleep(10)
element4=browser.find_element(By.XPATH,'/html/body/modal-container/div[2]/div/employee-attendance-working-remotely-request/div[2]/form/div/div/div[1]/div[1]/div[1]/div/span[2]')
webdriver.ActionChains(browser).move_to_element(element4).click().perform()
t.sleep(10)
element5=browser.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[5]/td[2]')
webdriver.ActionChains(browser).move_to_element(element5).click().perform()
t.sleep(10)

element6=browser.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[5]/td[5]')
webdriver.ActionChains(browser).move_to_element(element6).click().perform()
t.sleep(10)
element7=browser.find_element(By.XPATH,'/html/body/modal-container/div[2]/div/employee-attendance-working-remotely-request/div[2]/form/div/div/div[3]/textarea')
webdriver.ActionChains(browser).move_to_element(element7).click().send_keys("dfhdsfsdh").perform()
t.sleep(10)


