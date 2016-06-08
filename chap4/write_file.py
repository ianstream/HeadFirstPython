import nester
import pickle

def write_files(file_name='sketch.txt'):
    print("*** print_file ***")

    """
    read file sketch.txt
    and collect two list for man, other's spoken line
    """

    man = []
    other = []

    try:
        with open(file_name) as data:
            for each_line in data:
                try:
                    (role, line_spoken) = each_line.split(':', 1)
                    line_spoken = line_spoken.strip()

                    if role == 'Man':
                        man.append(line_spoken)
                    elif role == 'Other Man':
                        other.append(line_spoken)

                    print(role, end='')
                    print(' said: ', end='')
                    print(line_spoken, end='')
                except ValueError:
                    pass

            data.close()

    except IOError:
        print("The data file is mission")

    print("\n\n****************************************")
    print(man)
    print("\n")
    print(other)

    """
    open files to write man, other's list
    write lists
    close files using 'with'
    """
    try:
        with open('man_data.txt', 'wb') as man_file, \
             open('other_data.txt', 'wb') as other_file:
            pickle.dump(man, man_file)
            pickle.dump(other, other_file)

    except IOError:
        print('File Error !!!')

    except pickle.PickleError as perr:
        print('Pickel Error: ', str(perr))
