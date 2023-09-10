# Character Changer

This Python program takes a text file as input, randomly selects visually identical characters from other scripts, and replaces corresponding English characters. It then saves the modified text to a new file.

## Usage

1. Place the text file you want to modify in the same directory as the program.
2. Open the Python file (`main.py`) and specify the input and output file paths.
3. Run the program. It will read the input file, perform character replacements, and save the modified text to the specified output file.

## Customization

You can customize the character replacements by modifying the `replacements` dictionary in the Python file. Add or remove entries in the `replacements` dictionary to suit your preferences.

```python
replacements = {
        'a': 'а', 'd': 'ԁ', 'e': 'е', 'g': 'ɡ', 'i': 'і', 'j': 'ј',
        'l': 'I', 'n': 'ո', 'o': 'ο', 'p': 'р', 's': 'ѕ', 
        'v': 'ν', 'x': 'х', 'y': 'у', 'z': 'z'
    }
```

## Example
Input:
```text
This is a testing file.
It should appear identical.
Text is rendered differently in different fonts, however.

The quick brown fox jumped over the lazy dog.
```
Output:
```text
Thіѕ іѕ а tеѕtіոɡ fіIе.
It ѕhοuIԁ арреаr іԁеոtіcаI.
Tехt іѕ rеոԁеrеԁ ԁіffеrеոtIу іո ԁіffеrеոt fοոtѕ, hοwеνеr.

Thе quіck brοwո fοх јumреԁ ονеr thе Iаzу ԁοɡ.
```

