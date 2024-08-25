import sys

def reverse_file_content(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()[::-1]

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)

    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file_content(inpu_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        
    except Exception as e:
        print(f"Am error occurred: {e}")

def duplicate_file_content(input_file, output_file, count):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            duplicated_content = ' '.join([content] * count)
        
        with open(output_file, 'w', encoding="utf-8") as outfile:
            outfile.write(duplicated_content)
        
    except Exception as e:
        print(f"Am error occurred: {e}")

def replaces_file_content(input_file, output_file, needle, newstring):
    try:
        with open(input_file, 'r', encoding="utf-8") as infile:
            content = infile.read()
            replaced_content = content.replace(needle, newstring)
            print(replaced_content)
        
        with open(output_file, 'w', encoding="utf-8") as outfile:
            outfile.write(replaced_content)

    except Exception as e:
        print(f"Am error occurred: {e}")
            


if __name__ == "__main__":
    if len(sys.argv) == 4:
        _, command, input_file, output_file = sys.argv

        if command == 'reverse':
            reverse_file_content(input_file, output_file)

        if command == 'copy':
            copy_file_content(input_file, output_file)

    if len(sys.argv) == 5:
        _, command, input_file, output_file, count = sys.argv

        if command == 'duplicate':
            duplicate_file_content(input_file, output_file, int(count))

    if len(sys.argv) == 6:
        _, command, input_file, output_file, needle, newstring = sys.argv

        if command == 'replace':
            replaces_file_content(input_file, output_file, needle, newstring)
    
    else:
        print("Usage: python3 file_manipulator.py <input_file> <output_tile> ... arguments")