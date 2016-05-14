import sys, re

def num_5():
	try:
		line = raw_input("")
		while(line):
			items = line.split()
			file_name = items[0].replace('.txt', '')
			words = items[2:]
			print file_name, words #debug
			
			file = open( file_name+'.txt' )
			content = file.read()
			#print index
			for word in words:
				content = content.replace(word,'***')
			print content
			
			file_mod = open(file_name+'_mod.txt', 'w+')
			file_mod.write(content)
			line = raw_input("")
			
	except EOFError:
		pass
		
if __name__ == "__main__":
	num_5()