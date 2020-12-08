#bll
def calc(x,y,choice):
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(x+y)

        elif choice == '2':
            print(x-y)

        elif choice == '3':
            print(x*y)

        elif choice == '4':
            print(x/y)
choice = input("Enter choice(1/2/3/4): ")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
calc(x,y,choice)


    
    
           




