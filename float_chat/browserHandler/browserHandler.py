from . import helper
from . import tag_priority
# from selenium.webdriver.common.keys import Keys
import os
import xml.etree.ElementTree as Et
import time
import _thread as thread


class WebHandler:
    def __init__(self, browser_name):
        self.browser_name = browser_name

        current_dir = os.getcwd()
        self.application_dir = helper.get_parent_dir(current_dir, level=1)
        self.data_dir = os.path.join(self.application_dir, 'data')

        base_data_path = os.path.join(self.data_dir, 'base_data.xml')
        xp = XmlParser(base_data_path)
        
        driver_dir = os.path.join(self.data_dir, 'drivers')
        driver_name = xp.get_browser_driver_name(browser_name)
        driver_path = os.path.join(driver_dir, driver_name)

        self.driver = helper.open_browser(browser_name, driver_path)
        self.default_tab = None

        self.chat_tab_details = xp.get_chat_site()
        self.username_xpath, self.message_xpath = xp.get_chat_xpaths()
        self.is_listening = False

    def listen_chat(self, callback):
        self.is_listening = True
        thread.start_new_thread(self.start_float_chat, callback)

    def stop_listening(self):
        self.is_listening = False
    
    def start_float_chat(self, callback):
        driver = self.driver
        self.default_tab = helper.switch_to_chat_tab(driver, self.chat_tab_details)
        usernames = [x.text for x in driver.find_elements_by_xpath(self.username_xpath)]
        messages = [x.text for x in driver.find_elements_by_xpath(self.message_xpath)]

        is_cool = True
        cool_down_time = 2  # seconds
        cool_rate = helper.Rate(1)  # refresh per second
        hot_rate = helper.Rate(10)  # refresh per second when chat box is active
        last_cool_time = time.time()

        while self.is_listening:
            new_usernames = [x.text for x in driver.find_elements_by_xpath(self.username_xpath)]
            new_messages = [x.text for x in driver.find_elements_by_xpath(self.message_xpath)]

            if new_usernames != usernames or new_messages != messages:
                is_cool = False
                last_cool_time = time.time()
                callback(usernames=new_usernames, messages=new_messages)
                usernames = new_usernames
                messages = new_messages

            if is_cool:
                cool_rate.sleep()
            else:
                if time.time() - last_cool_time > cool_down_time:
                    is_cool = True
                hot_rate.sleep()

    def set_default_tab(self):
        self.default_tab = self.driver.current_window_handle

    def switch_to_default_tab(self):
        if self.default_tab:
            self.driver.switch_to.window(self.default_tab)


class XmlParser:
    def __init__(self, xml_path):
        self.xml_file_tree = Et.parse(xml_path)
        self.root = self.xml_file_tree.getroot()
    
    def get_browser_driver_name(self, name):
        drivers = self.root.findall('.//browserDrivers/driver')
        for driver in drivers:
            if driver.attrib['name'] == name:
                return driver.text
    
    def get_chat_site(self):
        sites = self.root.findall('.//sites/site')
        tag_name = None
        tag_info = None
        priority = None
        for site in sites:
            if site.attrib['name'] == 'chat':
                for info in site:
                    if priority is None or tag_priority[info.tag] < priority:
                        priority = tag_priority[info.tag]
                        tag_name = info.tag
                        tag_info = info.text
        
        return tag_name, tag_info

    def get_chat_xpaths(self):
        username_xpath = self.root.find('.//xpaths/xpath[@name="username"]').text
        message_xpath = self.root.find('.//xpaths/xpath[@name="message"]').text

        return username_xpath, message_xpath
