def find_string(line):
    open_quote = -1
    for idx, char in enumerate(line):
        if char == '"' and open_quote != -1:
            return line[open_quote: idx]
        if char == '"':
            open_quote = idx + 1
    return line 

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

def read_file(file_path):
    file = open(file_path, 'r')
    lines = file.read().split('\n')

    stack = []
    idx = 0

    while idx + 1 < len(lines):
        line = lines[idx].lstrip()
        if line == '}':
            stack[-2].append(stack[-1])
            stack.pop()
            idx += 1
            continue
            
        key = find_string(line)
        item = line[len(key) + 4:]
        arg = [key, item]

        if item == '{':
            empty_li = []
            stack.append(empty_li)
        else:
            stack[-1].append(arg)
        idx += 1
    return stack[0]

def read(file_path):
    file = open(file_path, 'r')
    lines = file.read().split('\n')

    stack = {}
    idx = 0

    while idx < len(lines):
        line = lines[idx].lstrip()
        key = find_string(line)

        #"TEXT":_item... 2 for " and then 2 for :_
        item = line[len(key) + 4:]
        if item == '{':
            empty_dict = {}
            stack[key] = empty_dict
        elif item == '}':
            keys = list(stack.keys())
            stack[keys[-2]][keys[-1]] = stack.pop(keys[-1])
        else:
            keys = list(stack.keys())
            stack[keys[-1]] = item
        idx += 1
    return stack

if __name__ == "__main__":
    print(read_file("quiz_data.txt"))   
