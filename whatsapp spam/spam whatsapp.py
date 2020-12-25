from PyQt5 import QtWidgets, uic
from selenium import webdriver 
import time

app = QtWidgets.QApplication([])
dig =uic.loadUi("app_spam_ui.ui")

def run_program():
    url = 'https://web.whatsapp.com/'
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)

    time.sleep(10) # 10 secons

    user = str(dig.e1.text())
    message = str(dig.e2.text())
    n = int(dig.e3.text())

    browser.find_element_by_css_selector("#side > div._1Ra05 > div > label > div > div._1awRl.copyable-text.selectable-text").send_keys(user)
    browser.find_element_by_css_selector("#side > div._1Ra05 > div > label > div > div._1awRl.copyable-text.selectable-text").send_keys(webdriver.common.keys.Keys.ENTER)

    for i in range(n):
        browser.find_element_by_css_selector("#main > footer > div._3SvgF._1mHgA.copyable-area > div.DuUXI._1WoQE > div > div._1awRl.copyable-text.selectable-text").send_keys(message)
        browser.find_element_by_css_selector("#main > footer > div._3SvgF._1mHgA.copyable-area > div.DuUXI._1WoQE > div > div._1awRl.copyable-text.selectable-text").send_keys(webdriver.common.keys.Keys.ENTER)

    #time.sleep(60)

    browser.close()
    
def run_program2():
    dig.e1.setText('')
    dig.e2.setText('')
    dig.e3.setText('')


dig.button1.clicked.connect(run_program)
dig.button2.clicked.connect(run_program2)


dig.show()
app.exec()
