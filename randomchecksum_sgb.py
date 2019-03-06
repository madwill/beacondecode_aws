from decodefunctions import getFiveCharChecksum
from random import randint

if __name__ == "__main__":

    hexchars='ABCDEF0123456789'

    randhexdic={}
    checksumdic={}
    randchar=3
    testpersample=0
    limittest=1000000
    writefile= open('sgbhexcollision.txt',"w")
    infile=open('test23uin.csv',"r")



    j=0
    collisions=0
    while(1):
        for lines in range(100000): #infile:

            realhex=infile.readline().strip()

            if len(realhex)==23 and j<limittest:
                j+=1


                realchecksum = getFiveCharChecksum(realhex)
                randomhex = []
                collision = []
                i=0
                while i < testpersample:

                    randposlist=[]

                    while len(randposlist) < randchar :
                        randpos = randint(0, 22)
                        if randpos not in randposlist:
                            randposlist.append(randpos)

                    newhex=realhex
                    for randpos2 in randposlist:
                        hexchar = hexrandom = realhex[randpos2]

                        while hexchar==hexrandom:
                            hexrandom = hexchars[(randint(0,15))]


                        if randpos2 == 0:
                            newhex = hexrandom + newhex[1:]
                        elif randpos2 == 22:
                            newhex = newhex[:-1] + hexrandom
                        else:
                            newhex = newhex[0:randpos2] + hexrandom + newhex[randpos2+1:]
                        #print(randpos)

                    randomhex.append(newhex)

                    if realchecksum ==getFiveCharChecksum(newhex) and realhex!=newhex:
                        collision.append((newhex,realhex))
                        writefile.write(':'.join(( '\n\nActual    ',    realhex, realchecksum,   '\nCollision ', newhex , getFiveCharChecksum(newhex)        )))
                        collisions+=1
                        print( newhex,getFiveCharChecksum(newhex),realhex,realchecksum)
                    i += 1
                    #print(getFiveCharChecksum(newhex))

                    #print(realhex,len(realhex))
                    #checksumdic[checksum] = hex
                for posno,char in enumerate(realhex[:-1]):
                    newhex = realhex[0:posno] + realhex[posno:posno+2][::-1] + realhex[posno+2:]

                    if realchecksum == getFiveCharChecksum(newhex) and realhex!=newhex:
                        collision.append((newhex,realhex))
                        writefile.write(':'.join(( '\n\nActual    ',    realhex, realchecksum,   '\nCollision ', newhex , getFiveCharChecksum(newhex)        )))
                        collisions+=1
                        print( newhex,getFiveCharChecksum(newhex),realhex,realchecksum)

        user_input = raw_input('Tested {} unique ids. Type STOP to quit, otherwise press the Enter/Return key '.format(j) )
        if user_input == 'STOP' or j==limittest:
            break



    #print(i)
    #print(len(checksumdic),i,(i-len(checksumdic))/float(i))
    print(j)
    writefile.write('\n\nUnique SGB tested: '+str(j)+ '  Collisions: '+ str(collisions)+'    Randomize Char : '+str(randchar)+'     Test per sample: ' + str(testpersample))
    infile.close()
    writefile.close()
    '''
    for i in range(10):
        randomhex = ''
        for d in range(15):
            randomhex=randomhex+hexchars[(randint(0,16))]
        #checksumdic[str(zlib.crc32(randomhex))]=randomhex
        checksumdic[str(getFiveCharChecksum(randomhex))] = randomhex
    print(len(checksumdic))
    '''