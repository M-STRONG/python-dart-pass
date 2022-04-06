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

   

evenodd(8)
