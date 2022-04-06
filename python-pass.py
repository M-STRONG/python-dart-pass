def evenodd():

   num = input('Enter number range: ')

   while not 0 < int(num) <= 10:

       num = input('Number must be greater than 0 &less than 10: ')

   nums = []

   for n in range(int(num)):

        x = int(input('Number: '))

        nums.append(x)

   for x in nums:

        if x%2==0 :

            print(x, 'even')

        else:

            print(x, 'odd')

evenodd()
