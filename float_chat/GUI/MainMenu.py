import tkinter as tk
from . import helper
from . import ChatBox


class MainMenu(tk.Frame):
    """
    Frame of opening GUI facilitates float chat toggle actions
    """
    def __init__(self, parent=None, **kwargs):
        """
        Initializing necessary values
        :param parent: parent frame
        :param kwargs: extra parameters for tkinter Frame
        """
        super().__init__(parent, **kwargs)
        self.parent = parent

        buttons = dict()  # contains the main buttons
        buttons['float_chat'] = tk.Button(self, text='Start float chat', command=self.toggle_chat)  # toggles float chat
        buttons['quit'] = tk.Button(self, text='Quit', command=self.if_quit)  # quit button
        self.buttons = buttons

        # arrange buttons
        i = 0
        for x in buttons:
            buttons[x].grid(row=0, column=i)
            i += 1

        self.web_handler = None  # web handler of the program
        self.float_chat_on = False  # if float chat window is up
        self.float_chat_toplevel = None  # toplevel of float chat window

    def connect_browser_handler(self, wh):
        """
        Sets the web handler from browserHandler.browserHandler.WebHandler
        :param wh: created WebHandler object
        :return: None
        """
        self.web_handler = wh

    def toggle_chat(self):
        """
        Opens float chat if not available
        Closes float chat if already opened
        :return: None
        """
        if not self.float_chat_on:
            self.float_chat_toplevel = tk.Toplevel(self)  # toplevel for float chat
            self.float_chat_toplevel.protocol('WM_DELETE_WINDOW', self.on_float_chat_close)
            self.float_chat_toplevel.attributes('-topmost', True)  # setting float chat top most

            # create and align chat box
            chat_box = ChatBox.ChatBox(self.float_chat_toplevel)
            chat_box.pack(expand=tk.YES, fill=tk.Y)
            chat_box.align_window()
            self.float_chat_toplevel.resizable(False, True)
            self.web_handler.listen_chat(chat_box.update_callback)

            self.buttons['float_chat'].config(text='Stop float chat')  # change button text
            self.float_chat_on = True  # change float chat on status
        else:
            self.on_float_chat_close()

    def on_float_chat_close(self):
        """
        Called when float chat is to be closed
        :return: None
        """
        self.web_handler.stop_listening()  # stops web handler from listening
        self.float_chat_toplevel.destroy()  # close float chat
        self.buttons['float_chat'].config(text='Start float chat')  # change button text
        self.float_chat_on = False  # change float chat on status

    def if_quit(self):
        """
        When the main menu is to be quit
        :return: None
        """
        answer = helper.quit_popup()
        if answer:
            self.parent.destroy()

    def align_window(self):
        """
                Align the main menu to the bottom right
                :return: None
                """
        self.parent.update()

        # get screen info
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        # get window info
        window_width = self.parent.winfo_width()
        window_height = self.parent.winfo_height()

        # determine position of the window
        x = screen_width - window_width/2 - 120
        y = screen_height - window_height/2 - 60

        # move the window to determined position
        self.parent.geometry('+%d+%d' % (x, y))
