fruitdict = {
    "ORANGE" : "A orange circular fruit.",
    "STRAWBERRY" : "A fruit which is red and is quite tough, but good and juicy",
    "BLUEBERRY" : "A blue berry, also known as a star berry for its shape on the top looking like a star",
    "BLUEBERRY2" : "A blue berry, also known as a star berry for its shape on the top looking like a star"
}
print(fruitdict)
print(fruitdict["ORANGE"])
print(fruitdict.keys())
print(fruitdict.values())

for HOMEWORKSUCKS in fruitdict:
    print(HOMEWORKSUCKS, fruitdict[HOMEWORKSUCKS])

if "KIWI" in fruitdict:
    print("True")
else:
    print("False")

if "ORANGE" in fruitdict:
    print("True")
else:
    print("False")

fruitdict["PAPAYA"] = "An okay-ish fruit, depends on the mood. Some people strongly like it, while others are the opposite and strongly dislike it."

print(fruitdict)

del(fruitdict["BLUEBERRY2"])

print(fruitdict)
