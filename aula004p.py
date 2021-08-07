#Aligned repetition structures (multiplication table)
#while + for
multi_table = 1
while (multi_table <= 10):
    print('MULTIPLICATION TABLE OF:{}' .format(multi_table))
    for i in range(1, 11, 1):
        print('{} x {} = {}' .format(multi_table, i, multi_table * i))
    multi_table += 1
