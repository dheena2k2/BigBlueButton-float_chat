import tkinter as tk
from . import helper
from . import ChatBox


class MainMenu(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

        buttons = dict()
        buttons['float_chat'] = tk.Button(self, text='Start float chat', command=self.toggle_chat)
        buttons['quit'] = tk.Button(self, text='Quit', command=self.if_quit)
        self.buttons = buttons

        i = 0
        for x in buttons:
            buttons[x].grid(row=0, column=i)
            i += 1

        self.web_handler = None
        self.float_chat_on = False
        self.float_chat_toplevel = None

    def connect_browser_handler(self, wh):
        self.web_handler = wh

    def toggle_chat(self):
        if not self.float_chat_on:
            self.float_chat_toplevel = tk.Toplevel(self)
            self.float_chat_toplevel.protocol('WM_DELETE_WINDOW', self.on_float_chat_close)
            self.float_chat_toplevel.attributes('-topmost', True)
            chat_box = ChatBox.ChatBox(self.float_chat_toplevel)
            chat_box.pack(expand=tk.YES, fill=tk.Y)
            chat_box.align_window()
            self.float_chat_toplevel.resizable(False, True)
            self.web_handler.listen_chat(chat_box.update_callback)
            self.buttons['float_chat'].config(text='Stop float chat')
            self.float_chat_on = True
        else:
            self.on_float_chat_close()

    def on_float_chat_close(self):
        self.web_handler.stop_listening()
        self.float_chat_toplevel.destroy()
        self.buttons['float_chat'].config(text='Start float chat')
        self.float_chat_on = False

    def if_quit(self):
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
