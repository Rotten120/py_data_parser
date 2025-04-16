def read_str(line):
    stack = [[]]
    idx = 0

    while idx + 1 < len(line):
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

if __name__ == "__main__":
    line = "{a{bc{b}}d}"
    print(read_str(line))
