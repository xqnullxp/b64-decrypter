#wrote by null
#kys
#imma big booter haxxer man
import os, base64, time

print('would you like to  decrypt a message?')

option = input('yes or no?:  ')

if option == 'yes':
    msg = input('what would you like to decrypt: ')
    time.sleep(2)
    os.system(cls)
    decoded = base64.standard_b64decode(msg)
    print(decoded)

if option == 'no':
    print('ok')
    time.sleep(1)
    exit()
