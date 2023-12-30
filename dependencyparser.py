result_list = []

with open("list.txt", mode="r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        #print(line, end="")
        lines[i] = lines[i].strip()
        if i != len(lines) - 1:
            result_list.append('"' + lines[i] + '",')
        else:
            result_list.append('"' + lines[i] + '"')

for item in result_list:
    print(item, end="\n")