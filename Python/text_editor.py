def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print("File '{}' created.".format(filename))
    except IOError:
        print("An error occurred while creating the file.")


def write_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content + '\n')
            print("Content appended to '{}'.".format(filename))
    except IOError:
        print("An error occurred while writing to the file.")


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Content of '{}':\n{}".format(filename, content))
    except IOError:
        print("An error occurred while reading the file.")


def main():
    filename = input("Enter the name of the file: ")

    create_file(filename)

    while True:
        print("\n--- Menu ---")
        print("1. Write to the file")
        print("2. Read the file")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            content = input("Enter the content: ")
            write_to_file(filename, content)
        elif choice == '2':
            read_file(filename)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
