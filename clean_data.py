f = open("./cran/cran.all.1400" , "r")
out_data= open("data.csv", "w")
out_data.write("Title\tContent\n")
lin='\"'
r= f.readline()
i=1
while r:
	print i
	
	if ".T" in r:
		l= f.readline()
		
		while l[0]!='.':
			lin+=l[0:-1]
			l= f.readline()
		lin+='\"\t'
	elif ".W" in r:
	
		l= f.readline()
		lin+='\"'
		while '.I' not in l:
			lin+=l[0:-1]
			l = f.readline()
		lin+='\"\n'
		
		out_data.write(lin)
		lin='\"'
		i+=1
		

		
	r= f.readline()
	
