first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_res = [(len(str1) - len(str2)) for str1, str2 in zip(first, second) if len(str1) != len(str2)]

second_res = [(len(first[i])) == (len(second[i])) for i in range(len(first))]

print(list(first_res))
print(list(second_res))
