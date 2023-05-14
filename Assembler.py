def add(r1,r2,r3):
    ans = disc_isa["add"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def sub(r1,r2,r3):
    ans = disc_isa["sub"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans
def mov(r1,r2,flg):
    if flg:
        ans =  disc_isa["mov1"]["opcode"]+"0"+disc_reg[r1] 
        r2 = str(bin(int(r2[1:])))[2:]
        if (len(r2) != 8):
            for i in range (0,8-len(r2),1):
                ans +="0"
        ans += r2
    else:
        ans =  disc_isa["mov2"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans
def ld(r1,mem_add):
    ans = disc_isa["ld"]["opcode"]+"0"+disc_reg[r1]+mem_add
    return ans

def st(r1,mem_add):
    ans = disc_isa["st"]["opcode"]+disc_reg[r1]+mem_add
    return ans

def rs(r1,r2):
    ans = disc_isa["rs"]["opcode"]+"0"+disc_reg[r1]
    r2 = str(bin(int(r2[1:])))[2:]
    if (len(r2) != 8):
        for i in range (0,8-len(r2),1):
            ans += "0"
    ans += r2

def ls(r1,r2):
    ans = disc_isa["ls"]["opcode"]+"0"+disc_reg[r1]
    r2 = str(bin(int(r2[1:])))[2:]
    if (len(r2) != 8):
        for i in range (0,8-len(r2),1):
            ans += "0"
    ans += r2

def mul(r1,r2,r3):
    ans = disc_isa["mul"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def div(r1,r2):
    ans = disc_isa["div"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans

def xor(r1,r2,r3):
    ans = disc_isa["xor"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def or_(r1,r2,r3):
    ans = disc_isa["or"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def and_(e1,e2,e3):
    ans = disc_isa["and"]["opcode"]+"00"+disc_reg[e1]+disc_reg[e2]+disc_reg[e3]
    return ans

def not_(r1,r2):
    ans = disc_isa["not"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans

def compare(r1,r2):
    ans = disc_isa["cmp"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans

def hlt():
    ans = disc_isa["hlt"]["opcode"]+"00000000000"
    return ans 

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


disc_reg = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}

disc_isa = {
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

list_of_instructions = list(disc_isa.keys()) #Code to create a list which contains all the instructions 
list_of_instructions.remove("movi")          #of the isa
list_of_instructions.remove("movr")
list_of_instructions.append("mov")

list_of_registers = list(disc_reg.keys()) #Code to create a list which contains all the name of the 
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
        
list_of_new_instructions = ['var','var','var','ld','ld','st','jmp','add','hlt_label:'] # makes list of instructions according to order of calling
list_of_jmp = [["hlt_label",8,'hlt']]                                                  # makes list of jumping on label with the line to traverse and instruction given in that line
list_reg = [['R1',3],['R2',4],['R3',5],['R1',7],['R2',7],['R3',7]]                     # list of registers with number of line called in
list_var = ['var1','var2','var3']                                                      # list of variables declared according to order

