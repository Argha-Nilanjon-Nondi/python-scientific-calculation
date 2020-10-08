def data_extract(time,hour):
	
	new_time=[]
	time_session=""
	time+=" "
	
	for i in time:
		if(i==" " or i==":"):
			new_time.append(time_session)
			time_session=""
			continue
		time_session+=i
		
	h=int(new_time[0])
	m=int(new_time[1])
	f=new_time[-1]
	
	g_h=int(hour.split(":")[0])
	g_m=int(hour.split(":")[1])
	
	return int(h),int(m),f,int(g_h),int(g_m)


		
def get_day_no(time1,time2):
	
	data=data_extract(time1,time2)
	
	hour=data[0]
	minu=data[1]
	format=data[2]
	g_hour=data[3]
	g_minu=data[4]		
	
	if(format=="PM"):
		hour+=12
		
	total=hour+g_hour+((minu+g_minu)/60)
	
	total=int(total//24)

	return total
	
def get_hour(time1,time2):
	
	data=data_extract(time1,time2)
	
	hour=data[0]
	minu=data[1]
	format=data[2]
	g_hour=data[3]
	g_minu=data[4]	
	
	new_format="AM"
	
	if(format=="PM"):
		hour+=12
			
	total=(((hour+g_hour)+((minu+g_minu)/60))%24)
	
	print(total)
		
	if(total>=12 ):
		new_format="PM"
		total-=12
		if(total>0 and total<1):
			total=int(total)+12
			
	if(total>0 and total<1):
		total=int(total)+12
		


				
	return int(total),new_format
	
def get_minu(time1,time2):
	
	data=data_extract(time1,time2)
	
	hour=data[0]
	minu=data[1]
	g_hour=data[3]
	g_minu=data[4]	
	
	total1=(minu+g_minu)%60
	
	total2=str(total1)	
	
	if(total1<10):
		total2="0"+str(total1)
		
	
	
	return total2
	

def get_day(time1,time2,day_name=0):		

	data_day={
	
	"Saturday":1,
	
	"Sunday":2,
	
	"Monday":3,
	
	"Tuesday":4,
	
	"Wednesday":5,
	
	"Thursday":6,
	
	"Friday":7	
	}
	
	
	data_bar={
	
	1:"Saturday",
	
	2:"Sunday",
	
	3:"Monday",
	
	4:"Tuesday",
	
	5:"Wednesday",
	
	6:"Thursday",
	
	7:"Friday"	
	}	
	
	data=data_extract(time1,time2)
	
	hour=data[0]
	minu=data[1]
	g_hour=data[3]
	g_minu=data[4]	
	
	
	day_no=get_day_no(time1,time2)
	
	day_type=""
	
	if(day_name!=0):
		day_name=day_name.lower()
		day_name=day_name.capitalize()
		day_name=data_day[day_name]
		day_name=day_name+day_no
		if(day_name%7==0):
			day_type+=", "+data_bar[day_name]
			
		else:
			day_type+=", "+data_bar[day_name%7]		
	
	if(day_no==1):
		day_type+=" (next day)"
		
	if(day_no>1):
		day_type+=" ({0} days later)".format(day_no)
		
	return day_type
	
		
		
def add_time(time1,time2,day=0):
	
	hour=get_hour(time1,time2)[0]
	
	minu =get_minu(time1,time2)
	
	format=get_hour(time1,time2)[1]
	
	day=get_day(time1,time2,day)
	
	day_no=get_day_no(time1,time2)
	
	if(day_no==0 or day_no==1):
		day_no=""
	
	result="{0}:{1} {2}{3}".format(hour,minu,format,day)
	
	return result

time1="11:59 AM"

time2="24:05"
	
print(add_time(time1,time2))
