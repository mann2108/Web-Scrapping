'''
@author mann2108

********** WEB Scrapping **********

Task :  downloading all the solution codes from codechef practice section located in
        'codechef.com/users/user_name' and store them in 'Problems' directory.

Prerequisite Actions : -

1. Install Selenium globally using - 'pip install selenium'
   If you are using pycharm then also install in it too for hint feature.
   Pycharm Installation : file->settings->Project Interpreter->click '+'->write selenium in search bar->Click Installed.

2. Create 'Problems' directory in same directory where this file exist.

3. Now download the chromedriver from the given link and just give the path to it in below code.
   In case some error occur due to version then try all different version of chrome browser you are
   using and select accordingly.

4. Count the no. of problems you have in practice problem section on codechef and assign it to for loop.

5. Give your profile url in 'driver.get()' method.

6. Lastly after getting text from line 37 give the extension of file name as '.py' or '.cpp' whatever your
   written in.

**********Happy Coding and Scrapping**********

'''
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#Give path too your chrome driver you downloaded compatible with your installed chrome browser
driver = webdriver.Chrome(executable_path="chromedriver.exe")

for i in range(32,88):

    #Give your own user profile link here
    driver.get("https://www.codechef.com/users/mann2108")


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    url = "/html/body/main/div/div/div/div/div/section[6]/div/article[1]/p[1]/span/a["+str(i)+"]"

    driver.find_element_by_xpath(url).click()

    #If you believe that your internet is too fast then ignore this line.
    time.sleep(5)

    temp = driver.find_element_by_xpath("/html/body/center/center/table/tbody/tr/td/div/div/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/ul/li/a").get_attribute("href")
    name_of_problem = driver.find_element_by_xpath("/html/body/center/center/table/tbody/tr/td/div/div/div/div/div[2]/div/div[2]/h2/a[2]").text
    new  = temp.replace("viewsolution","viewplaintext")
    driver.get(new)
    code = driver.find_element_by_xpath("/html/body/pre").text

    #Extension of file respective of coding language you used.
    name = "Problems/"+name_of_problem+".cpp"
    print(name)

    #File handling
    file = open(name,'w')
    file.write(code)
    file.close()


driver.close()
