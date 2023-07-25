def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as test_file:
        test_file.write(f'{file_content}')

def append_file(file_name, append_content):
     with open(f'{file_name}.txt', mode='a', encoding='utf-8') as test_file:
        test_file.write(f'{append_content}')

def read_file(file_name):
    test_file = open(f'{file_name}.txt', encoding='utf-8')
    return(test_file.read())
    test_file.close()
