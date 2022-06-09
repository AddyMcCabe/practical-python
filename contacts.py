contacts = {
    "number":5,
    "students":
        [
            {"name":"Bart Simpson", "email":"bart@example.com"},
            {"name":"Homer Simpson", "email":"Homer@example.com"},
            {"name":"Lisa Simpson", "email":"lisa@example.com"},
            {"name":"Marge Simpson", "email":"marge@example.com"},
            {"name":"Maggie Simpson", "email":"maggie@example.com"}

        ]
}

for student in contacts["students"]:
    print(student["email"])