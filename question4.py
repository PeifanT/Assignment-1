"""Write a program that asks the user to input two lists of equal length in the format: [a,b,c], [1,2,3].
The program should test that both lists are of equal length, if not, print out an error message.
If they are the same length, combine the two lists by alternatingly taking elements and output the results.
Using the input example above, the output would be: [a,1,b,2,c,3]"""

def input_list(prompt):
    while True:
        user_input = input(prompt).strip()

        if not (user_input.startswith("[") and user_input.endswith("]")):
            print("Invalid format. Please enter a list in the format [a,b,c]")
            continue

        try:
            lst = user_input[1:-1].split(",")
            lst = [elem.strip() for elem in lst]

            return lst
        except ValueError:
            print("Invalid input, please enter a list in the format [a,b,c]")


def combine_lists(lst1, lst2):
    return [subitem for pair in zip(lst1, lst2) for subitem in pair]


def main():
    list1 = input_list("Enter the first list in the format [a,b,c]: ")
    list2 = input_list("Enter the second list in the format [1,2,3]: ")

    if len(list1) != len(list2):
        print("Error: The lists are not of equal length.")
    else:
        combined_list = combine_lists(list1, list2)
        formatted_output = "[" + ",".join(combined_list) + "]"
        print(formatted_output)


if __name__ == "__main__":
    main()