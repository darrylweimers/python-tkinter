
def read_to_string(path):
    try:
        file_read = open(path, 'r+')
        string = file_read.read()
        file_read.close()
        return string
    except Exception as exception:
        print(exception)

    return ''

def read_to_array(path):
    try:
        file_read = open(path, 'r+')
        lines = file_read.readlines()
        file_read.close()
        return lines
    except Exception as exception:
        print(exception)

    return []


def write(path, lines):
    try:
        file_write = open(path, 'w+')
        file_write.writelines(lines)
        file_write.close()
    except Exception as exception:
        print(exception)
