from lexer import Lexer

if __name__ == "__main__":
    path_file_example = "example.txt"
    with open(path_file_example, 'r', encoding="utf-8") as file:
        info = file.read()

    l = Lexer(info)
    l.run()

    for t in l.tokens:
        print(f"Token: [key: '{t.key}', value: '{t.value}']")
