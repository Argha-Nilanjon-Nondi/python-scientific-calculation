import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self,**kwargs):
		self.value=kwargs
		
	@property
	def contents(self):
		lis=[]
		for i in self.value:
			for j in range(self.value[i]):
				lis.append(i)
				
		return str(lis)
		
	
		
	def draw(self,no):
		new_list=[]
		data_dic=list(self.value)
		
		for i in range(no):
			rand_no=random.randrange(len(data_dic))
			new_list.append(data_dic[rand_no])
			
		for i in new_list:
			
			self.value[i]=self.value[i]-1
			
		return new_list
	
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = 0
    for i in range(num_experiments):
        exp_hat = copy.deepcopy(hat)

        drawn_balls = exp_hat.draw(num_balls_drawn)

        good_exp = True
        for color, number in expected_balls.items():
            ball_num_in_draw = drawn_balls.count(color)
            if ball_num_in_draw < number:
                good_exp = False
                break

        if good_exp:
            prob += 1

    return prob / num_experiments

    return prob_cnt / num_experiments	
hat = Hat(red=5,blue=2)
actual = hat.draw(2)
print(actual)
print(hat.contents)

"""
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
"""