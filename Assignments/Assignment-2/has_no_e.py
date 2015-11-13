# Priya Mohan - 1005035315
import string

def has_no_e(input):
	if not 'e' in input:
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
	