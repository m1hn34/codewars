'''
You receive an array with your peers' test scores. Now calculate the average 
and compare your score!

Return True if you're better, else False!

Note:

Your points are not included in the array of your class's points. For 
calculating the average point you may add your point to the given array!
'''


def better_than_average(class_points, your_points):
    class_points.append(your_points)
    if sum(class_points) / len(class_points) < your_points:
        return True
    else:
        return False


class_points = [100, 40, 34, 57, 29, 72, 57, 88]
your_points = 75

print(better_than_average(class_points, your_points))

# print(class_points)
# print(your_points)

# class_points.append(your_points)
# print(class_points)
# print(sum(class_points))

print("it was too late to do anything..")


