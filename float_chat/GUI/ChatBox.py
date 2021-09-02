import tkinter as tk
import helper


class Chat(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.username = tk.StringVar()  # label holding username
        self.content = tk.StringVar()  # label holding content
        self.create_widgets()

    def create_widgets(self):
        user_font = ('calibri', 11, 'bold')  # font specifications
        content_font = ('calibri', 11, 'normal')
        username_label = tk.Label(self, textvariable=self.username, anchor=tk.W)  # create label widgets
        content_label = tk.Label(self, textvariable=self.content, anchor=tk.W)

        username_label.config(font=user_font, width=30, justify=tk.LEFT)
        content_label.config(font=content_font, width=30, justify=tk.LEFT)
        content_label.config(wraplength=content_label.winfo_reqwidth())
        print(content_label.winfo_reqwidth())

        username_label.grid(row=0, column=0, sticky=tk.EW)  # arranging widgets
        content_label.grid(row=1, column=0, sticky=tk.EW)

    def set_contents(self, username, content):
        self.username.set(username)
        # content = helper.fit_content(content, 23)  # fitting content to chat box by adding '\n'
        self.content.set(content)


if __name__ == '__main__':
    root = tk.Tk()
    widget = Chat(root)
    widget.pack(expand=tk.YES, fill=tk.BOTH)
    message = 'The len() Python method returns the length of a list, string, dictionary, or any other iterable data format in Python. The len() method takes one argument: an iterable object. ... The Python len() method is a built-in function that can be used to calculate the length of any iterable object.'
    widget.set_contents('Dheenadhayalan', message)
    root.resizable(False, True)
    root.mainloop()
