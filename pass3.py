f = open('passwd6.txt','w')
for id in range(999999):
	password = str(id).zfill(6)+'\n'
	f.write(password)
f.close()
#this is a zhushi
#this is the second edit
