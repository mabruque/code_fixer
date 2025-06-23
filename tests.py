from functions.get_file_content import get_file_content


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


result = get_file_content("calculator", "main.py")
print("Result for main.py in calculator")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print("Result for pkg/calculator.py in calculator")
print(result)

result = get_file_content("calculator", "/bin/cat")
print("Result for /bin/cat in calculator")
print(result)
