
import math
import mmh3
import time
from bitarray import bitarray


passArr = []
passCount = 0
numhashes = 3
file = open("dictionary.txt", "r")
while file:
    password  = file.readline().strip()
    passArr.append(password)
    passCount += 1
    if password == "":
        break
file.close() 

inputArr = []
file = open("sample_input.txt", "r")
passcount2 = file.readline().strip()
starttime = time.time()
for i in range(int(passcount2)):
    password  = file.readline().strip()
    inputArr.append(password)
    if password == "":
        break
    
file.close() 

bitArraySize = -(passCount * math.log(.1))/(math.log(2)**2)
bitArraySize = int(bitArraySize)
#print(bitArraySize)
bitArray = [False] * bitArraySize
def addToFilter(password):
    hashes = []
    for i in range(numhashes):
        hashDigest = mmh3.hash(password,i)  % bitArraySize
        hashes.append(hashDigest)
        bitArray[int(hashDigest)] = True
def isPresent(password):
     for i in range(numhashes):
            hashDigest = mmh3.hash(password, i) % bitArraySize
            if bitArray[int(hashDigest)] == False:
                return False
            return True

for i in passArr:
    addToFilter(i)
    
f = open("output3.txt", "w")
passcount2 = passcount2 + "\n"
f.write(passcount2)
for password in inputArr:
    if isPresent(password) == True:
        line = password + " maybe\n"
        f.write(line)
    else:
        line = password + " no\n"
        f.write(line)
endtime = time.time()
#print("time5", round(endtime-starttime,16))
f.close()
#print(bitArraySize)

numhashes = 5
bitArray = [False] * bitArraySize
for i in passArr:
    addToFilter(i)

f = open("output5.txt", "w")
f.write(passcount2)
for password in inputArr:
    if isPresent(password) == True:
        line = password + " maybe\n"
        f.write(line)
    else:
        line = password + " no\n"
        f.write(line)
f.close()