class Staff_record():
	'''This class stores in the user details'''
	def __init__(self,u_name,pwd,email,f_name,file):
		self.u_name=u_name
		self.pwd=pwd
		self.email=email
		self.f_name=f_name
		self.file=file
	def save(self):
		with open(self.file,'a') as f:
			f.write(self.u_name)
			f.write(self.pwd)
			f.write(self.email)
			f.write(self.f_name)