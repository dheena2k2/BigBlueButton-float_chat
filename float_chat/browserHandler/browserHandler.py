import helper
from . import tag_priority
from selenium.webdriver.common.keys import Keys
import os
import xml.etree.ElementTree as ET


class webHandler:
    def __init__(self, browser_name):
        self.browser_name = browser_name

        current_dir = os.getcwd()
        self.application_dir = helper.get_parent_dir(current_dir, level=2)
        self.data_dir = os.path.join(self.application_dir, 'data')

        base_data_path = os.path.join(self.data_dir, 'base_data.xml')
        xp = xmlParser(base_data_path)
        
        driver_dir = os.path.join(self.data_dir, 'drivers')
        driver_name = xp.get_browser_driver_name(browser_name)
        driver_path = os.path.join(driver_dir, driver_name)

        self.driver = helper.open_browser(browser_name, driver_path)
        self.default_tab = None
    
    def start_float_chat(self):
        driver = self.driver
        self.default_tab = helper.switch_tab_by_title(driver, )


class xmlParser:
    def __init__(self, xml_path):
        self.xml_file_tree = ET.parse(xml_path)
        self.root = self.xml_file_tree.getroot()
    
    def get_browser_driver_name(self, name):
        drivers = self.root.findall('.//browserDrivers/driver')
        for driver in drivers:
            if driver.attrib['name'] = name:
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
        
        return (tag_name, tag_name)
