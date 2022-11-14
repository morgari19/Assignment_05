#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AMorgan, 2022-Nov-12, Edited File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory \n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            strItem = ''
            for item in row.values():
                strItem += str(item) + ', '
            strItem = strItem[:-2]
            print(strItem)
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        delkey = input('Please provide ID of the CD you wish to delete: ')
        delindex =-1
        for row in lstTbl:
            delindex += 1
            if row['ID'] == int(delkey):
                del lstTbl[delindex]
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strItem = ''
            for item in row.values():
                strItem += str(item) + ','
            strItem = strItem[:-1] + '\n'
            objFile.write(strItem)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

