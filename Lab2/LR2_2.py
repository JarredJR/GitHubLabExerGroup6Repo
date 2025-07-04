def main():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines]

        total_lines = len(lines)
        print(f"The file has {total_lines} lines.")

        while True:
            line_number = input(f"Enter a line number (1 to {total_lines}, or 0 to quit): ")

            if not line_number.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            
            line_number = int(line_number)

            if line_number == 0:
                print("Exiting the program.")
                break
            elif 1 <= line_number <= total_lines:
                print(f"Line {line_number}: {lines[line_number - 1]}")
            else:
                print(f"Invalid line number. Please enter a number between 1 and {total_lines}.")

    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
