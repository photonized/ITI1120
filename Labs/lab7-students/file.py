files = open("file.txt", "w")
sentence=["123","321"]
def write_to_file(file, sentences):
    for s in sentences:
        file.write(s)

write_to_file(files, sentence)