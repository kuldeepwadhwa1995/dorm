import random
#bll

def checkwinner(number,n):
    if number==n:
        print("winner")
    else:
        print("losser")
#pl
def inputf():
    number=random.randrange(0,9)
    n=int(input("enter the number you want to compare"))
    print(n)
    checkwinner(number,n)

inputf()


    