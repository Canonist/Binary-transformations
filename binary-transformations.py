#setup imports
import time

#begin
#binary-transformations created by Canonist for github



#define "subroutines"
#calculate 2 to the power of p to figure out ASCII value for bit
def test(p):
    r = 2**p
    return r

#run through bits 1 til y
def run(y):
    x = 0
    while x < y:
        test(x)
        x += 1

def calbit(bi):
    count = len(bi)
    start = count-1
    adder = 0
    d = 0
    #print("count: ", count)
    #print("bi[0], bi[1], bi[2]: ",bi[0],bi[1],bi[2])
    while count > 0:
        current = int(bi[start])
        if current == 1:
            result = test(d)
            adder += result
            #print("adder: ",adder)
        #print("current: ",current)
        d += 1
        count -= 1
        start -= 1
    return adder

def bascii():
    word = str(input("Type in the binary to transform to ASCII: "))
    print(calbit(word))

'''
#test functionality
print("Printing bit 0 as 2 to the power of 0 aka 1")
test(0)

print("\n \n \n")

#run through 8-bits
print("Running through bits")
time.sleep(1)
print("Running through bits.")
time.sleep(1)
print("Running through bits..")
time.sleep(1)
print("Running through bits...")
time.sleep(1)

print("running bits 1-8")
run(8)
'''
#print("binary example 11011 aka 27 aka ESC key in ASCII")

#bascii()

