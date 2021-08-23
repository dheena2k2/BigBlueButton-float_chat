from selenium import webdriver
from . import select_tab_methods
import os


open_browser_methods = {'chrome': webdriver.Chrome}


def open_browser(name, cd_path, website=None):
    driver = open_browser_methods[name](cd_path)
    if website:
        driver.get(website)

    return driver


def switch_to_chat_tab(driver, tab_details):
    return select_tab_methods[tab_details[0]](driver, tab_details[1])


def switch_tab_by_title(driver, title):
    current_window = driver.current_window_handle
    tabs = driver.window_handles
    for tab in tabs:
        if tab != current_window:
            driver.switch_to.window(tab)
            if driver.title == title:
                break
    if driver.title == title:
        return current_window
    else:
        driver.switch_to.window(current_window)
        return None


def get_parent_dir(child_path, level=0):
    parent_path = child_path
    for i in range(level):
        parent_path = os.path.dirname(parent_path)
    
    return parent_path
