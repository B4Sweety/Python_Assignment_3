def FrequencyInList(iData, iNo):
    iCnt = 0

    for value in iData:
        if(value == iNo):
            iCnt = iCnt + 1

    return iCnt


def main():
    print("Enter elemnts : ")
    iElemnts = int(input())

    iList = list()
    print("Enter the values : ")

    for i in range(iElemnts):
        iList.append(int(input()))

    if (iElemnts == 0):
        print("List is empty")
        return

    print("Enter element to search : ")
    iNumber = int(input())

    iRet = FrequencyInList(iList, iNumber)

    print("Frequency is : ", iRet)

if __name__ == "__main__":
    main()


'''


C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>python 3_4.py
Enter elemnts :
11
Enter the values :
13
5
45
7
4
56
5
34
2
5
65
Enter element to search :
5
Frequency is :  3

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_3>

'''
