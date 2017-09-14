

def convert_a_string_to_raw_string(string=''):
    raw_string = "%r" % string
    return raw_string

def test_convert_a_string_to_raw_string():
    string = "Convert\ta string to \n raw \tstring"
    print("Raw string:")
    print(convert_a_string_to_raw_string(string))
    print()
    print("String:")
    print(string)
