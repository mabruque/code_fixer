from functions.write_file import write_file
from functions import run_python_file

# result = get_files_info("calculator", ".")
# print("Result for current directory")
# print(result)

# result = get_files_info("calculator", "pkg")
# print("Result for pkg directory")
# print(result)

# result = get_files_info("calculator", "/bin")
# print("Result for /bin directory")
# print(result)

# result = get_files_info("calculator", "../")
# print("Result for ../ directory")
# print(result)


# result = get_file_content("calculator", "main.py")
# print("Result for main.py in calculator")
# print(result)

# result = get_file_content("calculator", "pkg/calculator.py")
# print("Result for pkg/calculator.py in calculator")
# print(result)

# result = get_file_content("calculator", "/bin/cat")
# print("Result for /bin/cat in calculator")
# print(result)

# Test for write file
# result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print("Writing lorem.txt in calculator")
# print(result)

# result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print("Writing pkg/morelorem.txt in calculator")
# print(result)

# result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print("Writing /tmp/temp.txt in calculator")
# print(result)

# Test for run_python_file
result = run_python_file("calculator", "main.py")
print("Running  calculator/main.py")
print(result)

result = run_python_file("calculator", "main.py", ["3 + 5"])
print("Running  calculator/main.py 3+5")
print(result)

result = run_python_file("calculator", "tests.py")
print("Running  calculator/tests.py")
print(result)

result = run_python_file("calculator", "../main.py")
print("Running  calculator/../main.py")
print(result)

result = run_python_file("calculator", "nonexistent.py")
print("Running  calculator/nonexistent.py")
print(result)

result = run_python_file("calculator", "lorem.txt")
print("Running  calculator/lorem.txt")
print(result)

