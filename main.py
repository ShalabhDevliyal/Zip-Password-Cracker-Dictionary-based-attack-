import zipfile

def dictionary_approach(password_script, obj):
    idx = 0

    with open(password_script, 'rb') as list:

            for line in list:

             for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)

                    print("Password found at line", idx)

                    print("Password is", word.decode())

                    print("====================================================================================")
                    print("************************************************************************************")
                    print("====================================================================================")
                    return True
                except:
                    continue
    return False

print("====================================================================================")
print("************************************************************************************")

print("\nZIP PASSWORD CRACKER  -- BY SHALABH DEVLIYAL")

print("\n************************************************************************************")
print("====================================================================================")

password_script = input("\nEnter the Name of Password File or Script : ")

print("------------------------------------------------------------------------------------")

zip_file = input("\nEnter the Name of Zip file : ")

print("------------------------------------------------------------------------------------")

print("\n Please Wait for sometime")

obj = zipfile.ZipFile(zip_file)

combination_present = len(list(open(password_script, "rb")))

print("------------------------------------------------------------------------------------")

print("\n There are total", combination_present,
      "Number of Combinations avliable in the used List/script\n")
      
print("------------------------------------------------------------------------------------")

if dictionary_approach(password_script, obj) == False:
    
    print("------------------------------------------------------------------------------------")

    print("Unable to detect the Password,Please try another Script or file.\n")

    print("\n************************************************************************************")