import argparse
import sqlite3
connection = sqlite3.connect('arnab.db')

# cursor.execute("""
#                     CREATE TABLE sets(
#                         set_id integer,
#                         set_name text,
#                         elements integer
#                     )
#                 """)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path" , help="The Operation You Want This App To Do")
    args = parser.parse_args()
    # print(args.path)
    if args.path == "add-set":
        print("Add S1 , S2 , ....SM , Each have elements M")
        number_of_sets = int(input("How Many Sets Do You Like To Play With : "))
        # print(number_of_sets*2)
        sets = []
        cursor = connection.cursor()
        for i in range(number_of_sets):
            # print(i+1)
            print("------------------------------------------------------------------------------")

            set_id = int(input("Enter Set Id(Must Be Unique) : "))
            set_name = input("Name Each Set Differently For Better Analysis : ")
            elements = int(input("How Many Number Of Elements will {x} have : ".format(x=set_name)))

            sets.append([set_id , set_name , elements])
            cursor.execute("INSERT INTO sets VALUES({X},'{Y}',{Z})".format(X=set_id,Y=set_name,Z=elements))
            connection.commit()

        print("DONE ! Sets are Added, Run \"python arnab.py view-sets\" to view all the sets created")
        print(sets)
        connection.close()

    elif args.path == "view-sets":

        print("This Operation Lists All The Sets")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sets")
        all_sets = cursor.fetchall()
        # print(all_sets)
        for set in all_sets:
            print("---------------------------------------")
            print("Set Id : "+str(set[0]))
            print("Set Name : "+set[1])
            print("Elements in "+str(set[1])+" : "+str(set[2]))

        connection.commit()
        connection.close()
    elif args.path == "clear":

        print("This Operation Removes All Sets")
        concent = input("This Will Delete All Sets, Press Enter To Continue")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sets")
        connection.commit()
        connection.close()
        print("Phew! All Clear, run \"python arnab.py add-set\" to add sets all you want")

    elif args.path == "same-elements":

        print("Solution To Problem 1")
        print("Obtaining a non empty subset of stacks such that all stacks of this subset have the same number of elements")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sets")
        all_sets = cursor.fetchall()
        elements_list = []
        elements_set = set()
        result= []
        for set in all_sets:
            elements_list.append(set[2])
            elements_set.add(set[2])

        print(elements_list)
        print(elements_set)
        for ele in elements_set:
            count = elements_list.count(ele)
            data = {'elements' : ele , 'repeat' :count}
            result.append(data)
        print(result)
        connection.commit()
        connection.close()

    else :
        print("Invalid Operation Requested : Run \"python arnab.py -h\" for help")
