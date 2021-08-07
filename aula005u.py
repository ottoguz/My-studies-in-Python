def counter(end, start=0, pace=1):
    for i in range(start, end, pace):
        print('{}' .format(i), end=' ')
    print('\n')

counter(20, 10, 2)
counter(12)