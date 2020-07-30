# database.py                                      #  1
import sys, shelve                                 #  2
                                                   #  3
def store_person(db):                              #  4
    """                                            #  5
    Query user for data and store it in the shelf object #  6
    """                                            #  7
    pid = input('Enter unique ID number: ')        #  8
    person = {}                                    #  9
    person['name'] = input('Enter name: ')         # 10
    person['age'] = input('Enter age: ')           # 11
    person['phone'] = input('Enter phone number: ') # 12
    db[pid] = person                               # 13
                                                   # 14
def lookup_person(db):                             # 15
    """                                            # 16
    Query user for ID and desired field, and fetch the corresponding data from # 17
    the shelf object                               # 18
    """                                            # 19
    pid = input('Enter ID number: ')               # 20
    field = input('What would you like to know? (name, age, phone) ') # 21
    field = field.strip().lower()                  # 22
                                                   # 23
    print(field.capitalize() + ':', db[pid][field]) # 24
                                                   # 25
def print_help():                                  # 26
    print('The available commands are:')           # 27
    print('store  : Stores information about a person') # 28
    print('lookup : Looks up a person from ID number') # 29
    print('quit   : Save changes and exit')        # 30
    print('?      : Prints this message')          # 31
                                                   # 32
def enter_command():                               # 33
    cmd = input('Enter command (? for help): ')    # 34
    cmd = cmd.strip().lower()                      # 35
    return cmd                                     # 36
                                                   # 37
def main():                                        # 38
    database = shelve.open('C:\\database.dat') # You may want to change this name # 39
    try:                                           # 40
        while True:                                # 41
            cmd = enter_command()                  # 42
            if  cmd == 'store':                    # 43
                store_person(database)             # 44
            elif cmd == 'lookup':                  # 45
                lookup_person(database)            # 46
            elif cmd == '?':                       # 47
                print_help()                       # 48
            elif cmd == 'quit':                    # 49
                return                             # 50
    finally:                                       # 51
        database.close()                           # 52
                                                   # 53
if __name__ == '__main__':                         # 54
    main()                                         # 55
