import time
import os


def download_libraries():
    os.system("pip3 install selenium")


class HTML_getter:
    delay = 1
    path = ""

    def __init__(self, delay=1, path=""):
        self.delay = delay
        self.path = path

    def get_html_code_by(self, url):
        from selenium import webdriver

        driver = webdriver.Chrome(executable_path=self.path)

        try:
            driver.get(url)
            time.sleep(self.delay)
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
