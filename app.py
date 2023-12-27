# app.py

def is_digit(char):
    return '0' <= char <= '9'

def main():
    user_input = input("Введите символ: ")
    result = is_digit(user_input)
    
    if result:
        print(f"Символ {user_input} - цифра")
    else:
        print(f"Символ {user_input} - не цифра")

if __name__ == "__main__":
    main()
