from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Eddie\PycharmProjects\NewMinerobo\venv\Lib\site-packages\seleniumbase\drivers/chromedriver.exe")
driver.close()
driver.quit()