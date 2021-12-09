import json
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumContainerException(Exception):
    pass


class SeleniumFacade():
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_element(self, selector, time_wait=10):
        try:
            wait = WebDriverWait(self.driver, time_wait)
            result = selector['type_selector']
            if result == "by_xpath":
                wait.until(EC.presence_of_element_located((By.XPATH, selector['selector'])))
            elif result == "by_css":
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector['selector'])))
            elif result == "by_name":
                wait.until(EC.presence_of_element_located((By.NAME, selector['selector'])))
            elif result == "by_link":
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, selector['selector'])))
            else:
                wait.until(EC.presence_of_element_located((By.ID, selector['selector'])))
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="last i see")
            raise SeleniumContainerException("Timeout waiting for element", selector['selector'])


    def wait_visible_of_element(self, selector, value=10):
        try:
            wait = WebDriverWait(self.driver, value)
            result = selector['type_selector']
            if result == "by_xpath":
                wait.until(EC.visibility_of_element_located((By.XPATH, selector['selector'])))
            elif result == "by_css":
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector['selector'])))
            elif result == "by_name":
                wait.until(EC.visibility_of_element_located((By.NAME, selector['selector'])))
            elif result == "by_link":
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, selector['selector'])))
            elif result == "by_id":
                wait.until(EC.visibility_of_element_located((By.ID, selector['selector'])))
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="last i see")
            raise SeleniumContainerException("Timeout waiting for element", selector['selector'])


    def get_element(self, selector, time_wait=10):
        self.wait_element(selector, time_wait)
        try:
            result = selector['type_selector']
            if result == "by_xpath":
                return self.driver.find_element_by_xpath(selector["selector"])
            elif result == "by_css":
                return self.driver.find_element_by_css_selector(selector["selector"])
            elif result == "by_name":
                return self.driver.find_element_by_name(selector["selector"])
            elif result == "by_link":
                return self.driver.find_element_by_link_text(selector["selector"])
            else:
                return self.driver.find_element_by_accessibility_id(selector["selector"])
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="last i see")
            raise SeleniumContainerException("Timeout waiting for element", selector["selector"])

    def tap_element(self, selector, time_wait=10):
        """Warning this is beta function to determine type selector
        Keep watching on this"""
        element = self.get_element(selector, time_wait)
        try:
            if isinstance(element, list):
                element[0].click()
            else:
                element.click()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png())
            raise SeleniumContainerException("Wrong element", selector['selector'])

    def send_keys(self, selector, keys):
        element = self.get_element(selector)
        element.send_keys(keys)

    def clear_input(self, selector):
        element = self.get_element(selector)
        element.clear()

    def page_down(self):
        """Key command page down"""
        self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        """Key command page up"""
        self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)

    def key_down(self, how_many_times):
        """Pass on how many times need to press key down: how_many_times"""
        for _ in range(0, how_many_times):
            time.sleep(.5)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)

    def key_up(self, how_many_times):
        """Pass on how many times need to press key up: how_many_times"""
        for _ in range(0, how_many_times):
            time.sleep(.2)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.UP)

    def grab_cookie(self):
        """Grab cookie and save they in file cookies.json
        ATTENTION: every call this function, storage file will be rewrite"""
        with open("pages_objects/cookies.json", 'w') as file:
            json.dump(self.driver.get_cookies(), file)


    def get_element_image(self, selector):
        """Function return png object file if handle made it"""
        self.wait_visible_of_element(selector)
        try:
            result = selector['type_selector']
            if result == "by_xpath":
                return self.driver.find_element_by_xpath(selector["selector"]).screenshot_as_png
            elif result == "by_css":
                return self.driver.find_element_by_css_selector(selector["selector"]).screenshot_as_png
            elif result == "by_name":
                return self.driver.find_element_by_name(selector["selector"]).screenshot_as_png
            elif result == "by_link":
                return self.driver.find_element_by_link_text(selector["selector"]).screenshot_as_png
            else:
                return self.driver.find_element_by_accessibility_id(selector["selector"]).screenshot_as_png
        except Exception as ex:
            allure.attach(self.get_screen_shot(), name="last_i_seen")
            return "!get_element_image couldn't give a png file!"

    def get_element_text(self, selector):
        """Function return text from element if can handle it"""
        self.wait_visible_of_element(selector)
        # self.wait_element(selector)
        try:
            result = selector['type_selector']
            if result == "by_xpath":
                return self.driver.find_element_by_xpath(selector["selector"]).text
            elif result == "by_css":
                return self.driver.find_element_by_css_selector(selector["selector"]).text
            elif result == "by_name":
                return self.driver.find_element_by_name(selector["selector"]).text
            elif result == "by_link":
                return self.driver.find_element_by_link_text(selector["selector"]).text
            else:
                return self.driver.find_element_by_accessibility_id(selector["selector"]).text
        except Exception as ex:
            allure.attach(self.get_screen_shot(), name="last_i_seen")
            return "!get_element_text couldn't give a text from element!"


    def get_elements(self, selector):
        """Function returns elements, those what able find"""
        self.wait_element(selector)
        try:
            type = selector['type_selector']
            if type == "by_xpath":
                return self.driver.find_elements_by_xpath(selector["selector"])
            elif type == "by_css":
                return self.driver.find_elements_by_css_selector(selector["selector"])
            elif type == "by_name":
                return self.driver.find_elements_by_name(selector["selector"])
            elif type == "by_link":
                return self.driver.find_elements_by_link_text(selector["selector"])
            else:
                return self.driver.find_elements_by_accessibility_id(selector["selector"])
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="last i see")
            raise SeleniumContainerException("Timeout waiting for element, or IDKWTFJH", selector["selector"])

    def get_screen_shot(self):
        """Function return current screen"""
        return self.driver.get_screenshot_as_png()






