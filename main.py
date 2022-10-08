try:
    num = int(input('Enter number->'))
    start = 1
    sum = 1

    while sum <= num:
        sum *= start
        start += 1
    print(f'{sum}')
except Exception as ex:
    print(f'Error information: {ex}')




