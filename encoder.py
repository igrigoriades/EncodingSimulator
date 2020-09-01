def printSignal(stream, mode):
    if (mode == 0):
        high="¯¯"
        low="__"
        pipehigh="|¯¯"
        pipelow="|__"
    if (mode == 1):
        high="¯"
        low="_"
        pipehigh="|¯"
        pipelow="|_"
    counter=0
    for bit in stream:
        if (bit == '1'):
            if(counter == 0):
                print(high, end ="")
            else:
                if (stream[counter-1] == bit):
                    print(high, end ="")
                else:
                    print(pipehigh, end ="")
        elif (bit == '0'):
            if (counter == 0):
                print(low, end ="")
            else:
                if (stream[counter-1] == bit):
                    print(low, end ="")
                else:
                    print(pipelow, end ="")
        counter=counter+1
    print("\n")

def printSignalTri(stream):
    high="¯¯"
    low="__"
    neutral="--"
    flag=0
    for bit in stream:
        if (flag==1):
            flag=0
            continue
        elif (bit == "-"):
            print(low, end ="")
            flag=1
        elif (bit == '1'):
            print(high, end ="")
            flag=0
        elif (bit == '0'):
            print(neutral, end ="")
            flag=0
    print("\n")

def nrzEncoder(stream):
    encoded=""
    for bit in stream:
        if (bit == '1'):
            encoded=encoded+"1"
        elif (bit == '0'):
            encoded=encoded+"0"
    return encoded

def nrziEncoder(stream):
    encoded="0"
    counter=0
    for bit in stream:
        if (bit == '1'):
            if (encoded[counter] == '0'):
                encoded=encoded+'1'
            elif (encoded[counter] == '1'):
                encoded=encoded+'0'
        elif (bit == '0'):
            if (encoded[counter] == '0'):
                encoded=encoded+'0'
            elif (encoded[counter] == '1'):
                encoded=encoded+'1'
        counter=counter+1
    return encoded

def bipolaramiEncoder(stream):
    encoded=""
    counter=0
    for bit in stream:
        if (bit == '1'):
            counter=counter+1
            if (counter % 2 == 0):
                encoded=encoded+'-1'
            else:
                encoded=encoded+'1'
        elif (bit == '0'):
            encoded=encoded+'0'
    return encoded

def pseudoternaryEncoder(stream):
    encoded=""
    counter=0
    for bit in stream:
        if (bit == '0'):
            counter=counter+1
            if (counter % 2 == 0):
                encoded=encoded+'-1'
            else:
                encoded=encoded+'1'
        elif (bit == '1'):
            encoded=encoded+'0'
    return encoded

def manchesterEncoder(stream):
    encoded=""
    for bit in stream:
        if (bit == '0'):
            encoded=encoded+'10'
        elif (bit == '1'):
            encoded=encoded+'01'
    return encoded

def diffmanchesterEncoder(stream):
    encoded=""
    for bit in stream:
        if (bit == '0'):
            encoded=encoded+'01'
        elif (bit == '1'):
            encoded=encoded+'10'
    return encoded


def checkBitstream(stream):
    for bit in bitstream:
        if (bit == '0' or bit == '1'):
            pass
        else:
            return 1
    return 0

def menu():
    print("[1] NRZ\n[2] NRZ-I\n[3] Bipolar AMI\n[4] Pseudoternary\n[5] Manchester\n[6] Diff. Manchester")
    while True:
       try:
           encoding = int(input("[+] Select an encoding method: "))
       except ValueError:
           print ("That\'s not a number!")
       else:
           if (1 <= encoding <= 6):
               break
           elif (encoding == 0):
               exit(0)
           else:
               print ("Out of range. Try again")
    return encoding

bitstream = input("[+] Please enter a bit stream: ")
while (checkBitstream(bitstream) == 1):
    bitstream = input("[+] Enter a valid bit stream: ")
while True:
    encoding=menu()

    print("**************************************************")
    print("Input bitstream: ", bitstream)
    printSignal(bitstream,0)

    #The high voltage level is assumed to be the 1 and the low voltage level is assumed to be the 0.
    if (encoding == 1):
        encoded = nrzEncoder(bitstream)
        print("Output bitstream: ", encoded,"\nEncoding: NRZ-L")
        printSignal(encoded,0)
        print("**************************************************")

    if (encoding == 2):
        encoded = nrziEncoder(bitstream)
        print("Output bitstream: ", encoded,"\nEncoding: NRZ-I")
        printSignal(encoded,0)
        print("**************************************************")

    if (encoding == 3):
        encoded = bipolaramiEncoder(bitstream)
        print("Output bitstream: ", encoded,"\nEncoding: Bipolar AMI")
        printSignalTri(encoded)
        print("**************************************************")

    if (encoding == 4):
        encoded = pseudoternaryEncoder(bitstream)
        print("Output bitstream: ", encoded,"\nPseudoternary")
        printSignalTri(encoded)
        print("**************************************************")

    #The plotting of Manchester encoders is not accurate. Mind That
    #the plot using 2x the clock.
    if (encoding == 5):
        encoded = manchesterEncoder(bitstream)
        print("Output bitstream: ", encoded,"\nManchester")
        printSignal(encoded,1)
        print("**************************************************")

    if (encoding == 6):
        encoded = diffmanchesterEncoder(bitstream)
        print("Output bitstream: ", encoded,"\nDiff. Manchester")
        printSignal(encoded,1)
        print("**************************************************")
