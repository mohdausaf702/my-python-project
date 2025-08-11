# dict={
#     "name":"Ausaf",
#     "CGPA": 9.2,
#     "marks": [98,97,96]
# }
# print(dict)

# info={
#     "key":"value",
#     "name":"JMI",
#     "learning":"Bioinformatics"
# }
# print(info)

#   Accept all data types

# info= {
#     "name": "Ausaf",
#     "Subject": ["Python", "R"],
#     "Topics": ("dict","Set"),
#     "age":   25,
#     "marks": 94.5
# }
# print(info)

# print(info["name"])
# print(info["topics"])
# print(info["subject"])
# print(info["age"])
# print(info["age"])


# info= {
#     "name": "Ausaf",
#     "Subject": ["Python", "R"],
#     "Topics": ("dict","Set"),
#     "age":   25,
#     "marks": 94.5
# }
# print(info)
#
# # Assign new value
#
# info["name"]="Mohd"
# print(info)
#
# #  Add new key value
# info["Sur Name"]= "Gaur"
# print(info)

#  Make empty dict


# info={
#     "key":"value",
#     "name":"JMI",
#     "learning":"Bioinformatics"
# }
# print(info)
# null={}
# print(null)

#  Nested dictionaries in python

# student= {
#      "name": "Ausaf",
#      "score":{
#          "Chem":96,
#          "Phy": 94,
#          "math": 92
#      }
# }
# print(student)
# print(student["score"]["math"])

# student= {
#      "name": "Ausaf",
#      "score":{
#          "Chem":96,
#          "Phy": 94,
#          "math": 92
#      }
# }
# # print(len(student))
# print(list(student.key()))


student = {
    "name": "Ausaf",
    "score": {
        "Chem": 96,
        "Phy": 94,
        "math": 92
    }
}

print(list(student.keys()))
print(student.values())
print(student.items())


