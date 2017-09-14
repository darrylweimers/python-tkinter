
# CONVERT A STRING TO A RAW STRING

def convert_a_string_to_raw_string(string=''):
    raw_string = "%r" % string
    return raw_string

def test_convert_a_string_to_raw_string_1():
    string = "Convert\ta string to \n raw \tstring"
    print("Raw string:")
    print(convert_a_string_to_raw_string(string), '\n')
    print("String:")
    print(string)

def test_convert_a_string_to_raw_string_2():
    string = "\n\n\n"
    raw_string = convert_a_string_to_raw_string(string)
    print(raw_string.count(r'\n'))
