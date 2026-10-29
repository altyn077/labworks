fin = open('mailbox.txt', 'r')
fot = open('output.txt', 'w')
email=fin. readlines()
count=0
for line in email:
    if "@" in line:
        count=count+1
fot.write(str(count))
fin. close()
fot.close()