import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path
directory_path = "."

# Call the function to print directory contents
print_directory_contents(directory_path)