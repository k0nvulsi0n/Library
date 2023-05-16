def add_entries(filepath, Model):
    file_source = open(filepath)
    entries_list = []
    for line in file_source.readlines():
        if line[-1] == '\n':
            entries_list.append(line[:-1])
        else:
            entries_list.append(line)
    print(entries_list)  #for debugging
    for entry in entries_list:
        b = Model(name=str(entry))
        b.save()
