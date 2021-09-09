import tkinter as tk


class Chat(tk.Frame):
    """
    This frame is the body to hold a single chat message which consist of
    username and the respective message
    """
    def __init__(self, parent=None, **kwargs):
        """
        Initializing necessary values
        :param parent: parent frame
        :param kwargs: extra parameters for tkinter Frame
        """
        super().__init__(parent, **kwargs)
        self.parent = parent

    def create_widgets(self):
        """
        Creates and packs widget
        :return: tkinter string variable of username and message content aka data variables of chat cell
        """
        username = tk.StringVar()  # label holding username
        content = tk.StringVar()  # label holding content

        user_font = ('calibri', 10, 'bold')  # font specifications
        content_font = ('calibri', 10, 'normal')
        username_label = tk.Label(self, textvariable=username, anchor=tk.W)  # create label widgets
        content_label = tk.Label(self, textvariable=content, anchor=tk.W)

        username_label.config(font=user_font, width=30, justify=tk.LEFT)  # configuring widgets
        content_label.config(font=content_font, width=30, justify=tk.LEFT)
        content_label.config(wraplength=content_label.winfo_reqwidth())  # wrap content according to widget width

        username_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, anchor=tk.N)  # arranging widgets
        content_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, padx=(20, 0))

        return username, content


class ChatArray(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        """
        Initializing necessary values
        :param parent: parent frame
        :param total_chats: number of Chat frames the ChatArray should have
        :param kwargs: extra parameters for tkinter Frame
        """
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.chats = None  # list which will contain Chat cells
        self.is_created = False  # avoid multiple calls to create_widget method

    def create_widgets(self, total_chats=10):
        """
        Creates and arrange Chat cells
        :return: tuple of chat cell data variables
        """
        if self.is_created:  # proceed only if this is the first call
            return
        chats = list()  # holds chat data
        for i in range(total_chats):
            chat_cell = Chat(self)  # create chat cells
            chat = chat_cell.create_widgets()
            chat_cell.grid(row=i, column=0)  # arrange chat cells
            chats.append(chat)
        self.chats = tuple(chats[::-1])  # Arrange chat in bottom first order
        self.is_created = True

        return self.chats


class ChatBox(tk.Frame):
    """
    This frame combine all the other frames to create whole chat box
    """
    def __init__(self, parent=None, total_chats=None, **kwargs):
        """
        Initializing necessary values
        :param parent: parent frame
        :param total_chats: number of Chat frames the ChatArray should have
        :param kwargs: extra parameters for tkinter Frame
        """
        super().__init__(parent, **kwargs)
        self.canvas = tk.Canvas(self)  # to contain ChatArray
        self.chat_array = ChatArray(self.canvas)
        if total_chats:
            self.chat_data = self.chat_array.create_widgets(total_chats)
        else:
            self.chat_data = self.chat_array.create_widgets()

        self.chat_array.update()
        chat_array_width = self.chat_array.winfo_reqwidth()
        self.canvas.config(width=chat_array_width, height=300)  # fixing size of canvas
        self.fit_canvas()
        self.canvas.config(highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self)

        # configuring canvas and scrollbar
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # arranging widgets
        self.canvas.create_window(0, 0, anchor=tk.NW, window=self.chat_array)

        self.canvas.grid(row=0, column=0, sticky=tk.NS)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.rowconfigure(0, weight=1)

    def update_callback(self, chat_data):
        for i in range(len(chat_data)):  # update from bottom
            username, content = chat_data[i]
            rev_username = username[:28] + '...' if len(username) > 30 else username  # add continue dots
            username_var, content_var = self.chat_data[i]
            username_var.set(rev_username)
            content_var.set(content + '\n')

        for i in range(len(chat_data), len(self.chat_data)):  # remove entries in remaining chat cells
            username_var, content_var = self.chat_data[i]
            username_var.set('')
            content_var.set('')

        self.fit_canvas()

    def fit_canvas(self):
        self.chat_array.update()
        chat_array_width = self.chat_array.winfo_reqwidth()
        chat_array_height = self.chat_array.winfo_reqheight()
        self.canvas.config(scrollregion=(0, 0, chat_array_width, chat_array_height))


if __name__ == '__main__':
    root = tk.Tk()
    widget = ChatBox(root)
    widget.pack(expand=tk.YES, fill=tk.Y)
    root.resizable(False, True)
    root.mainloop()
