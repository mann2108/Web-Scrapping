# Web-Scrapping
Implemented realtime problem solution under web scrapping.

@author mann2108

********** WEB Scrapping **********

Task :  downloading all the solution codes from codechef practice section located in
        'codechef.com/users/user_name' and store them in 'Problems' directory.

Prerequisite Actions : -

1. Install Selenium globally using - 'pip install selenium'
   If you are using pycharm then also install there for hint feature.
   Pycharm Installation : file->settings->Project Interpreter->click '+'->write selenium in search bar->Click Installed.

2. Create 'Problems' directory in same directory where this file exist.

3. Now download the chromedriver from the given link and just give the path to it in below code.
   In case some error occur due to version then try all different version of chrome browser you are
   using and select accordingly. ('https://chromedriver.chromium.org/downloads')

4. Count the no. of problems you have in practice problem section on codechef and assign it to for loop.

5. Give your profile url in 'driver.get()' method.

6. Lastly after getting text from line 37 give the extension of file name as '.py', '.cpp', '.java', etc. whatever language you
   writte code in.

**********Happy Coding and Scrapping**********
