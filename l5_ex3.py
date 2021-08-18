tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]


def odd_nums():
    for num in range(0, len(tutors)):
        if len(tutors) > len(klasses) and num >= len(klasses):
            yield (tutors[num], 'None')
        else:
            yield (tutors[num], klasses[num])


cort = odd_nums()
print(*cort, sep = '\n')
print('\n', type(cort))