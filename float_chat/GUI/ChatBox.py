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

        user_font = ('calibri', 11, 'bold')  # font specifications
        content_font = ('calibri', 11, 'normal')
        tip_font = ('calibri', 10, 'normal')
        username_label = tk.Label(self, textvariable=username, anchor=tk.W)  # create label widgets
        content_label = tk.Label(self, textvariable=content)

        username_label.config(font=user_font, width=30, justify=tk.LEFT)  # configuring widgets
        content_label.config(font=content_font, width=30, justify=tk.LEFT)
        content_label.config(wraplength=content_label.winfo_reqwidth())  # wrap content according to widget width

        username_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, anchor=tk.N)  # arranging widgets
        content_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, padx=(20, 0))

        return username, content


class ChatArray(tk.Frame):
    def __init__(self, parent=None, total_chats=10, **kwargs):
        """
        Initializing necessary values
        :param parent: parent frame
        :param total_chats: number of Chat frames the ChatArray should have
        :param kwargs: extra parameters for tkinter Frame
        """
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.total_chat = total_chats
        self.chats = None  # list which will contain Chat cells

    def create_widgets(self):
        """
        Creates and arrange Chat cells
        :return: tuple of chat cell data variables
        """
        chats = list()  # holds chat data
        for i in range(self.total_chat):
            chat_cell = Chat(self)  # create chat cells
            chat = chat_cell.create_widgets()
            chat_cell.grid(row=i, column=0)  # arrange chat cells
            chats.append(chat)
        self.chats = tuple(chats)  # creating immutable order

        return self.chats


if __name__ == '__main__':
    root = tk.Tk()
    widget = ChatArray(root)
    widget.pack(expand=tk.YES, fill=tk.BOTH)
    message = 'The len() Python method returns the length of a list, string, dictionary, or any other iterable data format in Python. The len() method takes one argument: an iterable object. ... The Python len() method is a built-in function that can be used to calculate the length of any iterable object.'
    user = '2019BCS0038 Dheenadhayalan Ramadoss'
    chats = widget.create_widgets()
    '''for username, content in chats:
        username.set(user)
        content.set(message+'\n')'''
    root.mainloop()
