nat='abra kadabra fastethernet/1234 13451'
rez=''
count= (len(nat))
i=0
for i in range(count):
#    print (i)
    if nat[i]=='f' and nat[i+1]=='a' and nat[i+2]=='s' and nat[i+3]=='t':
	rez=rez+'gigabit'
	continue
    if nat[i-1]=='f' and nat[i]=='a' and nat[i+1]=='s' and nat[i+2]=='t':
	continue
    if nat[i-2]=='f' and nat[i-1]=='a' and nat[i]=='s' and nat[i+1]=='t':
	continue
    if nat[i-3]=='f' and nat[i-2]=='a' and nat[i-1]=='s' and nat[i]=='t':
	continue
    rez=rez+nat[i]
print (rez)