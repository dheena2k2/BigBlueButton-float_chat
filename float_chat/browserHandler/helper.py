from selenium import webdriver


def open_chrome(cd_path, website=None):
    driver = webdriver.Chrome(cd_path)
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
                            break
    if driver.title == title:
            return current_window
    else:
            driver.switch_to.window(current_window)
            return None
