
def print_list():

    try:
        james_list = get_coach_data('james.txt')
        julie_list = get_coach_data('julie.txt')
        mikey_list = get_coach_data('mikey.txt')
        sarah_list = get_coach_data('sarah.txt')

        print('james list : ', sorted(set([sanitize(each_list) for each_list in james_list]))[0:3])
        print('julie list : ', sorted(set([sanitize(each_list) for each_list in julie_list]))[0:3])
        print('mikey list : ', sorted(set([sanitize(each_list) for each_list in mikey_list]))[0:3])
        print('sarah list : ', sorted(set([sanitize(each_list) for each_list in sarah_list]))[0:3])

    except IOError:
        print("The data file is mission")

def get_coach_data(filename):
    try:
        with open(filename) as datas:
            data = datas.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File Error!!! ' + str(ioerr))
        return None

def sanitize(time_string):
    """
    get a string and retrun formated string(ex 5.43)
    :param time_string: string
    :return: formatted string
    """
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs