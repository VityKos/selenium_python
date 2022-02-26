from selenium import webdriver
import os


def download_libraries():
    os.system("pip3 install selenium")


def get_html_code_by(url):
    driver = webdriver.Chrome(executable_path="/Users/viktor/PycharmProjects/selenium_python/chromedriver")

    try:
        driver.get(url)
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
