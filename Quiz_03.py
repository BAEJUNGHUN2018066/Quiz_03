students = [90, 45, 64, 9, 17, 29]

results = []

for grade in students :
    if grade >= 71 :
        results.append("A")
    elif grade >= 41 :
        results.append("B")
    elif grade >= 11 :
        results.append("C")
    else:
        results.append("D")

print(results)
