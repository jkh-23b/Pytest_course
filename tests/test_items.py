from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_having_trash(browser):
    browser.get(link)
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, "[value='Добавить в корзину']")