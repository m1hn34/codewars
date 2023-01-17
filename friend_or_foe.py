def friend(x):
    y = []
    for i in x:
        if len(i) == 4:
            y.append(i)
    return y


print(friend(["Ryan", "Kieran", "Mark", ]))
