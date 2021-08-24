from selenium import webdriver
import os
import time


open_browser_methods = {'chrome': webdriver.Chrome}


def open_browser(name, cd_path, website=None):
    driver = open_browser_methods[name](cd_path)
    if website:
        driver.get(website)

    return driver


def switch_tab_by_title(driver, title):
    current_window = driver.current_window_handle
    tabs = driver.window_handles
    for tab in tabs:
        if tab != current_window:
            driver.switch_to.window(tab)
            if driver.title == title:
                return
    driver.switch_to.window(current_window)


select_tab_methods = {'title': switch_tab_by_title}


def switch_to_chat_tab(driver, tab_details):
    return select_tab_methods[tab_details[0]](driver, tab_details[1])


def get_parent_dir(child_path, level=0):
    parent_path = child_path
    for i in range(level):
        parent_path = os.path.dirname(parent_path)
    
    return parent_path


class Rate:
    def __init__(self, rate):
        self.call_time_gap = 1 / rate
        self.last_call = time.time()

    def sleep(self):
        time_now = time.time()
        elapsed_time = time_now - self.last_call
        if elapsed_time < self.call_time_gap:
            time.sleep(self.call_time_gap - elapsed_time)
        self.last_call = time_now
