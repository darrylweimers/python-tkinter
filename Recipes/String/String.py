
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

    
#remove all occurences of string 
string = r"Types.h\n\n\nKeepThisPart\n\n\nKeep-this-part"
index = string.find(r'\n\n\n')
print(string)
# for index in range(0, index):
#     print(string[index], end="")
# for index in range(index + len(r'\n\n\n') + 1, len(string)):
#     print(string[index], end="")

print(string[0:index], end='')
print(string[index + len(r'\n\n\n') + 1: len(string)], end='')


print()
print(string.count(r'\n\n\n'))




#def remove_occurence_of(string='')
