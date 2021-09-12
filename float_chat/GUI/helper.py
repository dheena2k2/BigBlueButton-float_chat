from tkinter.messagebox import askyesno


def quit_popup():
    """
    Quit action confirmation
    :return: Boolean representing confirmation
    """
    return askyesno(title='Confirm exit', message='Are you sure you want to exit?')
