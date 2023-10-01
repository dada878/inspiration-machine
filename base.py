import random
import quick_sqlite

db = quick_sqlite.Database("inspiration.db", auto_init=[])

projects = db.get("__projects__")
if len(projects) == 0:
    print("No projects found. Please create a project.")
    project = input("Project name: ")
    db.set("__projects__", [project])
    projects = [project]

print("===== Please select project =====")
for i in range(len(projects)):
    print(f"{i+1} - {projects[i]} - ({len(db.get(projects[i] + '_inspirations'))})")

selected = 0

while 1:
    selected = int(input("Project: ")) - 1
    if selected < 0 or selected >= len(projects):
        print("Invalid project.")
    else:
        break

while 1:
    print("===== Please select action =====")
    print("1 - Create inspirations")
    print("2 - Remove a inspiration")
    print("3 - Random inspiration")
    print("4 - Exit")
    action = int(input("Action: "))
    if action == 1:
        key_name = projects[selected] + "_inspirations"
        inspirations = db.get(key_name)
        while 1:
            name = input("Input inspiration (q to exit): ")
            if name == "q":
                break
            if name in inspirations:
                print("Inspiration already exists.")
                continue
            inspirations.append(name)
            db.set(key_name, inspirations)
            print("Inspiration added.")
    elif action == 2:
        key_name = projects[selected] + "_inspirations"
        name = input("Input inspiration to remove: ")
        inspirations = db.get(key_name)
        if name not in inspirations:
            print("Inspiration not found.")
        else:
            inspirations.remove(name)
            db.set(key_name, inspirations)
            print("Inspiration removed.")
    elif action == 3:
        count = int(input("How many inspirations do you want? "))
        key_name = projects[selected] + "_inspirations"
        inspirations = db.get(key_name)
        if len(inspirations) < count:
            print("Not enough inspirations.")
        else:
            print("===== Inspirations =====")
            for i in range(count):
                print(random.choice(inspirations))
    else:
        break
    
    
    