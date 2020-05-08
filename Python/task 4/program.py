import customer_account as c
print("\t1.Staff login\n\t2.close program")
choice=input('Enter your choice(1or2):  ')
filename='staff.txt'
with open(filename) as f:
	file=f.read()
lst=file.split(',')
if choice=='1':
	name=[]
	while True:
		username=input('Enter your username: ')
		password=input('Enter your password: ')
		for num in range(0,len(lst)):
			if lst[num]==username and lst[num+1]==password:
				print('\nLogin successful')
				name.append(lst[num+3])
				print(f'Welcome {name[0]}\n')
				c.account()
				if choice=='1':
					c.create_account()
				elif choice=='2':
					c.retrieve_account()		
				else:
					continue
				break		
			else:
				print('wrong username or password')
				break
		if name:
			break
		else:
			continue
else:
    print('Thanks for banking with us')
				
