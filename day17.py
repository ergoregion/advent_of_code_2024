import re
import numba

with open('data/day17data', 'r') as file:
    lines = file.readlines()
    a_values = re.findall(r"\d+", lines[0])
    a= int(a_values[0])
    b_values = re.findall(r"\d+", lines[1])
    b= int(b_values[0])
    c_values = re.findall(r"\d+", lines[2])
    c= int(c_values[0])

    code_lines = re.findall(r"\d+", lines[4])
    code= [ int(x) for x in code_lines]


print(a)
print(b)
print(c)
print(code)

class Registers:
    def __init__(self):
        self.a =0
        self.b =0
        self.c = 0

registers = Registers()

def combo_operand(i):
    if i in range(4):
        return i
    elif i ==4:
        return registers.a
    elif i ==5:
        return registers.b
    elif i==6:
        return registers.c
    else :
        assert(False)


result = []
def operation(code, oprand):
    if code ==0:
        registers.a = registers.a // pow(2, combo_operand(oprand))
        return None
    elif code ==1:
        registers.b=registers.b ^ oprand
        return None
    elif code ==2:
        combo = combo_operand(oprand)
        cme = combo %8
        registers.b=cme
        return None
    elif code ==3:
        if (registers.a ==0):
            return None
        else:
            return oprand
    elif code ==4:
        registers.b = registers.b ^ registers.c
        return None
    elif code ==5:
        result.append(combo_operand(oprand) % 8)
        return None
    elif code ==6:
        registers.b = registers.a // pow(2, combo_operand(oprand))
        return None
    elif code ==7:
        registers.c = registers.a // pow(2, combo_operand(oprand))
        return None
    else:
        raise (False)

def code_step(code,position):
    code_number = code[position]
    operand = code[position + 1]
    jump = operation(code_number, operand)
    if jump is None:
        return position + 2
    else:
       return jump

def run_code(code):
    position = 0
    while (position <len(code)):
        position = code_step(code,position)

registers.c =9
run_code([2,6])
assert(registers.b==1)

registers.a = a
registers.b = b
registers.c = c

run_code(code)
print(','.join([str(x) for x in result]))

def short(a,n):
    d = ((a//pow(8,n)) % 8) ^ 6
    return (d ^ (a // pow(2, d)) ^ 7) % 8

def try_next_field(last,targets):
    if len(targets) ==0:
        print(f"Sucess: {last}")
        return
    for i in range(8):
        value = 8*last+i
        if short(value,0) == targets[-1]:
            try_next_field(value, targets[:-1])

targets =[2, 4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]

try_next_field(0, targets)


registers.a = 47910079998866
registers.b = 0
registers.c = 0
result = []
run_code(code)
print(','.join([str(x) for x in result]))
