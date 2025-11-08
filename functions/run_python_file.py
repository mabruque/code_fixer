import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    subprocess_args = ["python3", abs_file_path]
    if args:
        subprocess_args.extend(args)

    try:
        completed_process = subprocess.run(args=subprocess_args,timeout=30, capture_output=True, text= True)
        if not completed_process.stdout and not completed_process.stderr:
            return "No output produced."
        result = f"STDOUT:\n{completed_process.stdout}\nSTDERR:\n{completed_process.stderr}\n"
        if completed_process.returncode > 0:
            result += f"Process exited with code {completed_process.returncode}"
        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"