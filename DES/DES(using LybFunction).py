#Sanket Badjate 
#Roll No- 03
from Crypto.Cipher import DES
cipher = DES.new("8bytekey")
encrypted_data = cipher.encrypt("0123data")
print (encrypted_data)
print (cipher.decrypt(encrypted_data))
