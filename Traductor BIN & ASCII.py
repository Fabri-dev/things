# Get the binary code from the user
binary_code = input("Enter the binary code: ")

# Split the binary code into 7-bit chunks
chunks = [binary_code[i:i+7] for i in range(0, len(binary_code), 7)]

# Initialize an empty string to store the translated ASCII characters
ascii_string = ""

# Translate each chunk of binary code into an ASCII character
for chunk in chunks:
  ascii_string += chr(int(chunk, 2))

# Print the translated ASCII string
print(ascii_string)





   

        
