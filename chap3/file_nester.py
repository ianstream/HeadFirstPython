
data = None

def file_open():
    data = open('txt/sketch.txt')

def print_file():
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        else:
            print(each_line)

def file_close():
    data.close()