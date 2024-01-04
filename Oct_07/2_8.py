filename = "python_notes.txt"
extensionless_filename = filename.removesuffix(".txt")

print(extensionless_filename)

assert extensionless_filename == "python_notes"