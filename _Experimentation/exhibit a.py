first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
# right-hand side expressions are resolved, and allocated in the memory as a new string
message = f"Hello, {full_name.title()}!"
print(message)

first_name = "python"
# message does *not* change, since message does *not* hold references to first_name and last_name
# therefore, message can't react to their changes
print(message)
