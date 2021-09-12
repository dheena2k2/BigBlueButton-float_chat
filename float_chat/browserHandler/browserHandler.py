from . import helper
from . import tag_priority
from selenium.common.exceptions import StaleElementReferenceException
import os
import xml.etree.ElementTree as Et
import time
import _thread as thread


class WebHandler:
    """
    This class handles the collection of data from the chat site
    updates in the chat box is notified to other methods through callback
    """
    def __init__(self, browser_name='chrome'):
        """
        This method collects all the required data from
        float_chat/data/base_data.xml file and opens a browser to control
        :param browser_name: indicates the type of browser to open. Example, 'chrome'
        """
        self.browser_name = browser_name

        current_dir = os.getcwd()
        self.application_dir = helper.get_parent_dir(current_dir, level=1)  # path of the main directory float_chat
        self.data_dir = os.path.join(self.application_dir, 'data')  # path of data directory

        base_data_path = os.path.join(self.data_dir, 'base_data.xml')  # path of base_data.xml
        xp = XmlParser(base_data_path)
        
        driver_dir = os.path.join(self.data_dir, 'drivers')
        driver_name = xp.get_browser_driver_name(browser_name)
        driver_path = os.path.join(driver_dir, driver_name)  # path of the browser driver
        default_tab_url = xp.get_site('default')[1]

        self.driver = helper.open_browser(browser_name, driver_path, default_tab_url)  # open browser
        self.default_tab = self.driver.current_window_handle  # saving for easy switch

        self.chat_tab_details = xp.get_site('chat')  # get chat site details to switch
        self.username_xpath, self.message_xpath = xp.get_chat_xpaths()  # get chat username and message xpath
        self.is_listening = False  # if listening to chat

    def listen_chat(self, callback):
        """
        Initiates listening the chat by calling self.start_float_chat
        :param callback: method to call in case of change in chat
        :return: None
        """
        self.is_listening = True  # keeps while loop running for listening to chats
        thread.start_new_thread(self.start_float_chat, tuple([callback]))  # create new thread

    def stop_listening(self):
        """
        Stops the listening to the chat
        :return: None
        """
        self.is_listening = False
    
    def start_float_chat(self, callback):
        """
        Listens to the chat repeatedly and calls callback method in case of changes in chat
        :param callback: method to call in case of change in chat
        :return: None
        """
        driver = self.driver
        self.is_listening = helper.switch_to_chat_tab(driver, self.chat_tab_details)  # switch to chat tab
        usernames = list()  # get chat usernames
        messages = list()  # get chat contents

        is_cool = True  # if chat is not active
        cool_down_time = 2  # seconds to wait for cool down
        cool_rate = helper.Rate(1)  # refresh per second
        hot_rate = helper.Rate(10)  # refresh per second when chat box is active
        last_cool_time = time.time()  # to keep track of cool down time

        while self.is_listening:
            try:
                new_usernames = [x.text for x in driver.find_elements_by_xpath(self.username_xpath)]  # get new data
                new_messages = [x.text for x in driver.find_elements_by_xpath(self.message_xpath)]
            except StaleElementReferenceException as e:
                new_usernames = usernames
                new_messages = messages

            if new_usernames != usernames or new_messages != messages:  # if change in chat
                is_cool = False  # set chat is active
                last_cool_time = time.time()
                chat_data = [(new_usernames[i], new_messages[i]) for i in range(min(len(new_usernames), len(new_messages)))]
                chat_data = chat_data[::-1]  # arranging latest first order
                callback(chat_data=chat_data)  # indicate to callback
                usernames = new_usernames
                messages = new_messages

            if is_cool:
                cool_rate.sleep()
            else:
                if time.time() - last_cool_time > cool_down_time:  # if cool down time is passed
                    is_cool = True
                hot_rate.sleep()

    def set_default_tab(self):
        """
        Sets the currently handling tab as default
        :return: None
        """
        self.default_tab = self.driver.current_window_handle

    def switch_to_default_tab(self):
        """
        Switches to already set default tab
        :return: None
        """
        if self.default_tab:
            self.driver.switch_to.window(self.default_tab)


class XmlParser:
    def __init__(self, xml_path):
        """
        Obtains base_data.xml file and set the root for parsing
        :param xml_path: path of base_data.xml file
        """
        self.xml_file_tree = Et.parse(xml_path)
        self.root = self.xml_file_tree.getroot()
    
    def get_browser_driver_name(self, name):
        """
        Fetches the name of the browser driver
        :param name: name of the browser. Example, 'chrome'
        :return: name of the browser driver. Example, 'chromedriver'
        """
        drivers = self.root.findall('.//browserDrivers/driver')  # find all driver tags
        for driver in drivers:
            if driver.attrib['name'] == name:
                return driver.text  # returns name if match found
    
    def get_site(self, name):
        """
        Fetches details of the chat site, details which have high priority
        :return: type of the detail and detail itself
        """
        sites = self.root.findall('.//sites/site')  # get all saved site
        tag_name = None
        tag_info = None
        priority = None
        for site in sites:
            if site.attrib['name'] == name:  # if site's name attribute is 'chat'
                for info in site:
                    if priority is None or tag_priority[info.tag] < priority:  # get highest priority info
                        priority = tag_priority[info.tag]
                        tag_name = info.tag
                        tag_info = info.text
        
        return tag_name, tag_info

    def get_chat_xpaths(self):
        """
        Fetches the xpath of chat usernames and messages in the chat site
        :return: xpath of usernames and their messages
        """
        username_xpath = self.root.find('.//xpaths/xpath[@name="username"]').text
        message_xpath = self.root.find('.//xpaths/xpath[@name="message"]').text

        return username_xpath, message_xpath
