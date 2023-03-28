def logical_and(a, b):
    return ''.join(['_' if x == '_' or y == '_' else '-' for x, y in zip(a, b)])

def logical_or(a, b):
    return ''.join(['_' if x == '_' and y == '_' else '-' for x, y in zip(a, b)])

def logical_xor(a, b):
    return ''.join(['_' if x == y else '-' for x, y in zip(a, b)])

def logical_nand(a, b):
    return ''.join(['_' if x != '_' and y != '_' else '-' for x, y in zip(a, b)])

def logical_nor(a, b):
    return ''.join(['_' if x != '_' or y != '_' else '-' for x, y in zip(a, b)])

def logical_nxor(a, b):
    return ''.join(['-' if x == y else '_' for x, y in zip(a, b)])

n = int(input())
m = int(input())

inputs = {}
outputs = {}

# read inputs
for i in range(n):
    name, signal = input().split()
    inputs[name] = signal

# read outputs
for i in range(m):
    name, gate, input1, input2 = input().split()
    if gate == 'AND':
        signal = logical_and(inputs[input1], inputs[input2])
    elif gate == 'OR':
        signal = logical_or(inputs[input1], inputs[input2])
    elif gate == 'XOR':
        signal = logical_xor(inputs[input1], inputs[input2])
    elif gate == 'NAND':
        signal = logical_nand(inputs[input1], inputs[input2])
    elif gate == 'NOR':
        signal = logical_nor(inputs[input1], inputs[input2])
    elif gate == 'NXOR':
        signal = logical_nxor(inputs[input1], inputs[input2])
    outputs[name] = signal

for name, signal in outputs.items():
    print(name, signal)