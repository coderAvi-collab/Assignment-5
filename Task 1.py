# Student dictionary

students = {
    'alice': 50,
    'sam' : 65,
    'avinaba':100
}

st = input("Enter the student's name:")
st_lower = st.lower()
res = students.get(st_lower, 'Student not found')

if res != 'Student not found':
    marks = students[st_lower]
    print(f"{st}'s marks:", marks)
else: print(res)