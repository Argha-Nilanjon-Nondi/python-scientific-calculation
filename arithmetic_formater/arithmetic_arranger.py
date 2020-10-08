def arithmetic_arranger(rows,result=False):
	"""
	arithmetic_arranger is a function for mathematical purpose:
		
	it need two argument:
	row is list
	result is a boolean (optional)
	
	It is a project for freecodecamp
	"""
	
	#collection of data - start
	number=[]
	operator=[]
	space=[]
	#collection of data - end
	
	for x in range(len(rows)):
		#erro condition 1-start
		if(len(rows)>5):
			return "Error: Too many problems."
		#erro condition 1-end
			
		#erro condition 2-start
		if(("-" not in rows[x]) and ("+" not in rows[x])):
			return "Error: Operator must be '+' or '-'."
			
		#erro condition 2-end
		
		for c in rows[x]:
			try:
				if(c==" " or c=='+' or c=="-"):
					pass
				else:
					int(c)
			except:
				return "Error: Numbers must only contain digits."
		
	
	#data collection process - start
	
	for i in rows:
		i=i.replace(" ","")
		
		if "+" in i:
			operator.append("+")
			num1=i.split("+")
			ele1=num1[0]
			ele2=num1[-1]
			
			#error condition 3-start
			if((len(ele1)>4) or (len(ele2)>4)):
				return "Error: Numbers cannot be more than four digits."
			#error condition 3-end
			
			number.append([int(ele1),int(ele2)])
			
			if( len(ele1) >= len(ele2) ):
				space.append( len(ele1)+2)
				
			else:
				space.append( len(ele2)+2)			
		else:
			operator.append("-")
			num1=i.split("-")
			ele1=num1[0]
			ele2=num1[-1]
			if((len(ele1)>4) or (len(ele2)>4)):
				return "Error: Numbers cannot be more than four digits."			
			number.append([int(ele1),int(ele2)])
			
			if( len(ele1) >= len(ele2) ):
				space.append( len(ele1)+2)
				
			else:
				space.append( len(ele2)+2)
				
	#data collection process - end
	
	#making string for result - start
	str1=""
	str2=""
	str3=""
	str4=""	
	gap0="    "
	
	for j in range(len(number)):
		
		ele1=str(number[j][0])
		gap1=" "*(space[j]-len(ele1))
		str1+=gap1+ele1+gap0
		
	
		ele2=str(number[j][1])
		gap2=" "*((space[j]-1)-(len(ele2)))
		str2+=operator[j]+gap2+ele2+gap0
		
		str3+=("-"*space[j])+gap0
		
		if(result==True):
			
			ele1=number[j][0]
			ele2=number[j][1]
			
			if(operator[j]=="+"):
				re_no=ele1+ele2
				
			else:
				re_no=ele1-ele2
			
			
			gap3=" "*(space[j]-len(str(re_no)))
			
			str4+=gap3+str(re_no)+gap0
			
		else:
			pass
			
	#making string for result - end
		
	#return str1+"\n"+str2+"\n"+str3+"\n"+str4
	
	return  "{0}\n{1}\n{2}\n{3}".format(str1,str2,str3,str4)
	
	
print(arithmetic_arranger(["3992 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))


expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"

print(expected)