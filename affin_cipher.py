def  encrypt(key_a, key_b, text):
     encrypted_text = ""
     for char in text:
          if char.isalpha():
               if char.islower():
                    encrypted_text += chr(((key_a * (ord(char) - ord('a')) + key_b) % 26) + ord('a'))
               else:
                    encrypted_text += chr(((key_a* (ord(char) - ord('A')) + key_b) % 26) + ord('A'))
          else: 
               encrypted_text += char
     return encrypted_text    
    

def mod_inverse(a, m):
     for i in range(1,m):
          if (a * i ) % m == 1:
             return i
     return None

def decrypt(key_a, key_b, cipher_text):
     decrypted_text = ""
     mod_inverse_a = mod_inverse( key_a, 26)

     if mod_inverse_a is None:
          return "Key 'a' does not have modular inverse!"
    
     for char in cipher_text:
          if char.isalpha():
               if char.islower():
                    decrypted_text += chr(((mod_inverse_a * (ord(char) - ord('a') - key_b)) % 26) + ord('a'))
               else:
                    decrypted_text += chr(((mod_inverse_a * (ord(char) - ord ('A') - key_b)) % 26) + ord('A'))
          else:
               decrypted_text += char
     return decrypted_text

plain_text = input("Enter a plain text: ")
key_a = int(input("Enter a key as integer: "))
key_b = int(input("Enter another key as integer: "))

encrypted_text = encrypt(key_a, key_b, plain_text)
print("\nEncrypted Text: ", encrypted_text)

decrypted_text = decrypt(key_a, key_b, encrypted_text)
print("Decrypted Text: ", decrypted_text)