import coach

coach.print_dict()

a = coach.AthleteList(a_name='ian kim', a_dob='2016-02-15', a_times=['2.15', '2.45', '3.01', '2.05'])

print('*** print test ***')
print(a.name + ", " + a.dob + ", " + str(a) + ", " + str(a.top3()))

print('*** append test ***')
a.append('3.05')
print(a.name + ", " + a.dob + ", " + str(a) + ", " + str(a.top3()))

print('*** extend test ***')
a.extend(['3.04', '3.65'])
print(a.name + ", " + a.dob + ", " + str(a) + ", " + str(a.top3()))


vera = coach.AthleteList('Vera Vi')
vera.append('1:31')
print(vera.top3())

vera.extend(('3:35', '2:15', '1:43'))
print(vera.top3())
