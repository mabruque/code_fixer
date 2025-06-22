import os


def get_files_info(working_directory, directory=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = abs_working_dir
        if directory:
            target_dir = os.path.join(abs_working_dir, directory)

        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        directory_content = os.listdir(target_dir)
        directory_content_string = ""
        for content in directory_content:
            content_full_path = os.path.join(target_dir, content)
            size = os.path.getsize(content_full_path)
            is_dir = os.path.isdir(content_full_path)
            directory_content_string += (
                f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"
            )
        return directory_content_string
    except Exception as error:
        return f"Error: {str(error)}"
