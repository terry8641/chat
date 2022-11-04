#更改input成output

#chat = []
#name = ['Allen', 'Tom']
#with open('input.txt', 'r', encoding='utf-8') as f:
#	for line in f:
#		if name[0] in line:
#			with open('output.txt', 'a', encoding='utf-8') as f:
#				f.write(name[0] + ':' + '\n')
#		if name[1] in line:
#			with open('output.txt', 'a', encoding='utf-8') as f:
#				f.write(name[1] + ':' + '\n')
#
#		contents = line.strip()
#		chat.append([contents])

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有直，不是None的話
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
	
main()