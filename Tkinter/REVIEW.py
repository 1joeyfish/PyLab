from random import randint 

#HOUSES 
#DOG=1
#CAT=2
#LION=3

#START PLAYING

SCORE=0

for a in range(5):
    HOUSE1=randint(1,3)
    HOUSE2=randint(1,3)
    HOUSE3=randint(1,3)

    HOUSE_CHOSE=int(input('PLEASE IMPUT THE HOUSE YOU WANT TO GO IN 1,2,3:'))
    if HOUSE_CHOSE>=1 and HOUSE_CHOSE<=3:
        if HOUSE_CHOSE==1:
            if HOUSE1==1:
                print('I love dogs(YOU FOUND A DOG!)')
                SCORE=SCORE+1
            elif HOUSE1==2:
                print('I always wanted a cat(YOU FOUND A CAT!)')
                SCORE=SCORE+1                                                
            elif HOUSE1==3:
                print('RUN AWAY!(YOU FOUND A LION!)')
        elif HOUSE_CHOSE==2:
            if HOUSE2==1:
                print('I love dogs(YOU FOUND A DOG!)')
                SCORE=SCORE+1
            elif HOUSE2==2:
                print('I always wanted a cat(YOU FOUND A CAT!)')
                SCORE=SCORE+1
            elif HOUSE2==3:
                print('RUN AWAY!(YOU FOUND A LION!)')
        elif HOUSE_CHOSE==3:
            if HOUSE3==1:
                print('I love dogs(YOU FOUND A DOG!)')
                SCORE=SCORE+1
            elif HOUSE3==2:
                print('I always wanted a cat(YOU FOUND A CAT!)')
                SCORE=SCORE+1
            elif HOUSE3==3:
                print('RUN AWAY!(YOU FOUND A LION!)')



    else:
        print(HOUSE_CHOSE,'is not a choice we don\'t trust you.Please RESTART')
        exit()

if SCORE>2:
    print('you win!')
else:
    print('you loose!')
