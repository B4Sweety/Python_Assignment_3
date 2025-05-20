def MinInList(iData):

    iMin = 0

    iMin = iData[0]    

    for value in iData:
        if(value < iMin):
            iMin = value

    return iMin


def main():
    print("Enter elemnts : ")
    iElemnt = int(input())

    iList = list()
    print("Enter the values : ")

    for i in range(iElemnt):
        iList.append(int(input()))

    if (iElemnt == 0):
        print("List is empty")
        return    

    iRet = MinInList(iList)

    print("Minimum is : ", iRet)

if __name__ == "__main__":
    main()


'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>python 3_3.py
Enter elemnts :
4
Enter the values :
13
5
45
7
Minimum is :  5

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>

'''