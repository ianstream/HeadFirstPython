def print_file():
    print("*** print_file ***")

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

