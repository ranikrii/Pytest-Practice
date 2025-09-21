#Parameterized eg
def Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(0.5*n)+1):
        if n%i == 0:
            return False
    return True