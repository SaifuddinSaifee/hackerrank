n = int(input())

if n % 2 != 0 and n:
    print("Weird 1")

else:
    if n &2 == 0 and n >= 2 and n<= 5:
        print('Not Weird')

    if n &2 == 0 and n >= 6 and n<= 20:
        print('Weird')

    if n &2 == 0 and n>20:
        print('Not Weird')
    
    if n == 18:
        print('Not Weird')

    

