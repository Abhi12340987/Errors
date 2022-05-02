print(1)
int(9)
int(9)
print(2)
print(3)

#exception errrors
a =1 
b = "2"
print(a+ float(b))
print(int(2.5))

def divide(a,b):
    try:
        return a/b
    except:
        b = 0
        return "zero division is forbbiden"
print(divide(1,0))