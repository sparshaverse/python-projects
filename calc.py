def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

print("Select Operation: 1.Add 2.Subtract")
choice = input("Enter choice(1/2):")
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))

if choice == '1':
    print(add(num1,num2))
elif choice == '2':
    print(subtract(num1,num2))
else:
    print("Invalid input")