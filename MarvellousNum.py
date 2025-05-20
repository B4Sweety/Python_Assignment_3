def ChkPrime(iNo):

    if (iNo < 2) :
        return False
    for iCnt in range (2,iNo):
        if ((iNo % iCnt) == 0) :
            return False
    return True