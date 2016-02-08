def write_files():
    print("*** print_file ***")

    """
    read file sketch.txt
    and collect two list for man, other's spoken line
    """

    man = []
    other = []

    try:
        data = open('sketch.txt')

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
    close files
    """
    try:
        man_file = open('man_data.txt', 'w')
        other_file = open('other_data.txt', 'w')

        print(man, file=man_file)
        print(other, file=other_file)

    except IOError:
        print('File Error !!!')

    finally:
        man_file.close()
        other_file.close()
