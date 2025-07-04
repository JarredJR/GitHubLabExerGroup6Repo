def mean(numbers):
    if not numbers: 
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:  
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint - 1] + numbers[midpoint]) / 2

def mode(numbers):
    if not numbers: 
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_count = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_count]
    if len(mode) == len(numbers):
        return 0 
    elif len(mode) == 1:
        return mode[0] 
    else:
        return mode  

def main():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, 'r') as file:
            numbers = []
            for line in file:
                words = line.split()
                for word in words:
                    try:
                        numbers.append(float(word))
                    except ValueError:
                        continue  

            print("Numbers:", numbers)
            print("Mean:", mean(numbers))
            print("Median:", median(numbers))
            print("Mode:", mode(numbers))
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
