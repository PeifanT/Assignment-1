"""Write a program that asks a user to input a string and then determine if it’s a palindrome.
If it is, print out “The string <the string the user typed in> [is | is not] a palindrome.
If the user types q, the program exits"""

def palindrome(s):
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

def main():
    while True:
        user_input = input("Enter a string to check if it's a palindrome (enter 'q' to quit): ")
        if user_input == 'q':
            break
        if palindrome(user_input):
            print(f"The string '{user_input}' is a palindrome.")
        else:
            print(f"The string '{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()
