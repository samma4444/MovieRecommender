
name = list("#asdf")

for i in range(len(name)):
    if (name[i] == '#') :
        name[i] = ''

name = "".join(name)
print(name)
