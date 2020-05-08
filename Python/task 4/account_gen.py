import random
def generator():
	init_num=['08100']
	for a in range(5):
		init_num.append(str(random.randint(0,9)))
	acc_no=''.join(init_num)
	return acc_no