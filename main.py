try:
    filename: str = 'test.txt'
    file = open(filename, 'r')
    content = file.read()
    lines = content.split('\n')
    for line in lines:
        counter: int = 0
        words = line.split(' ')
        for word in words:
            if len(word) > 1 and not word.isdigit() or word.isalpha() and word == 'I':
                counter += 1
        print(f'{line} - {counter}')

except FileNotFoundError as e:
    print(f"File Not Found: {filename}")
except Exception as e:
    print(f"Exeption: {e}")