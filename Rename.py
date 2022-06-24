import os

print("Author: Bo Fethe")
print("Purpose: To rename files within a desired directory\n\n")

# Define the prefix function
def prefixText():

    # Pick the prefix you want
    word = input('Enter prefix: ')
    print()

    # Iterate through all the files in home directory
    changed = 0
    unchanged = 0

    for file in os.listdir("."):
        fileName, ext = os.path.splitext(file)
        
        #Make sure the prefix isn't alraedy there and skip the python script as well
        if (not word + '_' in fileName) and (ext != '.py'):
            os.rename(file, word + "_" + fileName + ext)
            changed += 1

        else:
            unchanged += 1

    #print the results
    print("Files renamed: " + str(changed) + '\n' + "Files skipped: " + str(unchanged) + '\n')

# Define the suffix function
def suffixText():

    # Pick the suffix you want
    word = input('Enter suffix: ')
    print()

    # Iterate through all the files in home directory
    changed = 0
    unchanged = 0

    for file in os.listdir("."):
        fileName, ext = os.path.splitext(file)

        #Make sure the suffix isn't alraedy there and skip the python script as well
        if (not '_' + word in fileName) and (ext != '.py'):
            os.rename(file, fileName + "_" + word + ext)
            changed += 1

        else:
            unchanged += 1

    #print the results
    print("Files renamed: " + str(changed) + '\n' + "Files skipped: " + str(unchanged) + '\n')

# Define the replace function
def replaceText():

    # Pick the text you want to replace
    target = input('Enter the target text you want to replace: ')

    # Pick the new text you want to be shown
    newValue = input('Enter the new text you want: ')
    print()

    # Iterate through all the files in home directory
    changed = 0
    unchanged = 0

    for file in os.listdir('.'):
        fileName, ext = os.path.splitext(file)
        
        if target in fileName:
            newName = fileName.replace(target, newValue)
            os.rename(file, newName + ext)
            changed += 1

        else:
            unchanged += 1

    #print the results
    print("Files renamed: " + str(changed) + '\n' + "Files skipped: " + str(unchanged) + '\n')

# Pick which function should be called
def funCall():

    # Pick the directory
    folder = input('Enter the path to the folder with the files to be renamed: ')
    path = os.path.normcase(folder)
    os.chdir(path)
    
    # List the operation types and ask for the desired function
    print('Operation types:', 'p - Add a prefix', 's - Add a suffix', 'r - Replace text', '', sep='\n')
    funtype = input('Enter type of operation: ')
    funtype = funtype.lower()

    # Call the appropraite function
    if funtype == 'p':
        prefixText()

    elif funtype == 's':
        suffixText()

    elif funtype == 'r':
        replaceText()

    else:
        print('Invalid type of operation')

    # See if the user wants to do another operation
    repeat = input('Do another operation? (y/n): ')
    if repeat.lower() == 'y':
        funCall()

funCall()

input('\nPress any key to close the window')
