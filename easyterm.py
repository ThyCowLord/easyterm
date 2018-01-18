import os 
import random
import sys
help = "help"
list = "list"
view = "view"
go = "go"
airplanemode = "airplane mode"
amazingness = "amazingness"
whowins = "who wins"
aurpackage = "aurpackage"
readyplayerone = "ready player one"
androidsay = "androidsay"
edit = "edit"
customcommand = "custom command"
rps = "rps"
cowsay = "cowsay"
easter = "easter"
clear = "clear"
fortune = "fortune"
randomnumber = "random number"
package = "package"
go = "go"
open = "open"
view = "edit"
print("                     _____                  ") 
print("  ___  __ _ ___ _   |_   _|__ _ __ _ __ ___ ") 
print(" / _ \/ _` / __| | | || |/ _ \ '__| '_ ` _ \ ") 
print("|  __/ (_| \__ \ |_| || |  __/ |  | | | | | | ")
print(" \___|\__,_|___/\__, ||_|\___|_|  |_| |_| |_| ")
command = input("Welcome to easyTerm! Type help for a list of commands! ")
if command not in (help, airplanemode, amazingness, whowins, list, "jackass", easter, readyplayerone, cowsay, randomnumber, view, clear, aurpackage, fortune, customcommand, package, open, view, edit, androidsay):
	print("Sorry! Command unknown! Please type help for all available commands. ")
	os.system("python3 easyterm.py")
if command == "help":
	print("The current commands are help (Displays this screen), airplane mode (Self explanatory), amazingness (Gauges something's amazingness) who wins (Chooses a name from a list of two names) edit (Edits a file), fortune (Gives you a fortune) custom command (Executes a non-included command) package(manages, installs and removes programs.), clear (Clears the screen), list (Lists files and folders in the easyterm folder.), random number (Prints a random number.), open (opens a url), and cowsay (Makes a cow say something.") 
	os.system("python3 easyterm.py") 

if command == "list":
	os.system("ls")
	os.system("python3 easyterm.py")
if command == "cowsay":
	subcommand = input("What would you like the cow to say?")
	os.system("cowsay " + subcommand)
	os.system("python3 easyterm.py")
	
if command == "random number":
	random = random.randint(1, 1000000)
	print(random)
	os.system("python3 easyterm.py")

if command == "clear":
	os.system("clear")
	os.system("python3 easyterm.py")
if command == "package":
	debianorarch = input("Are you using debian or arch linux?")
	if debianorarch == "debian":
		package = input("What package would you like to install? ")
		install = "sudo apt-get install "+package
		os.system(install)
		os.system("python3 easyterm.py")
	if debianorarch != ("arch", "debian"):
		print("I'm sorry, that's invalid")
		os.system("python3 easyterm.py")
	else:
		choice1 = input("Would you like to remove or install a package?")
		remove1 = "remove"
		install1 = "install"
		if choice1 not in [remove1, install1]:
			print("I'm sorry, that's not an option.")
			os.system("python3 package.py")
		if choice1 == remove1:
			remove = input("What package would you like to remove? ")
			packremove = "sudo pacman -Rsc "+remove
			os.system(packremove)
		if choice1 == install1:
			install = input("What package would you like to install?")
			packinstall = "sudo pacman -S "+install
			os.system(packinstall)
	
		os.system("python3 easyterm.py")

if command == "custom command":
	command = input("What command would you like to execute?") 
	if command == "sudo rm -rf /":
		print("This command is dangerous.")
		os.system("python3 easyterm.py")
	if command == "sudo chmod -R 777":
		print("This command is dangerous.")
		os.system("python3 easyterm.py")
	os.system(command)
	os.system("python3 easyterm.py")

if command == "fortune":
	os.system("fortune")
	os.system("python3 easyterm.py")
if command == "open":
	web = input("What URL would you like to view? ")
	url = "xdg-open " + web
	os.system(url)
	os.system("python3 easyterm.py")
if command == "view":
	cat = input("What file would you like to view? ")
	command = "cat "+cat
	os.system(command)
	os.system("python3 easyterm.py")

if command == "edit":
	command = input("What file would you like to edit? ")
	nano = "nano "+command
	os.system(nano)
	os.system("python3 easyterm.py")

if command == "exit":
	exit("Thanks for using easyTerm!")
if command == "jackass":
	print("You found an easter egg!")
	print("The donkey says: I'm an ass.")
	os.system("python3 easyterm.py")

if command == "ready player one":
	print("Nice! You found THE easter egg! You now have half a billion dollars and full control of the OASIS! Also, best line from the Ready Player One trailer: 'If you are seeing this, I'm dead.' - James Halliday.")
	os.system("python3 easyterm.py")
if command == easter:
	print("Haha. You thought this was an easter egg.")
	os.system("python3 easyterm.py")

if command == "aurpackage":
	choice1 = input("What package would you like to install? ")
	install = "yaourt "+choice1
	os.system(install)
	os.system("python3 easyterm.py")
if command == "who wins":
	name1 = input("Put in two names, and this program will select who is better. Enter the first name here: ")
	name2 = input("Enter the second name here: ")
	names = [name1, name2]
	choice = random.choice(names)
	print(choice)
	os.system("python3 easyterm.py")
if command == amazingness:
	amazing = input("This tool will gauge something's awesomeness in a percentage. Enter something here: ")
	randomamazing = random.randint(1, 100)
	print("This thing... is", randomamazing, "percent amazing!")
	os.system("python3 easyterm.py")
if command == airplanemode:
	onoroff = input("Would you like airplane mode to be turned on, or off? ")
	if onoroff == "on":
		os.system("sudo rfkill block all")
		os.system("python3 easyterm.py")
	if onoroff == "off":
		os.system("sudo rfkill unblock all")
		os.system("python3 easyterm.py")
	if onoroff != ("off", "on"):
		print("I'm sorry, that's invalid")
		os.system("python3 easyterm.py")




# Thanks for reading!<3
