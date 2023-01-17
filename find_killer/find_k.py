"""
## 🐍 CODE CHALLENGE - FIND KILLER & NEXT VICTIM
 
Eric and Terry have been killed by someone they met last week Who is the killer? AND Who is the next Victim?
 
Below are the people each person met last week
 
print the answers
 
input : 'Eric' met ['Jane','John','Mike','Leigh','Todd','Lee','Judy']
 
'Jen' met ['Mark','Mike','Leigh','Jim','Lara','John','Bill']
 
'Terry' met ['Joe','Sara','Reg','Jill','John','Greg','Bryan']
 
'Lara' met ['Pete','Li','Todd','Reg','Jane','Mike','Jen','Ang']
 
output: 'The killer is ???? and the next victim is ???'
 
Try to find a generalised solution that would work for ’any ’ sample and number of people.
 
Have fun!🥳
 
Please share code in editable & Runnable format for others to play with.
 
And discuss / assist each other with code
 
Extra points for not using imports...
 
------------------------------------------
"""


def list_pop(list_of_list, list_to_pop):
    """ Removes a list from list of list if match """
    new_list = []
    matched = 0
    for each_list in list_of_list:
        if len(each_list) == len(list_to_pop):
            for item_index in range(len(each_list)):
                if list_to_pop[item_index] == each_list[item_index]:
                    matched += 1
            if matched != len(list_to_pop):
                new_list.append(each_list)
            matched = 0
        else:
            new_list.append(each_list)
    return new_list


def shortest(list_of_list):
    """ Returns the shortest list from a list of list """
    shortest_list = list_of_list[0]
    for each_list in list_of_list:
        if len(each_list) < len(shortest_list):
            shortest_list = each_list
    return shortest_list


def find_common(list_of_list):
    """ Returns only those items that appear in all the list in list_of_list """
    shortest_list = shortest(list_of_list)
    list_of_list = list_pop(list_of_list, shortest_list)
    common_items = []
    for item in shortest_list:
        for each_list in list_of_list:
            for each_item in each_list:
                if each_item == item and each_item not in common_items:
                    common_items.append(each_item)
    return common_items


potential_victims = {
    "Jen": ['Mark', 'Mike', 'Leigh', 'Jim', 'Lara', 'John', 'Bill'],
    "Lara": ['Pete', 'Li', 'Todd', 'Reg', 'Jane', 'Mike', 'Jen', 'Ang']
}

actual_victims = {
    "Eric": ['Jane', 'John', 'Mike', 'Leigh', 'Todd', 'Lee', 'Judy'],
    "Terry": ['Joe', 'Sara', 'Reg', 'Jill', 'John', 'Greg', 'Bryan']
}

victim_list = []
for victim in actual_victims:
    victim_list.append(actual_victims[victim])

killer = find_common(victim_list)[0]

potential = []
for person in potential_victims:
    people_met = potential_victims[person]
    if killer in people_met:
        potential.append(person)

print(f"The killer is {killer} and the next victim(s) are {potential}")
