def Chkprime(Number):

    if Number <= 1:
        return False
    
    for i in range(2,int(Number** 0.5)+1):
        if Number % 1 == 0:
            return False
        
    return False