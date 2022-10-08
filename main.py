try:
    num = int(input('Enter number->'))
    start = 1
    sum = 1

    for i in range(start,num):
        sum *= start
        start += 1
    print(f'{sum}')
except Exception as ex:
    print(f'Error information: {ex}')




