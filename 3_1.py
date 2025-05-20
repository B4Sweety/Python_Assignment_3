def AdditionList(iData):

    iSum = 0

    for value in iData:
        iSum = iSum + value
    return iSum    


def main():
    print("Enter elemnts : ")
    iElemnt = int(input())

    iList = list()
    print("Enter the values : ")

    for i in range(iElemnt):
        iData.append(int(input()))

    if (iElemnt == 0):
        print("List is empty")
        return     

    iRet = AdditionList(iList)

    print("Addition is : ", iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>python 3_1.py
Enter elemnts :
6
Enter the values :
13
5
45
7
4
56
Addition is :  130

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>

'''