import MarvellousNum
def ListPrime(iData):
    iSum = 0

    for value in iData:
        if(MarvellousNum.ChkPrime(value)):
            iSum = iSum + value

    return iSum


def main():
    print("Enter elemnts : ")
    iElemnts = int(input())

    iList = list()
    print("Enter the values : ")

    for i in range(iElemnts):
        iList.append(int(input()))


    iRet = ListPrime(iList)

    print("Addition of prime number is : ", iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>python 3_5.py
Enter elemnts :
11
Enter the values :
13
5
45
7
4
56
10
34
2
5
8
Addition of prime number is :  32

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>

'''
