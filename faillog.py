import sys
from os import path
import re
from datetime import *
import time


Username = []
Date = []
Time = []
lines = []
DateSorted = []
TimeSorted = []




def __main__():
	option,file_path = argv_valid()
	read_file(file_path)


	if option == '-a':print_username()
	elif option == '-u':find_by_username()
	elif option == '-t':find_by_time()
	elif option == '-v':print_myname()





def argv_valid():
	option = sys.argv[1]
	file_path = sys.argv[-1]
	valid_option = ['-a','-u', '-t', '-v']

	if option not in valid_option:
		print("Error: invalid option.")
		sys.exit(1)

	if not (path.exists(file_path)):
		print("Error: file does not exist.")
		sys.exit(1)

	if not (path.isfile(file_path)):
		print("Error: file is not a file.")
		sys.exit(1)

	return option, file_path



def read_file(file_path):
	file = open(file_path, "r")
	if file.readable() == False:
		print("Error: file is not readable.")

	for line in file:
		categorized = re.split(" ", line)
		Username.append(categorized[0])
		Date.append(categorized[1])
		Time.append(categorized[2])
		lines.append(line.rstrip("\n"))


	





def print_username():
	if len(Username) == 0:
		print("No usernames found")
		sys.exit(1)
	elif len(sys.argv) > 3:
		print("Error: too many arguments.")
		sys.exit(1)
	elif len(sys.argv) < 3:
		print("Error: insufficient arguments.")
		sys.exit(1) 
	print("Usernames:")
	for username in Username:
		print(username)


def find_by_username():
	if len(sys.argv) > 4:
		print("Error: too many arguments.")
		sys.exit(1)
	elif len(sys.argv) < 4:
		print("Error: insufficient arguments.")
		sys.exit(1) 
	

	username = sys.argv[2]
	match = 0
	print("Events for user: "+ username)

	for index in range(len(Username)):
		if Username[index] == username:
			print(lines[index])
			match = 1

	if match == 0:
		print("No events found for the given username")



def find_by_time():
	if len(sys.argv) > 5:
		print("Error: too many arguments.")
		sys.exit(1)
	elif len(sys.argv) < 5:
		print("Error: insufficient arguments.")
		sys.exit(1) 
	
	
	date = sys.argv[2]
	time = sys.argv[3]

	dateArgumentSorted = datetime.strptime(date, "%d/%m/%Y")
	timeArgumentSorted = datetime.strptime(time, "%H:%M:%S")

	for line in Date:
		line = line.rstrip("\n")
		DateSorted.append(datetime.strptime(line, "%d/%m/%Y"))

	for line in Time:
		line = line.rstrip("\n")
		TimeSorted.append(datetime.strptime(line, "%H:%M:%S"))

	match = 0

	for index in range(len(DateSorted)):
		if DateSorted[index] >= dateArgumentSorted and TimeSorted[index] >= timeArgumentSorted:
			print(lines[index])
			match = 1

	if match == 0:
		print("No events found for the given date/time")










def print_myname():
	if len(sys.argv) > 3:
		print("Error: too many arguments.")
		sys.exit(1)
	elif len(sys.argv) < 3:
		print("Error: insufficient arguments.")
		sys.exit(1) 
	print("Chuanxu, WANG, 12426894, 2021/05/10")






__main__()



