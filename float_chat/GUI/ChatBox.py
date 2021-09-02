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
        self.username = tk.StringVar()  # label holding username
        self.content = tk.StringVar()  # label holding content
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and packs widget
        :return: None
        """
        user_font = ('calibri', 11, 'bold')  # font specifications
        content_font = ('calibri', 11, 'normal')
        tip_font = ('calibri', 10, 'normal')
        username_label = tk.Label(self, textvariable=self.username, anchor=tk.W)  # create label widgets
        content_label = tk.Label(self, textvariable=self.content)

        username_label.config(font=user_font, width=30, justify=tk.LEFT)  # configuring widgets
        content_label.config(font=content_font, width=30, justify=tk.LEFT)
        content_label.config(wraplength=content_label.winfo_reqwidth())  # wrap content according to widget width

        username_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, anchor=tk.N)  # arranging widgets
        content_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, padx=(20, 0))

    def set_contents(self, username, content):
        """
        Assign values to username and content label
        :param username: username of the message sender
        :param content: content of the message
        :return: None
        """
        rev_username = username[:28] + '...' if len(username) > 30 else username
        self.username.set(rev_username)
        self.content.set(content + '\n')  # '\n' to separate messages


if __name__ == '__main__':
    root = tk.Tk()
    widget = Chat(root)
    widget.pack(expand=tk.YES, fill=tk.BOTH)
    message = 'The len() Python method returns the length of a list, string, dictionary, or any other iterable data format in Python. The len() method takes one argument: an iterable object. ... The Python len() method is a built-in function that can be used to calculate the length of any iterable object.'
    widget.set_contents('2019BCS0038 Dheenadhayalan Ramadoss', message)
    root.mainloop()
