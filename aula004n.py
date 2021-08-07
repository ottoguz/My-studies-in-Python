#Aligned repetition structures (multiplication table)
#using 2-while
multi_table = 1
while (multi_table <= 10):
    print('MULTIPLICATION TABLE OF {}' .format(multi_table))
    i = 1
    while (i <= 10):
        print('{} x {} = {}' .format(multi_table, i, multi_table * i))
        i += 1
    multi_table += 1


