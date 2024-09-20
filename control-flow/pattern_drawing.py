# pattern_drawing.py

def main():
    # Prompt User for Pattern Size
    size = int(input("Enter the size of the pattern: "))
    
    # Initialize row counter
    row = 0
    
    # Draw the Pattern
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

if __name__ == "__main__":
    main()
