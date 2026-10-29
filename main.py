f = open("mailbox.txt")
out = open("output.txt", "w")

for line in f:
    if "java" in line:
        out.write(line)

f.close()
out.close()