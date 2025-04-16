def read_str(line):
    stack = [[]]
    idx = 0

    while idx + 1 < len(line):
        print(stack)
        char = line[idx]
        if char == '{':
            empty_li = []
            stack.append(empty_li)
        elif char == '}':
            stack[-2].append(stack[-1])
            stack.pop()
        else:
            stack[-1].append(char)
        idx += 1
    return stack[1]

def find_string(line):
    open_quote = -1
    for idx, char in enumerate(line):
        if char == '"' and open_quote != -1:
            return line[open_quote: idx]
        if char == '"':
            open_quote = idx + 1
    return line 

def read(file_path):
    file = open(file_path, 'r')
    lines = file.read().split('\n')

    stack = {{}}
    idx = 0

    while idx < len(lines):
        line = lines[idx].lstrip()
        key = find_string(line)
        
            

        
        line = lines[idx].lstrip()
        key = find_string(line)
        args[key] = line[line.find(": "):]
        idx += 1
    return args

if __name__ == "__main__":
    print(read("aaa.txt"))   
