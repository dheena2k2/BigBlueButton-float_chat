import tkinter as tk
from browserHandler import browserHandler
from GUI import MainMenu
from GUI import helper


class Application:
    def __init__(self):
        """
        Combines the created modules and create the main application
        :return: None
        """
        web_handler = browserHandler.WebHandler()  # open browser

        # create and configure root window
        root = tk.Tk()
        root.title('Float chat menu')
        root.attributes('-topmost', True)
        root.protocol('WM_DELETE_WINDOW', self.at_close)

        # create and configure main menu
        main_menu = MainMenu.MainMenu(root)
        main_menu.pack()
        main_menu.align_window()
        main_menu.connect_browser_handler(web_handler)

        root.resizable(False, False)  # root is not resizable
        self.root = root  # to facilitate closing
        root.mainloop()

    def at_close(self):
        """
        Called when close button is pressed
        :return: None
        """
        if helper.quit_popup():  # if quit is confirmed
            self.root.destroy()


if __name__ == '__main__':
    Application()
