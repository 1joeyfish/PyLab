from random import randint

mylist=[]
#github test
def find_big_num():
    global mylist
    bignum=mylist[0]
    for i in range(len(mylist)):
        if mylist[i]>bignum:
            bignum=mylist[i]
    print('The biggest number is '+str(bignum))

def find_sml_num():
    global mylist
    smlnum=mylist[0]
    for i in range(len(mylist)):
        if mylist[i]<smlnum:
            smlnum=mylist[i]
    print('The smallest number is '+str(smlnum))

def main():
    global mylist
    for i in range(1000):
        mylist.append(randint(0,100000))
    mylist.sort()
    print(mylist)
    find_big_num()
    find_sml_num()
    
if __name__=='__main__':
    main()
