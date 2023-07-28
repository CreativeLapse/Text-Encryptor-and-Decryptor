def encrypt():
  text = input("Type what you want to encrypt: ")
  codefrequency = int(input("Type the code frequency: "))
  encryptedtext = ""
  
  for char in text:
    encryptedtext += str(codefrequency * ord(char)) + " "
    
  print(f"Encrypted with frequency {codefrequency}:\n{encryptedtext}")

def decrypt():
  string = input("Type what you want to decrypt: ")
  codefrequency = int(input("Type the code frequency: "))
  decryptedtext = ""

  codelist = string.split()
  for code in codelist:
    decryptedtext += chr(int(code) // codefrequency)
    
  print(f"Decrypted with frequency {codefrequency}:\n{decryptedtext}")

crypt = input("Encrypt or decrypt? ")

if crypt == "encrypt":
  encrypt()
elif crypt == "decrypt":
  decrypt()
else:
  print("Invalid input")
