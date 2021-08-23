import helper
from . import tag_priority
# from selenium.webdriver.common.keys import Keys
import os
import xml.etree.ElementTree as Et
import time


class WebHandler:
    def __init__(self, browser_name):
        self.browser_name = browser_name

        current_dir = os.getcwd()
        self.application_dir = helper.get_parent_dir(current_dir, level=2)
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
    
    def start_float_chat(self):
        driver = self.driver
        self.default_tab = helper.switch_to_chat_tab(driver, self.chat_tab_details)
        usernames = [x.text for x in driver.find_elements_by_xpath(self.username_xpath)]
        messages = [x.text for x in driver.find_elements_by_xpath(self.message_xpath)]

        for i in range(len(usernames)):
            print(usernames[i])
            print(messages[i])
            print('='*20)

        is_cool = True
        cool_down_time = 2  # seconds
        cool_rate = helper.Rate(1)  # cool_interval = 1  # seconds between refresh
        hot_rate = helper.Rate(10)  # hot_interval = 0.1  # seconds between refresh when chat box is active
        last_cool_time = time.time()

        while True:
            new_usernames = [x.text for x in driver.find_elements_by_xpath(self.username_xpath)]
            new_messages = [x.text for x in driver.find_elements_by_xpath(self.message_xpath)]

            if new_usernames != usernames or new_messages != messages:
                is_cool = False
                last_cool_time = time.time()

                start_at = -1
                for i in range(len(new_usernames)):
                    if new_usernames[-(i+1)] == usernames[-1] and new_messages[-(i+1)] == messages[-1]:
                        start_at = -i
                        break

                while start_at < 0:
                    print(new_usernames[start_at])
                    print(new_messages[start_at])
                    print('='*20)
                    start_at += 1

                usernames = new_usernames
                messages = new_messages

            if is_cool:
                cool_rate.sleep()
            else:
                if time.time() - last_cool_time > cool_down_time:
                    is_cool = True
                hot_rate.sleep()

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
                    if priority is None or tag_priority[tag_name] < priority:
                        priority = tag_priority[tag_name]
                        tag_name = info.tag
                        tag_info = info.text
        
        return tag_name, tag_info

    def get_chat_xpaths(self):
        username_xpath = self.root.find('.//xpaths/xpath[@name="username"]').text
        message_xpath = self.root.find('.//xpaths/xpath[@name="message"]').text

        return username_xpath, message_xpath
