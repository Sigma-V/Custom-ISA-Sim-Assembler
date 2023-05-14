def add(r1,r2,r3):
    val = isa_codes["add"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def sub(r1,r2,r3):
    val = isa_codes["sub"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def mov(r1,r2,flg):
    if flg:
        val =  isa_codes["movr"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    else:
        val =  isa_codes["movi"]["opcode"]+"0"+reg_codes[r1] 
        r2 = str(bin(int(r2[1:]))).lstrip("0b")
        if (len(r2) != 7):
            for i in range (0,7-len(r2),1):
                val +="0"
        val += r2 
    return val

def ld(r1,mem_add):
    alpha = ""
    if len(mem_add) !=7:
        for i in range(7-len(mem_add)):
            alpha+="0"
    mem_add = alpha+mem_add
    val = isa_codes["ld"]["opcode"]+"0"+reg_codes[r1]+mem_add
    return val

def st(r1,mem_add):
    alpha = ""
    if len(mem_add) !=7:
        for i in range(7-len(mem_add)):
            alpha+="0"
    mem_add = alpha+mem_add
    val = isa_codes["st"]["opcode"]+"0"+reg_codes[r1]+mem_add
    return val

def rs(r1,r2):
    val = isa_codes["rs"]["opcode"]+"0"+reg_codes[r1]
    r2 = str(bin(int(r2[1:]))).lstrip("0b")
    if (len(r2) != 7):
        for i in range (0,7-len(r2),1):
            val += "0"
    val += r2

def ls(r1,r2):
    val = isa_codes["ls"]["opcode"]+"0"+reg_codes[r1]
    r2 = str(bin(int(r2[1:]))).lstrip("0b")
    if (len(r2) != 7):
        for i in range (0,7-len(r2),1):
            val += "0"
    val += r2

def mul(r1,r2,r3):
    val = isa_codes["mul"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def div(r1,r2):
    val = isa_codes["div"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    return val

def xor(r1,r2,r3):
    val = isa_codes["xor"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def or_(r1,r2,r3):
    val = isa_codes["or"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def and_(e1,e2,e3):
    val = isa_codes["and"]["opcode"]+"00"+reg_codes[e1]+reg_codes[e2]+reg_codes[e3]
    return val

def not_(r1,r2):
    val = isa_codes["not"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    return val

def cmp(r1,r2):
    val = isa_codes["cmp"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    return val

def hlt():
    val = isa_codes["hlt"]["opcode"]+"00000000000"
    return val

def jmp(r1):
    val = isa_codes["jmp"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val

def jlt(r1):
    val = isa_codes["jlt"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val

def jgt(r1):
    val = isa_codes["jgt"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val
def je(r1):
    val = isa_codes["je"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val

def validity_of_instruction(input_instruction,list_of_instructions):
    flag = True
    for instruction_name in input_instruction:
        if instruction_name not in list_of_instructions:
            flag = False
            break
    return flag

def validity_of_registers(input_register,list_of_registers):
    flag = True
    for register_name in input_register:
        if register_name not in list_of_registers:
            flag = False
            break
    return flag

def validity_of_variables(input_memory,list_of_variables):
    flag = True
    for variable in input_memory:
        if variable not in list_of_variables:
            flag = False
            break
    return flag

def correct_usage_of_halt(input_instruction):
    occurence_of_halt = input_instruction.count("hlt")
    index_of_halt = input_instruction.index("hlt")
    last_index = len(input_instruction) - 1

    if occurence_of_halt == 1 and index_of_halt == last_index:
        return True
    else:
        return False

def checking_length_of_immediate(immediate):
    if (len(immediate) == 7):
        return True
    else:
        return False

def checking_variable_declared_starting(line_when_variable_added):
    if sum(line_when_variable_added) == int(len(line_when_variable_added)*(len(line_when_variable_added) + 1)/2):
        return True
    else:
        return False


reg_codes = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}
isa_codes = {
        "add" : {"opcode" : "00000", "type" : "a"},
        "sub" : {"opcode" : "00001", "type" : "a"},
        "movi" : {"opcode" : "00010", "type" : "b"},
        "movr" : {"opcode" : "00011", "type" : "c"},
        "ld" : {"opcode" : "00100", "type" : "d"},
        "st" : {"opcode" : "00101", "type" : "d"},
        "mul" : {"opcode" : "00110", "type" : "a"},
        "div" : {"opcode" : "00111", "type" : "c"},
        "rs" : {"opcode" : "01000", "type" : "b"},
        "ls" : {"opcode" : "01001", "type" : "b"},
        "xor" : {"opcode" : "01010", "type" : "a"},
        "or" : {"opcode" : "01011", "type" : "a"},
        "and" : {"opcode" : "01100", "type" : "a"},
        "not" : {"opcode" : "01101", "type" : "c"},
        "cmp" : {"opcode" : "01110", "type" : "c"},
        "jmp" : {"opcode" : "01111", "type" : "e"},
        "jlt" : {"opcode" : "11100", "type" : "e"},
        "jgt" : {"opcode" : "11101", "type" : "e"},
        "je" : {"opcode" : "11111", "type" : "e"},
        "hlt" : {"opcode" : "11010", "type" : "f"}}

list_of_instructions = list(isa_codes.keys()) #Code to create a list which contains all the instructions 
list_of_instructions.remove("movi")          #of the isa
list_of_instructions.remove("movr")
list_of_instructions.append("mov")

list_of_registers = list(reg_codes.keys()) #Code to create a list which contains all the name of the 
list_of_registers.remove("FLAGS")         #registers



f = open("instruction.txt","r")             #reads data from the input file
data = f.readlines()
f.close()

for counter in range(len(data)):
    data[counter]=data[counter].rstrip()
    data[counter] = data[counter].split()  #ends here


list_of_variables = []                              # makes a list of the name of the variables
line_when_variable_added = []                       # and the line when they are declared
for counter in range(len(data)):
    if data[counter][0] == "var":
        list_of_variables.append(data[counter][1])
        line_when_variable_added.append(counter+1)

input_labels = []                                   # classifies the input into registers, memory locations
jump_to_labels = []                                 # , labels, instructions and immediates      
input_register = []
input_memory = []
input_instruction = []
immediates = []

for counter in range(len(data)):   
    try:                                                                      #first we just find out the labesl and the instructions 
        if data[counter][0][len(data[counter][0])-1] == ":":                   #present in the input and put them into lists
            input_labels.append(data[counter][0][0:len(data[counter][0])-1:])  #Depending on the type of instruction, we can extract 
            input_instruction.append(data[counter][1])                         #more info from a given line
            if isa_codes[data[counter][1]]["type"] == "a":
                input_register.append(data[counter][2])
                input_register.append(data[counter][3])
                input_register.append(data[counter][4])
            elif isa_codes[data[counter][1]]["type"] == "b":
                input_register.append(data[counter][2])
                immediates.append(data[counter][3][1::])
            elif isa_codes[data[counter][1]]["type"] == "c":
                input_register.append(data[counter][2])
                input_register.append(data[counter][3]) 
            elif isa_codes[data[counter][1]]["type"] == "d":
                input_register.append(data[counter][2])
                input_memory.append(data[counter][3])
            elif isa_codes[data[counter][1]]["type"] == "e":
                jump_to_labels.append(data[counter][2])
            else:
                continue

        else:
            input_instruction.append(data[counter][0])
            if isa_codes[data[counter][0]]["type"] == "a":
                input_register.append(data[counter][0])
                input_register.append(data[counter][1])
                input_register.append(data[counter][2])
            elif isa_codes[data[counter][0]]["type"] == "b":
                input_register.append(data[counter][0])
                immediates.append(data[counter][1][1::])
            elif isa_codes[data[counter][0]]["type"] == "c":
                input_register.append(data[counter][0])
                input_register.append(data[counter][1]) 
            elif isa_codes[data[counter][0]]["type"] == "d":
                input_register.append(data[counter][0])
                input_memory.append(data[counter][1])
            elif isa_codes[data[counter][0]]["type"] == "e":
                jump_to_labels.append(data[counter][1])
            else:
                continue
    except:
        continue
            
m= []
for i in range(0,127) :
    x = str(bin(i)).lstrip("0b")
    m.append(x)

label_checker = {}         
var_name = {}              
count_counter = var_count = count_empty = 0

for i in data:
    if i != "\n":
        final_list = [x for x in i.split()]
        if final_list[0][-1] == ":":
            final_list = final_list[1:]
        if final_list != []:
            if final_list[0] == "var":
                var_count += 1
        else:
            count_empty += 1
    else:
        count_empty += 1

length = len(data) - var_count -count_empty

for i in data:
    if i == "\n":
        continue
    else:
        final_list = [x for x in i.split()]
        if final_list[0] == "var" :
            var_name[final_list[1]] = m[count_counter + length]   
        if final_list[0][-1] == ":" :
            label_checker[final_list[0][0:-1]] = m[count_counter - var_count]
            final_list = final_list[1:]
        if final_list != []:
            count_counter += 1
    
for i in data:
    flag = True
    val = ""
    if i == "\n":
        flag = False
        pass
    else:
        final_list = [x for x in i.split()]
        if final_list[0] == "var":
            flag = False
            pass
        if final_list[0][-1] == ":" :
            final_list = final_list[1:]
        if final_list == []:
            flag = False
            pass
        elif final_list[0] == "add":
            val = add(final_list[1],final_list[2],final_list[3])
        elif final_list[0] == "sub":
            val = sub(final_list[1],final_list[2],final_list[3])
        elif final_list[0] == "mov":
            t = True
            if final_list[2][0] == "$":
                t = False
            val = mov(final_list[1],final_list[2],t)
        elif final_list[0] == "ld":
            temp=var_name[final_list[2]]
            val = ld(final_list[1],temp)
        elif final_list[0] == "st":
            temp=var_name[final_list[2]]
            val = st(final_list[1],temp)
        elif final_list[0] == "mul":
            val = mul(final_list[1],final_list[2],final_list[3])
        elif final_list[0] == "div":
            val = div(final_list[1],final_list[2])
        elif final_list[0] == "rs":
            val = rs(final_list[1],final_list[2])
        elif final_list[0] == "ls":
            val = ls(final_list[1],final_list[2])
        elif final_list[0] == "xor":
            val = xor(final_list[1],final_list[2],final_list[3])
        elif final_list[0] == "or":
            val = or_(final_list[1],final_list[2],final_list[3])
        elif final_list[0] == "and":
            val = and_(final_list[1],final_list[2],final_list[3])
        elif final_list[0] == "not":
            val = not_(final_list[1],final_list[2])
        elif final_list[0] == "cmp":
            val = cmp(final_list[1],final_list[2])
        elif final_list[0] == "jmp":
            val = jmp(final_list[1])
        elif final_list[0] == "jlt":
            val = jlt(final_list[1])
        elif final_list[0] == "jgt":
            val = jgt(final_list[1])
        elif final_list[0] == "je":
            val = je(final_list[1])
        elif final_list[0] == "hlt":
            val = hlt()
    if flag == True:
        print(val)


