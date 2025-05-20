def MaxInList(iData):

    iMax = 0

    iMax = iData[0]    

    for value in iData:
        if(value > iMax):
            iMax = value

    return iMax


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

    iRet = MaxInList(iList)

    print("Maximum is : ", iRet)

if __name__ == "__main__":
    main()


'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>python 3_2.py
Enter elemnts :
7
Enter the values :
13
5
45
7
4
56
1
Maximum is :  56

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>

'''