def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def max_width(text):
    lines = text.split('\n')
    return max(list(map(lambda x: width(x), lines)))

def width(line):
    width = len(line) * 6 + 6
    for element in line:
        if element == ',' or element == '\'':
            width -= 6
        else:
            width += 12
    return width

def max_height(text):
    return len(text.split('\n')) * 36 + 174

if __name__ == '__main__':
    f = read_file('lorem.in')
    print(max_width(f), max_height(f))

