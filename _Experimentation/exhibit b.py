first_name = "ada"
last_name = "lovelace"

def full_name():
    return f"{first_name} {last_name}"

def message():
    return f"Hello, {full_name().title()}!"

# message is calculated
print(message())

first_name = "python"
# message is recalculated with the reference to the new values
print(message())

