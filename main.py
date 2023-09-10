import random


def replace_characters(text):
    replacements = {
        'a': 'а', 'd': 'ԁ', 'e': 'е', 'g': 'ɡ', 'i': 'і', 'j': 'ј',
        'l': 'I', 'n': 'ո', 'o': 'ο', 'p': 'р', 's': 'ѕ', 
        'v': 'ν', 'x': 'х', 'y': 'у', 'z': 'z'
    }

    replaced_text = []
    for char in text:
        if char in replacements:
            replaced_text.append(replacements[char])
        else:
            replaced_text.append(char)

    return ''.join(replaced_text)


def main(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read()

        modified_text = replace_characters(input_text)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(modified_text)

        print("Text replacement complete. Check the output file:", output_file)

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file path
    output_file = "output.txt"  # Replace with your desired output file path
    main(input_file, output_file)
