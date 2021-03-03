import  random
import string

letters = string.ascii_letters
numbers = '0123456789'
spe = '-+*/%&$#£>!_-?,;.:=~<|'
symbols = letters + numbers + spe
len = int(input("Enter Pass. Length(Max len : 84 ) : "))
password = ''.join(random.sample(symbols,len))
print(password)