name = " \t Xingkai Chen \n"
lstripped_name = name.lstrip()
rstripped_name = name.rstrip()
stripped_name = name.strip()

print(name)
print(lstripped_name)
print(rstripped_name)
print(stripped_name)

assert lstripped_name == "Xingkai Chen \n"
assert rstripped_name == " \t Xingkai Chen"
assert stripped_name == "Xingkai Chen"