import time
import os

delay = 1

def download_libraries():
    os.system("pip3 install selenium")


def set_delay(t):
    delay = t


def get_html_code_by(url):
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path="/Users/viktor/PycharmProjects/selenium_python/chromedriver")

    try:
        driver.get(url)
        time.sleep(delay)
        return driver.page_source

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    print("hellow")


if __name__ == '__main__':
    main()
