import random

r = random.randint(1,50)

while(True):
    guess = int(input())
    if( guess > r):
        print("wrong guess , guess a smaller number")
    elif( guess < r ):
        print("wrong guess , guess a greater number")
    elif( guess = r):
        print("yahoo! congratulation you made it")
        break;
