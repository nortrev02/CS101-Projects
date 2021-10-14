
import string 

def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.''' 
    code = []
    for i in string_text:
      char = ord(i)
      if(i != " "):
        code.append(chr(65 + ((((char - 65) + int_key) % 26))))
      else:
        code.append(i)
    encoded = "".join(code)
    return encoded  

def Decrypt(string_text, int_key): 
  ''' Decrypts Caesar-encrypted string with specified key. ''' 
  code = []
  for i in string_text:
    char = ord(i)
    if(i != " "):
        code.append(chr(65 + ((((char - 65) - int_key) % 26))))
    else:
        code.append(i)
  decoded = "".join(code)
  return decoded  
  

def Print_menu():
  '''Prints menu. No user interaction. '''
  print("1) Encrypt a (brief) string of text")
  print("2) Decrypt a (brief) string of text")
  print("Q) Quit the program")
  print("Enter your Selection:")
  
def main(): 
  Again = True 
  while Again: 
    Print_menu()
    Choice = input().upper() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper()
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper()
      Key = int(input("Enter the number the letters were shifted by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext)
    elif Choice == "Q": 
      print("Have an ordinary day.") 
      Again = False 
    else:
      print("Please enter one of the valid responses.")
      
      
# our entire program: 
main() 

