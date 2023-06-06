def int_to_bin(n,k):
    number = bin(n)[2:] 
    number = number.zfill(k)  
    return str(number)

registers = {}
ProgCounter = 0
for i in range(7):
    temp = str(int_to_bin(i,3))
    registers[temp] = 0
registers["FLAGS"] = [0,0]


f = open("binary.txt","r")             
data_list = f.readlines()
f.close()


for counter in range(len(data_list)):
    data_list[counter]=data_list[counter].rstrip()
    data_list[counter] = data_list[counter].split()


no_of_lines = len(data_list)

data = []
for i in range(no_of_lines):
    data.append(data_list[i][0])

while(True):
    line = data[ProgCounter]
    temp = []
    temp.append(int_to_bin(ProgCounter,7))
    opCode = line[:5:]
    if opCode == "11010":
        print(temp[0],end = " ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        break
    elif opCode == "00000": #Add
        r1 = line[7:10:]
        r2 = line[10:13]
        r3 = line[13::]
        temp_sum = registers[r2] + registers[r3]
        if (temp_sum > 2**16 - 1 or temp_sum < 0):
            registers[r1] = 0
            registers["FLAGS"][0] = 4
            registers["FLAGS"][1] = ProgCounter
        else:
            registers[r1] = temp_sum
        print(temp[0],end = " ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["FLAGS"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["FLAGS"][1] != ProgCounter:
            registers["FLAGS"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00001": # Sub
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        temp_diff = registers[r2] - registers[r3]
        if temp_diff > 2**16 - 1 or temp_diff < 0:
            registers[r1] = 0
            registers["FLAGS"][0] = 4
            registers["FLAGS"][1] = ProgCounter
        else:
            registers[r1] = temp_diff
        print(temp[0], end=" ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["FLAGS"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["FLAGS"][1] != ProgCounter:
            registers["FLAGS"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00110": #Mult
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        temp_prod = registers[r2] * registers[r3]
        if temp_prod > 2**16 - 1 or temp_prod < 0:
            registers[r1] = 0
            registers["FLAGS"][0] = 4
            registers["FLAGS"][1] = ProgCounter
        else:
            registers[r1] = temp_prod
        print(temp[0], end=" ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["FLAGS"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["FLAGS"][1] != ProgCounter:
            registers["FLAGS"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01010": #Bitwise XOR 
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        a = int_to_bin(registers[r2],16)
        b = int_to_bin(registers[r3],16) 
        c = []
        for i in range(16):
            c.append(0)
        for i in range(16):
            c[i] = str(int(a[0]) ^ int(b[0]))
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0], end=" ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["FLAGS"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["FLAGS"][1] != ProgCounter:
            registers["FLAGS"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01011": #Bitwise OR
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        a = int_to_bin(registers[r2],16)
        b = int_to_bin(registers[r3],16) 
        c = []
        for i in range(16):
            c.append(0)
        for i in range(16):
            c[i] = str(int(a[0]) | int(b[0]))
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0], end=" ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["FLAGS"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["FLAGS"][1] != ProgCounter:
            registers["FLAGS"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01011": #Bitwise AND
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        a = int_to_bin(registers[r2],16)
        b = int_to_bin(registers[r3],16) 
        c = []
        for i in range(16):
            c.append(0)
        for i in range(16):
            c[i] = str(int(a[0]) & int(b[0]))
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0], end=" ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["FLAGS"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["FLAGS"][1] != ProgCounter:
            registers["FLAGS"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
