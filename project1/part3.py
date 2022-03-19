from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends.openssl.backend import backend
import os
import binascii
def weakCollision():
    str1 = "abf"
    digest = hashes.Hash(hashes.SHA256(), backend)
    digest.update(str1.encode("utf-8"))
    hash1 = digest.finalize()
    avg = 0
    for x in range(5):
        
        total = 0
        count = 0
        while True:
            #create a string of 3bytes
            randstr = os.urandom(3)
            #create the hash using the random string
            randdigest = hashes.Hash(hashes.SHA256(),backend)
            randdigest.update(randstr)
            hash2 = randdigest.finalize()
            count +=1
            #if the two hashes match then break the loop and add the count to total
            if hash1[0:3] == hash2[0:3]:
                #print(hash1[0:3], hash2[0:3])
                total += count
                #prints the trials it took to break weak collison
                #print( "trials :", count)
                break
    avg = total/5
    print("Average amount of trials for weak collision: ", avg)
    #avg for 5 trials 20,233,913.2


def strong_collision():
    total = 0
    for x in range(100):
        dosomething = True
        count = 0
        array = []
        while dosomething == True:
            str1 = os.urandom(3)
            digest = hashes.Hash(hashes.SHA256(),backend)
            digest.update(str1)
            hash1 = digest.finalize()
            #append the 3 bytes to the array
            array.append(hash1[:3])
            #if array size is not 0 check if the hash already exists in it
            if len(array) > 1:
                for i in range(len(array)-1):
                    if array[i] == hash1[:3]:
                        #we found a match so break the loop
                        dosomething = False
                        break
             
            count += 1
        total += count
        #print("total" , total)
        #print("trials" , count)
    print("Average amount of trials for strong collision: ", total/100)
    



def main():
    weakCollision()
    strong_collision()

if __name__ == "__main__":
    main()
