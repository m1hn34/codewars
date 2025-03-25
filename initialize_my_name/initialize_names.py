'''
    Initialize my name

* Your task is to initialize the middle names (if there are any).

Examples:
'Jack Ryan' => 'Jack Ryan'
'Lois Mary Lane' => 'Lois M. Lane'
'Daniel' => 'Daniel'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'
'''


def initialize_names(name):
    name_parts = name.split()
    if len(name_parts) < 3:
        return name
    else:
        short_parts = [name_parts[0]]
        for part in name_parts[1:-1]:
            short_parts.append(part[0] + ".")
        short_parts.append(name_parts[-1])
        return " ".join(short_parts)

