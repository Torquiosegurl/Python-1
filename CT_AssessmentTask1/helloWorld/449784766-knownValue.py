#This program takes an encrypted message from a file with one known value and tries to decode it
#This is done by running the known value through all possible shifts and compares it to the encrypted message.

import os # Import the os module for path operations
print("Current working directory:", os.getcwd())

def ascii_decrypt(text, shift): #convert char to ascii and subtracts shift
    result = []
    for ch in text:
        # Convert char → ASCII, subtract shift, wrap around 0–255
        new_code = (ord(ch) - shift) % 256
        result.append(chr(new_code))
    return "".join(result)


def break_ascii_cipher(ciphertext, known_word): #looking to see if known value is in the message. If not then try/except will handle
    known_word = known_word.lower()

    for shift in range(256):
        decrypted = ascii_decrypt(ciphertext, shift)
        if known_word in decrypted.lower():
            return shift, decrypted

    return None, None

#gets encrypted msg, an output file and
try: #takes care of errors - does not offer second chance - must manually try again
    # Read encrypted file
    input_file = input("Enter the input file: ").strip()
    with open(input_file, "r", encoding="latin1") as f:
        cipher = f.read()

    outputFilename = input("Enter the output file: ").strip()
    crib = input("What is your known value? ")

    # Attempt to break cipher
    shift, plaintext = break_ascii_cipher(cipher, crib)

    if shift is None:
        print("❌ Error: No matching shift found. Known value not detected.")
    else:
        print("Key found:", shift)
        # Write output file
        with open(outputFilename, "w", encoding="latin1") as f:
            f.write(plaintext)

        print(f"✅ Success! Decrypted message written to '{outputFilename}'")

except FileNotFoundError:
    print("❌ Error: Input file not found. Check the filename and try again.")

except Exception as e:
    print("❌ An unexpected error occurred:", e)

