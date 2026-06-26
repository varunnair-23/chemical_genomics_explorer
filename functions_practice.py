student_majors = {
    "Alice": "Computer Science",
    "Ben": "Mathematics",
    "Charlie": "Physics"
}

def lookup_major(name):
    try:
        major = student_majors[name]
        print(f"{name} is a {major} major.")
    except KeyError:
        print(f"No major found for {name}.")

lookup_major("Alice")
lookup_major("Bob")
