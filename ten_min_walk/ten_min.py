'''
Python func that cheks to see if a walk would take 10 minutes.
It gets directions like N, S, E, W that take 1 minute each.
'''


# def is_valid_walk(walk):
#     # determine if walk is valid
#     time = north = south = east = west = 0

#     for i in walk:
#         time += 1
#         if i == 'n':
#             north += 1
#         if i == 's':
#             south += 1
#         if i == 'e':
#             east += 1
#         if i == 'w':
#             west += 1

#     if time == 10 and north == south and east == west:
#         return True
#     else:
#         return False


def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
