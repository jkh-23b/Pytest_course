import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test...")
    driver = webdriver.Chrome()

    yield driver
    print("\nquit browser...")
    driver.quit()



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox",
                     choices=('chrome', 'firefox'))


@pytest.fixture(scope="function")
def browser(request):
    user_languages = ['en', 'ru']
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_languages}
    )
    options_firefox = OptionsFirefox()
    options_firefox.set_preference('intl.accept_languages', user_languages)
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
