def resta(*nums:float)->float:         #Definimos función de resta
    res = nums[0]
    for valor in nums:
        res -= valor
    return res
def suma(*nums:float)->float:          #Definimos función de suma
    res= 0
    for valor in nums:
        res += valor
    return res

def mult(*nums:float)->float:          #Definimos función de multiplicación
    res= 1
    for valor in nums:
        res *= valor
    return res

def div(n1:float, n2:float)->float:          #Definimos función de división
    res = n1/n2
    sobra = n1 % n2
    
    return res, sobra



