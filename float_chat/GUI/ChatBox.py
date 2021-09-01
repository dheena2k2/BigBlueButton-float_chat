import tkinter as tk


class Chat(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.username = tk.StringVar()  # label holding username
        self.content = tk.StringVar()  # label holding content
        self.create_widgets()

    def create_widgets(self):
        user_font = ('calibri', 11, 'bold')
        content_font = ('calibri', 11, 'normal')
        username_label = tk.Label(self, textvariable=self.username, anchor=tk.W)  # create label widgets
        content_label = tk.Label(self, textvariable=self.content, anchor=tk.W)

        username_label.config(font=user_font, width=30)
        content_label.config(font=content_font, width=30)

        username_label.grid(row=0, column=0, sticky=tk.EW)
        content_label.grid(row=1, column=0, sticky=tk.EW)

    def set_contents(self, username, content):
        self.username.set(username)
        self.content.set(content)


if __name__ == '__main__':
    root = tk.Tk()
    widget = Chat(root)
    widget.pack(expand=tk.YES, fill=tk.BOTH)
    message = 'M' * 23 + '\nHello'
    widget.set_contents('Dheenadhayalan', message)
    root.resizable(False, True)
    root.mainloop()
