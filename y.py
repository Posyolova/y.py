students = []

with open("y2.txt", "r") as file:
    for line in file:
        values = line.strip().split(";") 
        student = {
            'id': int(values[0]),
            'full_name': values[1],
            'var': int(values[2]),
            'subgroup': int(values[3])
        }
        students.append(student)

print(students)
