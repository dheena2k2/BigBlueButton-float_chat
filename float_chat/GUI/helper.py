def fit_content(text, length):
    """
    This method adds '\n' at appropriate places in such a way that
    each line will not exceed the given maximum length
    :param text: content to which '\n' is added
    :param length: maximum length of a single line
    :return: content to which '\n' is added
    """
    if len(text) <= length:  # ignore if text length is less
        return text
    new_text = ''
    fill = 0  # filled spaces in single line
    last_space = -1  # last encountered space
    for i in range(len(text)):
        if fill == length:  # new line if line is filled
            if last_space >= 0:  # replace last space with new line
                new_text = new_text[: last_space] + '\n' + new_text[last_space+1:]
            else:
                new_text += '\n'
            fill = 0
        new_text += text[i]
        fill += 1
        if new_text[-1] == ' ':  # update last space
            last_space = len(new_text) - 1

    return new_text
