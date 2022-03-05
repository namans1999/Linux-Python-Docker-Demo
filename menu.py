import os
from docker import docker
os.system("clear")
os.system("tput setab 53")
os.system("tput setaf 1")
print("\t\tWelcome To the UI")
os.system("tput setaf 7")
print("-------------------------------------------------")
print("""Where would you like to perform the function 
1. Local
2. Remote
Enter Your Choice""",end=" ")
location=input()
if location=="1":
	print("Starting Local Environment")
	print ("""Select the Services from below 
1 : To see Date
2 : To see Calander
3 : To Configure Apache Web Server
4 : To Create a new user
5 : To Create a New File
6 : To Check if a Program is installed or not
7 : To Find Location of the Program
8 : To Enter Docker World
Enter Your Choice:""",end=" ")
	ch=input()
	if ch=="1":
		os.system("date") 
	elif ch=="2":
		os.system("cal")
	elif ch=="3":
		os.system("systemctl disable firewalld")
		os.system("systemctl start httpd")
		os.system('echo "Welcome to The Apache Web Server" > /var/www/html/index.html')
		os.system('firefox localhost')
	elif ch=="4":
		uname=str(input("Enter the name of user you want to add: "))
		os.system("useradd {}".format(uname))
	elif ch=="5":
		fname=str(input("Enter the name of the File with its format: "))
		os.system("touch {}".format(fname))
	elif ch=="6":
		pname=str(input("Enter name of the Program : "))
		os.system("rpm -q {}".format(pname))
	elif ch=="7":
		sname=str(input("Enter Name of The Software you find to location: "))
		os.system("which {}".format(sname))
	elif ch=="8":
		docker()
	else:
		print("Wrong Input")
		print("Enter Your choice again",end=" ")
		ch=input()
elif location=="2":
	print("Enter IP Address to connect to")
	ip_add=input()
	os.system('ssh {}'.format(ip_add))
	## I have to add a Connection Checking Code
	
else:
	print("Wrong Input")
	location=input("Re-Enter Your Choice : ")

os.system("tput setab 0")
os.system("tput setaf 7")



#----------------------------------------------------------------------------------------




