def read_from_file(open_file_path):
    try:
        file_read = open(open_file_path, 'r+')
        lines = file_read.readlines()
        file_read.close()
        return lines
    except Exception as exception:
        print(exception)

    return []


def write_to_file(save_file_path, lines):
    try:
        file_write = open(save_file_path, 'w+')
        file_write.writelines(lines)
        file_write.close()
    except Exception as exception:
        print(exception)
