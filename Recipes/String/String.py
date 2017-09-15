
# Convert a string to a raw string
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

    
# Remove first/all occurences of string 
def remove_all_occurrence_of(string='', substring=''):
    number_of_occurrence = string.count(substring)
    while number_of_occurrence:
        string = remove_first_occurrence_of(string, substring)
        number_of_occurrence -= 1
    return string


def remove_first_occurrence_of(string='', substring=''):
    index_substring = string.find(substring)
    part1 = string[0:index_substring]
    part2 = string[index_substring + len(substring): len(string)]
    return part1 + part2

def test_remove_all_occurrence_of():
    string = r"Types.h\n\n\nKeepThisPart\n\n\nKeep-this-part"
    substring = r'\n\n\n'
    print("%-35s\t%-30s" % ("String:", string))
    print("%-35s\t%-30s" % ("Substring:", substring))
    print("%-35s\t%-30s" % ("String after computation:",remove_all_occurrence_of(string, substring)))
    
# Replace first/all occurences of string    
def replace_first_occurrence_of(string='', substring='', replacement_substring=''):
    index_substring = string.find(substring)
    part1 = string[0:index_substring]
    part2 = string[index_substring + len(substring): len(string)]
    return part1 + replacement_substring + part2

def replace_all_occurrence_of(string='', substring='', replacement_substring=''):
    number_of_occurrence = string.count(substring)
    while number_of_occurrence:
        string = replace_first_occurrence_of(string, substring, replacement_substring)
        number_of_occurrence -= 1
    return string

def test_replace_first_occurrence_of():
    string = r"Types.h\n\n\nKeepThisPart\n\n\nKeep-this-part"
    substring = r'\n\n\n'
    replacement_substring = ' '
    print("%-35s\t%-30s" % ("String:", string))
    print("%-35s\t%-30s" % ("Substring:", substring))
    print("%-35s\t%-30s" % ("String after computation:", replace_first_occurrence_of(string, substring, replacement_substring)))


