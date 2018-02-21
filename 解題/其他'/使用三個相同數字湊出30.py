def getValue(a,op,b):
    return {
            '+':a+b,
            '-':a-b,
            '*':a*b,
            '/':a/b,
            '^':a**b
        }.get(op)
record = []
opera =['+','-','*','/','^']
def dp(value,rec,cut,count):
    if value == 30:
        record.append(rec)
    elif count < 3:
        for o in opera:
            cutRec = rec[:]
            cutRec.extend([o,cut])
            dp(getValue(value,o,cut),cutRec,cut,count+1)
for i in range(1,10):
    dp(i,[i],i,1)
for result in record:
    for value in result:
        print(value,end='')
    print()

''' result:
3^3+3
5*5+5
6*6-6
'''
