def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    while True:
        print(f"\nThe file has {len(lines)} lines.")
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1]}", end="")
            else:
                print("Invalid line number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
