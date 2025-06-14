import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(abs_working_dir):
        f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_path):
        f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10_000

    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) < MAX_CHARS:
            return file_content_string

        return f'{file_content_string}\n[...File "{target_file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error: {e}"
