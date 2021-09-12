import tkinter as tk
from browserHandler import browserHandler
from GUI import MainMenu
from GUI import helper


def main():
    """
    Combines the created modules and create the main application
    :return: None
    """
    web_handler = browserHandler.WebHandler()  # open browser

    # create and configure root window
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.protocol('WM_DELETE_WINDOW', helper.quit_popup)

    # create and configure main menu
    main_menu = MainMenu.MainMenu(root)
    main_menu.pack()
    main_menu.align_window()
    main_menu.connect_browser_handler(web_handler)

    root.resizable(False, False)  # root is not resizable
    root.mainloop()


if __name__ == '__main__':
    main()
