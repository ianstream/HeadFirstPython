import nester

test_data1 = ['test1', 'test2', 'test3', 'test4', 'test5',]

print('Test 1 of test_data1')
nester.print_lol(test_data1, False, 0)

print('\nTest 2 of test_data1')
nester.print_lol(test_data1, True)


test_data2 = ['test1', 'test2', 'test3', 'test4', 'test5',
              ['inner list1', 'inner list2', 'inner list3', 'inner list4', 'inner list5'],
            ]

print('\nTest 1 of test_data2')
nester.print_lol(test_data2, False, 0)

print('\nTest 2 of test_data2')
nester.print_lol(test_data2, True, 1)


import write_file

#exception test
write_file.write_files('error.txt')


write_file.write_files()

