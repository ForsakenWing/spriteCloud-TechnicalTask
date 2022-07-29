import os
import shutil
import time

from selenium.webdriver.support.ui import WebDriverWait


# I COPIED THAT FRAGMENT OF CODE FROM MY FRIENDS/COLLEAGUE REPOSITORY.
# IF YOU`D LIKE TO CONTACT HIM. TELEGRAM USERNAME: @blademax1
class Screenshot:
    name_directory_for_screenshots = []

    def __init__(self):
        if not os.path.exists("./reports"):
            os.mkdir("./reports")

    @staticmethod
    def delete_screenshots():
        folder = "./reports/"
        try:
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            print("\n---------------- Dellete screenshots folder --------------------")
        except FileNotFoundError:
            print("FileNotFoundError")

    def create_dir_for_screenshots(self):
        name_dir = f"screenshots-{time.time()}"
        self.name_directory_for_screenshots.append(name_dir)
        try:
            os.mkdir("./reports/{}/".format(name_dir))
        except FileExistsError:
            print("File exists: /reports/{}".format(name_dir))

    def save_screenshot(self, name):
        self.driver.save_screenshot("./reports/{}/{}.png".format(self.name_directory_for_screenshots[0], name))


class ClassHelper(Screenshot):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait_t = 15
        self.wait = WebDriverWait(self.driver, self.wait_t)

    def navigate_to_page(self, url):
        self.driver.get(url)
