def evenodd(num):

    num = input('Enter X value: ')

    nums = []

    for n in range(int(num)):

        x = int(input('Number: '))

        nums.append(x)

    for x in nums:

        if 0 < x <= 10:

            if x%2==0 :

                print(x, 'even')

            else:

                print(x, 'odd')

        else:

            print(x, 'out of range')

            break

    

    '''if 0< num <= 10:

        for i in range(num):

            num=int(input('Enter X value:'))

            if num%2==0 :

                print('even')

            else:

                print('odd')

    else:

     1  print('agine')'''

evenodd(8)
