def parse_rec(text):
	list=[]
	new_text=""	
	for i in str(text):
		try:
			if i =="," or i==")":
				list.append(int(new_text))
				new_text=""
			int(i)
			new_text+=i
		except:
			pass	
	return list

												
class Rectangle:
	def __init__(self,width,height):
		self.width=width
		self.height=height

		
	def get_area(self):
		area=self.width*self.height
		return area
		
	def get_perimeter(self):
		perimeter=(2*self.height)+(2*self.width)
		return perimeter
		
		
	def get_diagonal(self):
		diagonal=((self.width ** 2 )+ (self.height** 2) )** 0.5
		return diagonal
		
	def set_height(self,height):
		self.height=height
				
	def set_width(self,width):
		self.width=width
		
	def get_picture(self):
		if ((self.height>50)or(self.width>50)):
			return "Too big for picture."
		else:
			return ("*"*self.width+"\n")*self.height
			
	
	def get_amount_inside(self,pic):
		pic=str(pic)
		data=parse_rec(pic)
		if("Rec" in pic):
			result=int((self.height*self.width)//(data[0]*data[1]))
			return result	
				
		else:
			result=int((self.height*self.width)//(data[0]*data[0]))
			return result
		
	def __str__(self):
		return "Rectangle(width={width}, height={height})".format(width=self.width,height=self.height)	
		
				
		
class Square(Rectangle):
	def __init__(self,side):
		self.side=side

	def get_area(self):
		area=self.side**2
		return area		
		
	def get_perimeter(self):
		perimeter=(2*self.side)+(2*self.side)
		return perimeter
		
		
	def get_diagonal(self):
		diagonal=((self.side ** 2 )+ (self.side ** 2) )** 0.5
		return diagonal
		
	def set_side(self,side):
		self.side=side
				
	def set_width(self,width):
		self.side=width
		
	def get_picture(self):
		return ("*"*self.side+"\n")*self.side
				
	def __str__(self):
		return "Square(side={side})".format(side=self.side)
										
actual = Rectangle(8,7)
actual.set_height(97)
actual.set_width(3)
print(actual.get_picture())