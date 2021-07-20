from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

#initialize web driver
driver = webdriver.Chrome('C:\Python39\loginscript\chromedriver.exe')

print('Auto Log In')
logInSuccess = False

while logInSuccess is False:

    #input username and password
    userName = input('username: ')
    userName = userName + "@usf.edu"
    passWord = input('password: ')

    #retrieve usf website
    driver.get('https://www.usf.edu/')

    #click log in button
    openLogin = driver.find_element_by_class_name('utilNav_link')
    openLogin.click()

    try:    
        print('Attempting login...')

        #waits for username input then sends username
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'i0116')))
        userBar = driver.find_element_by_id('i0116')
        userBar.send_keys(userName)

        #hit the next button
        nextButton = driver.find_element_by_id('idSIButton9')
        nextButton.click()

        #wait for password input then sends password
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'i0118')))
        passBar = driver.find_element_by_id('i0118')
        passBar.send_keys(passWord)

        #definite wait function to avoid security
        time.sleep(5)

        #find and click submit button
        subButton = driver.find_element_by_id('idSIButton9')
        subButton.click()

        #looks for next code input to verify login success
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'idTxtBx_SAOTCC_OTC')))

        #successful login to break while loop
        logInSuccess = True
    except:
        print('Login unsuccessful. Try again:')
else:
    print('Login successful!')

phoneCode = False

while phoneCode is False:
    try:
        verCode = input('Phone code: ')
        time.sleep(5)

        codeBar = driver.find_element_by_id('idTxtBx_SAOTCC_OTC')
        codeBar.send_keys(verCode)

        verifyButton = driver.find_element_by_id('idSubmit_SAOTCC_Continue')
        verifyButton.click()

        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'idSIButton9')))

        print('Phone verification successful!')
        phoneCode = True

        phoneNext = driver.find_element_by_id('idSIButton9')
        phoneNext.click()
    except:
        print('Phone verification unsuccessful. Try again.')