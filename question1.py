# Write a program that prints a mulSplicaSon table for numbers up to 12
def multiplication_table():
    for i in range(1, 13):
        table = "\n".join([f"{i} x {j} = {i * j}" for j in range(1, 13)])
        print(table)
        print("\n")

multiplication_table()
