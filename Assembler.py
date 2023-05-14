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



