sm = { "alice": 85,"nimesh": 90,"yadip": 78,"David": 92 }
n = input("Enter the student's name: ")

if n in sm:
    print(f"{n}'s marks: {sm[n]}")
else:
    print("Student not found.")
