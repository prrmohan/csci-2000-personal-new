import string

def has_no_e(input):
	for i in range(0, len(input)-1):
		if(input[i] == ('e')):
			return 'false'
		
	return 'true'
	
def main():
	fr = open("gadsby_stripped.txt")
	
	while(fr.readline()):
		line = fr.readline()
		check = has_no_e(line)
		print(check)
	
if __name__ == '__main__':
    main()
	