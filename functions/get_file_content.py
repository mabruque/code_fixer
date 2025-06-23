import os

MAX_CHARS = 10000


def read_file(file_path):
    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    return file_content_string


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_content = read_file(abs_file_path)
        if len(file_content) == MAX_CHARS:
            file_content += f' [...File "{file_path}" truncated at 10000 characters]'
        return file_content

    except Exception as error:
        return f"Error: {str(error)}"
