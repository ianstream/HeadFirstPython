
def print_list():

    try:
        with open('james.txt') as james:
            data = james.readline()
        james_list = data.strip().split(',')

        with open('julie.txt') as julie:
            data = julie.readline()
        julie_list = data.strip().split(',')

        with open('mikey.txt') as mikey:
            data = mikey.readline()
        mikey_list = data.strip().split(',')

        with open('sarah.txt') as sarah:
            data = sarah.readline()
        sarah_list = data.strip().split(',')

        clean_james = []
        clean_julie = []
        clean_mikey = []
        clean_sarah = []

        for each_list in james_list:
            clean_james.append(sanitize(each_list))

        for each_list in julie_list:
            clean_julie.append(sanitize(each_list))

        for each_list in mikey_list:
            clean_mikey.append(sanitize(each_list))

        for each_list in sarah_list:
            clean_sarah.append(sanitize(each_list))

        print('james list : ', sorted(clean_james))
        print('julie list : ', sorted(clean_julie))
        print('mikey list : ', sorted(clean_mikey))
        print('sarah list : ', sorted(clean_sarah))

        james.close()
        julie.close()
        mikey.close()
        sarah.close()
    except IOError:
        print("The data file is mission")

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs