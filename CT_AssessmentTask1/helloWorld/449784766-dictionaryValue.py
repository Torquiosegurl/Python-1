#This program takes an encrypted message and uses a list of 1000 words to brute force and cross check with every word in the code
#This program should ask the user for an input file, an output file and a dictionary file of words.
#All dictionary words shorter than 3 letters are ignored.

import os # Import the os module for path operations
print("Current working directory:", os.getcwd())

def ascii_decrypt(text, shift): #convert char to ascii and subtracts shift
    result = []
    for ch in text:
        # Convert char → ASCII, subtract shift, wrap around 0–255
        new_code = (ord(ch) - shift) % 256
        result.append(chr(new_code))
    return "".join(result)


def break_ascii_cipher_multiple(ciphertext, crib_list):
    for shift in range(256):
        decrypted = ascii_decrypt(ciphertext, shift)
        lower_dec = decrypted.lower()

        for crib in crib_list:
            if crib.lower() in lower_dec:
                return shift, decrypted, crib  #return which crib matched with the encrypted

    return None, None, None

#gets encrypted message, an output file and dictionary file
try: #takes care of errors - does not offer second chance - must manually try again
    # Read encrypted file
    input_file = input("Enter the input file: ").strip()
    with open(input_file, "r", encoding = "latin1") as f:
        cipher = f.read()

    outputFilename = input("Enter the output file: ").strip()

    #read dictionary file - contains one word for now.
    crib_file = input("Enter the known value file: ").strip()
    with open(crib_file, "r", encoding="latin1") as f:
        cribs = [line.strip() for line in f if len(line.strip()) > 3]


    # Attempt to break cipher with multiple words
    shift, plaintext, matched_crib = break_ascii_cipher_multiple(cipher, cribs)

    if shift is None: #output - error message and success message
        print("❌ Error: No matching shift found for any known word.")
    else:
        print("Key found:", shift)
                # Write output file
        with open(outputFilename, "w", encoding="latin1") as f:
                    f.write(plaintext)
        print(f"✅ Success! Decrypted message written to '{outputFilename}'")


except FileNotFoundError: #file name is incorrect
    print("❌ Error: Input file not found. Check the filename and try again.")

except Exception as e: #other errors
    print("❌ An unexpected error occurred:", e)