import statistics
import matplotlib.pyplot as plt

def get_data():
    data = input("Enter numbers seperated by space: ")
    return list(map(float, data.split()))

def show_menu():
    print("\n--- Statistics Menu ---")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Standard Deviation")
    print("5. Variance")
    print("6. Histogram")
    print("7. Box Plot")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (0-7): ")

    if choice == '0':
        print("Exiting program. Goodbye!")
        break

    elif choice in ['1', '2', '3', '4', '5', '6', '7']:
        data = get_data()

        if choice == '1':
            print("Mean:", statistics.mean(data))

        elif choice == '2':
            print("Median:", statistics.median(data))

        elif choice == '3':
            try:
                print("Mode:", statistics.mode(data))
            except statistics.StatisticsError:
                print("No unique mode found.")

        elif choice == '4':
            print("Standard Deviation:", statistics.stdev(data))

        elif choice == '5':
            print("Variance:", statistics.variance(data))

        elif choice == '6':
            plt.hist(data, bins=5, color='skyblue', edgecolor='black')
            plt.title("Histogram")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()

        elif choice == '7':
            plt.boxplot(data)
            plt.title("Box Plot")
            plt.ylabel("Values")
            plt.show()
    else:
        print("Invalid choice. Please enter a number from 0 to 7.")
