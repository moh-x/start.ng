from account_gen import generator
def account():
	print('''1.Create new bank account details
2.Check account details
3.Logout''')
	choice=input('Enter an option as provided above: ')
def create_account():
		acc_name=input('Enter account name: ')
		open_balance=input('Enter amount you want to use in opening account: ')
		acc_type=input('Enter account type(savings/current): ')
		acc_email=input('Enter account email: ')
		account_no=generator()
		print(f'Account successfully created,your account number is {account_no}')
		with open('customer.txt','w') as f:
			f.write(acc_name+',')
			f.write(open_balance+',')
			f.write(acc_type+',')
			f.write(acc_email+',')
			f.write(account_no+',')
def retrieve_account():
		with open('customer.txt') as f:
			file=f.read()
		lst=file.split(',')
		account_no=input('Enter account number of the customer: ')
		for num in range(0,len(lst)):
			if lst[num]==account_no:
				print(f'Account name:{lst[num-4]}')
				print(f'Opening balance:{lst[num-3]}')
				print(f'Account type:{lst[num-2]}')
				print(f'Account email:{lst[num-1]}')
				break
			else:
				print('Customer details does not exist')
				