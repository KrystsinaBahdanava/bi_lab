def find_message(text):
    return "".join([c for c in text if c.isupper()])


if __name__ == '__main__':
    assert find_message(u"How are you? Eh, ok.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
