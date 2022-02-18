for num in range(1, 101):
    if 2 <= num % 10 <= 4 and not 12 <= num % 100 <= 14:
        print(f'{num} процента')
    elif 1 == num % 10 and not 11 <= num % 100 <= 20:
        print(f'{num} процент')
    else:
        print(f'{num} процентов')


