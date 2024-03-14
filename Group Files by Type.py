# Author: Aaditya Vaibhav Sah


import os, time

Folders = ['FILE FOLDERS','']
OtherEx = ['OTHER EXTENSIONS','']
Sorted = []
path = input("Enter a Path: ")
print_path = input("Do you want to print the Direct(Executable) Path of the Files or Folders also? [Y/N] ")[0]
if print_path.upper().__eq__('Y'):
    print_path = 1
else:
    print_path = 0


def remove_duplicate_items_from_any_list(a_list):
    a_list = list(a_list)
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def getfileextensionlist(path):
    exs = []
    for file_path, dir, files in os.walk(path):
        for i in files:
            if '.' not in i:
                if print_path == 1:
                    OtherEx.append(f'{i}\nExecutable Path: {os.path.abspath(file_path)+'\\'+i}')
                else:
                    OtherEx.append(f'{i}')
                continue
            ext = ''
            for j in range(len(i) - 1, -1, -1):
                if str(i)[j].__eq__('.'):
                    ext += '.'
                    break;
                else:
                    ext += str(i)[j]
            ext2 = ''
            for i in range(len(ext) - 1, -1, -1):
                ext2 += ext[i]
            exs.append(ext2)
    return remove_duplicate_items_from_any_list(exs)

if os.path.isdir(path.strip()):
    file_extensions_in_that_path = getfileextensionlist(path=path)
    for file_path, dir, files in os.walk(path):
        for i in dir:
            if print_path == 1:
                Folders.append(f'{i}\nPath: {os.path.abspath(file_path)+'\\'+i}')
            else:
                Folders.append(f'{i}')
        for file_name in files:
            for extension_name in file_extensions_in_that_path:
                if file_name.endswith(extension_name):
                    if str(extension_name).replace('.','').upper()+' FILES' not in Sorted:
                        Sorted.append(str(extension_name).replace('.','').upper()+' FILES')
                    if print_path == 1:
                        Sorted.append(f'{file_name}\nPath: {os.path.abspath(file_path)+'\\'+file_name}')
                    else:
                        Sorted.append(f'{file_name}')
    for i in Sorted:
        if i.isupper() and i.endswith('FILES'):
            print('\n')
        print(i)
    if not len(Folders) == 2:
        print('\n\n')
        for i in Folders:
            print(i)
    if not len(OtherEx) == 2:
        print('\n\n')
        for i in OtherEx:
            print(i)
    choice = input("Do you want to save these results in a Text File? [Y/N] ")[0]
    if choice.upper() == 'Y':
        with open('Files Sorted by Type.txt','w+') as f:
            data = ''
            for i in Sorted:
                if i.isupper() and i.endswith('FILES'):
                    data += '\n'
                data+=i+'\n'
            if not len(Folders) == 2:
                data +='\n\n'
                for i in Folders:
                    data+=i+'\n'
            if not len(OtherEx) == 2:
                data+='\n\n'
                for i in OtherEx:
                    data+=i+'\n'
            f.write(f'------------------------------------------------------------------\nResults of the Directory "{path}"\n------------------------------------------------------------------\n{data}')
        print('Thank You for using this Tool')
        print("The File has been Saved in the same Directory")
        print('Exiting in ',end='')
        for i in range(4,0,-1):
            print(f'{i}',end=' ')
            time.sleep(1)
    else:
        print('Thank You for using this Tool')
        print('Exiting in ', end='')
        for i in range(4, 0, -1):
            print(f'{i}', end=' ')
            time.sleep(1)
else:
    print("Invalid Path or Directory")