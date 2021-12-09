import json
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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

    # def smart_wait(self, selector):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.ID, selector['selector'])))
    #
    #     print(element)

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
        # time.sleep(1.0)
        element = self.get_element(selector, time_wait)
        # print(type(element))
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

    def put_in_cookie(self, cookie=None):
        """If cookie didn't pass into argument function call :
        Function grab cookie in file and add they into browser."""
        if cookie is None:
            with open('pages_objects/cookies.json', 'r') as json_file:
                cookie = json.load(json_file)
                for cook in cookie:
                    self.driver.add_cookie(cook)
        else:
            self.driver.add_cookie(cookie)

    def put_in_local_storage(self, key, value):
        """this function put var into browser local storage"""
        self.driver.execute_script(f"window.localStorage.setItem('{key}','{value}')")
        # self.driver.execute_script("window.localStorage.setItem(\"welcome\",\"true\")")

    def make_swipe_down(self):
        TouchActions(self.driver.swipe(start_x=300, start_y=800, end_x=300, end_y=600, duration=1200))

    def refresh_page(self):
        self.driver.refresh()

    def show_alert(self):
        self.driver.execute_script("alert('what the fuck')")

    def execute_scroll(self, amount=500):
        """scroll, you can throw variable 'amount', count distance for swipe"""
        self.driver.execute_script(f"window.scrollBy(0, {amount})", "")

    # class ScreenshotMaker:
    #     def __init__(self,driver):
    #         self.driver = driver
    #
    #     def capture_screenshot(self):
    #         return self.driver.get_screenshot_as_png()

    def scroll_to_element(self, selector):
        self.wait_element(selector)
        try:
            result = selector['type_selector']
            if result == "by_xpath":
                return ActionChains(self.driver).move_to_element(
                    self.driver.find_element_by_xpath(selector["selector"])).perform()
            elif result == "by_css":
                return ActionChains(self.driver).move_to_element(
                    self.driver.find_element_by_css_selector(selector["selector"])).perform()
            elif result == "by_name":
                return ActionChains(self.driver).move_to_element(
                    self.driver.find_element_by_name(selector["selector"])).perform()
            elif result == "by_link":
                return ActionChains(self.driver).move_to_element(
                    self.driver.find_element_by_link_text(selector["selector"])).perform()
            else:
                return ActionChains(self.driver).move_to_element(
                    self.driver.find_element_by_accessibility_id(selector["selector"])).perform()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="last i see")
            raise SeleniumContainerException("Scroll failed, element:", selector["selector"])

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

    def is_displayed_element(self, selector):
        """Function will be return true if element is_displayed"""
        self.wait_visible_of_element(selector)
        try:
            result = selector['type_selector']
            if result == "by_xpath":
                return self.driver.find_element_by_xpath(selector["selector"]).is_displayed()
            elif result == "by_css":
                return self.driver.find_element_by_css_selector(selector["selector"]).is_displayed()
            elif result == "by_name":
                return self.driver.find_element_by_name(selector["selector"]).is_displayed()
            elif result == "by_link":
                return self.driver.find_element_by_link_text(selector["selector"]).is_displayed()
            else:
                return self.driver.find_element_by_accessibility_id(selector["selector"]).is_displayed()
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

    def get_count_elements(self, selector):
        return len(self.get_elements(selector))

    def get_screen_shot(self):
        """Function return current screen"""
        return self.driver.get_screenshot_as_png()

    def check_var_with_template(self, expected_var, current_var):
        """This function accepts two arguments (expected_var, current_var)
            and compare them.
            After will return value: true or false """
        if expected_var == current_var:
            pass
        elif expected_var != current_var:
            allure.attach(self.get_screen_shot(), name="last_i_seen")
            raise AssertionError(f"'{current_var}' doesn't math with template '{expected_var}'")

    def is_part_of(self, part_text, target_text):
        """checking the occurrence of a part of the text in the text"""
        if part_text in target_text:
            pass
        else:
            allure.attach(self.get_screen_shot(), "last i see")
            raise AssertionError("part_text doesnt exist in target_text")

    def get_set_windows_size(self, width=1440, height=800):
        self.driver.set_window_size(width, height)

    def get_windows_name(self):
        """Function will be return massive of available windows"""
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def close_window_in_focus(self):
        self.driver.close()

    def switch_to_first_frame(self):
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def close_target_window(self):
        self.driver.execute_script("window.close('2');")

