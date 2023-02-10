'''
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given
a positive integer number of floors. A tower block is represented with "*" 
character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

'''


# Long-but-fast Method
def tower_builder_1(n_floors):
    tower = []
    for i in range(n_floors):
        tower.append(' '*(n_floors-i-1) + '*'*(2*i+1) + ' '*(n_floors-i-1))
    return tower


# Shorter-slower Method with center()
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


# debug
print(tower_builder(3))
