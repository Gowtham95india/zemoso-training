#!/user/bin/env python 

#Opening File -- Command Line Inputs in Appending Mode
f = open("cli.txt", 'a')

try:
	read_more = "yes" 	
	while read_more:
		f.write(raw_input("cmd>:")+":\t"+raw_input("desc>:")+"\n")
		read_more = raw_input("to continue, type anything:")
	else:
		f.close()
		print "[+] File Closed! All Commands  are Saved!"
except Exception as e:
	f.close()	#Closing File if error raised
	print "[+] File Closed! All Commands are saved except the last one!"
	print "[-] Error Occured! Error is %s"%e
