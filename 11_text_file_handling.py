# Create a program that reads data from a file and writes it to another file in a different format.

def convert_data(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            # Read data from input file
            data = input_file.read()

        # Modify data to a different format (for example, converting to uppercase)
        modified_data = data.upper()

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_data)
        
        print("Data has been successfully converted and written to", output_filename)
    
    except FileNotFoundError:
        print("File not found.")

def main():
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")

    convert_data(input_filename, output_filename)

if __name__ == "__main__":
    main()
