import difflib

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def compare_files(file1_path, file2_path):
    lines1 = read_file(file1_path)
    lines2 = read_file(file2_path)

    differ = difflib.Differ()
    diff = list(differ.compare(lines1, lines2))

    return diff

file1_path = 'C:\\Users\\admin\\Documents\\file2.txt'
file2_path = 'C:\\Users\\admin\\Documents\\file1.txt'

differences = compare_files(file1_path, file2_path)

for line in differences:
    print(line)













