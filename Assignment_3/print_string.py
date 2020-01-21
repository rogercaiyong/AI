def print_string(*str, sep = ' ', end = '\\n'):
    string = sep.join(str) + end
    print(string)

print_string('This is a test')
print_string('This', 'is', 'a', 'test')
print_string('This', 'is', 'a', 'test', sep = '-')
print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')
