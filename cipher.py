def encode_message(message):
    """
    Encodes a message using a Caesar cipher with a shift of 15.
    - Lowercase letters are shifted within 'a' to 'z'
    - Uppercase letters are shifted within 'A' to 'Z'
    - All other characters (spaces, punctuation, numbers) remain unchanged
    """
    
    encoded = ""  # This will store the final encoded message

    for char in message:
        
        # --- Handle lowercase letters ---
        if char.islower():
            # Convert letter to ASCII, shift by 15
            shifted = ord(char) + 15
            
            # Wrap around if we go past 'z'
            if shifted > ord('z'):
                shifted -= 26
            
            # Convert back to a character and add to result
            encoded += chr(shifted)

        # --- Handle uppercase letters ---
        elif char.isupper():
            # Convert letter to ASCII, shift by 15
            shifted = ord(char) + 15
            
            # Wrap around if we go past 'Z'
            if shifted > ord('Z'):
                shifted -= 26
            
            # Convert back to a character and add to result
            encoded += chr(shifted)

        # --- Handle punctuation, spaces, numbers, etc. ---
        else:
            # Leave non‑alphabetic characters unchanged
            encoded += char

    return encoded


# --- Program execution starts here ---

# Ask the user for a message to encode
user_input = input("Enter a message to encode: ")

# Encode the message using our function
result = encode_message(user_input)

# Display the encoded message clearly
print("Encoded message:", result)
