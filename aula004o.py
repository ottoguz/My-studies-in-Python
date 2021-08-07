#Aligned repetition structures (multiplication table)
#using 2-for
for multi_table in range(1, 11, 1):
    print('MULTIPLICATION TABLE OF: {}' .format(multi_table))
    for i in range(1, 11, 1):
        print('{} x {} = {}' .format(multi_table, i, multi_table * i))

