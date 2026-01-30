monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve","Frank"}
monday_class.add("Grace")

print(f"Monday class: {monday_class}")

print(f"Wednesday class: {wednesday_class}")

print(f"Attended both class: {monday_class & wednesday_class}")

print(f"Attended either class: {monday_class | wednesday_class}") # | This is called a pipe

print(f"Only Attended Monday class: {monday_class - wednesday_class}")

print(f"Only Attended one class (not both): {monday_class ^ wednesday_class}") # ^ this is a carret

all_classes = monday_class | wednesday_class

print ("Is monday subset of all students? ", monday_class <= all_classes) # it should return true (Always boolean)
