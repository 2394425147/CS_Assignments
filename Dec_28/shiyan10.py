def find_file(file_name: str) -> str:
    """
    Locates a file in the current directory, falling back to parent directories if it's not found.

    Parameters:
    file_name: The name of the file to locate.

    Returns:
    The relative path to the file.
    """
    import os

    file_under_script_directory = os.path.join(os.path.dirname(__file__), file_name)
    if os.path.exists(file_under_script_directory):
        return file_under_script_directory

    if os.path.exists(file_name):
        return file_name

    raise FileNotFoundError(f"File {file_name} not found.")

def main():
    with open(find_file("shiyan10.py"), "r") as f:
        lines = f.readlines()
        line_count = len(lines)
        line_count_width = len(str(line_count))
        for index, line in enumerate(lines):
            print(f"{index + 1:>{line_count_width}} | {line}", end="")
    pass

if __name__ == "__main__":
    main()