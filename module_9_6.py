def all_variants(text: str):
    _substring = ""
    index = 0
    delta = 1
    while _substring != text:
        index += 1
        _substring = text[index - delta: index]
        if index == len(text):
            delta += 1
            index = delta - 1
        yield _substring


a = all_variants("abcd")
for i in a:
    print(i)
