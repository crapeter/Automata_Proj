from pprint import pprint

"""
Group Members:
	Craig Peterson
	Ethan Norales De La Rosa

Assumptions:
	- The NFA is represented as a 5-tuple: (alphabet, states, init_state, final_states, transitions) along with Beta (input strings)
	- The first two lines of the input file are open parentheses that start the NFA definition and the last three lines contain the input strings (Beta) and closing parentheses.
		- Assuming that we can remove those lines when parsing the alpha tuple
		 ( removed
			( removed
				(0, 1),
				(q0, q1, q2),
				q0,
				(q2),
				((q0, 0, q0), (q0, 1, q0),(q0, 0, q1),(q1, 1, q2))
			), removed 
			() removed
		) removed
"""

"""
BFS implementation of NFA

Inputs: nfa - a 5-tuple representing the NFA
				beta - the input string to process

Outputs: True if beta is accepted by the NFA, False otherwise
"""
def NFA(nfa, beta):
	alphabet, states, init_state, final_states, transitions = nfa

	if not set(beta).issubset(set(alphabet)):
		return False

	current_states = set([init_state])
	# Process each symbol in the input string
	for b in beta:
		next_states = set()
		# Find all possible next states for the current states and input symbol
		for state in current_states:
			# If the state is not in the set of states, skip it
			if not state in states:
				continue
			# Add all possible next states
			for t in transitions:
				if t[0] == state and t[1] == b:
					next_states.add(t[2])
		# Update current states
		current_states = next_states

		""" 
		Print input symbol and current states for visualization if needed
		Uncomment the following two lines to see the states possible for each symbol of beta
		"""
	# 	print(f"Current Symbol \"{b}\": Possible Next States {current_states}")
	# print()

	return not current_states.isdisjoint(set(final_states))


"""
Take user input and runs the NFA on it.
"""
def empty_beta(nfa):
	count = 0
	while True:
		b = input(f"Please input {'a' if count == 0 else 'another'} string: ").strip()

		if b == "":
			print("Bye bye")
			break

		print(f"{"Accepted" if NFA(nfa, b) else "Rejected"}")
		count += 1


"""
Run the NFA on the given beta.
"""
def non_empty_beta(nfa, beta):
	string_accepted = []

	# Process each string in beta and append the result to string_accepted
	for b in beta:
		if NFA(nfa, b):
			string_accepted.append("accepted")
		else:
			string_accepted.append("rejected")
	print("(" + ', '.join(string_accepted) + ")", end='')


"""
Flatten the NFA definition from multiple lines into a single 5-tuple.

Inputs: alpha - list of strings representing the NFA definition
Outputs: nfa - a 5-tuple representing the NFA
"""
def flatten_nfa(alpha):
	# Converts multi-line NFA definition into a single line
	alpha = [line.strip() for line in alpha]
	text = ' '.join(alpha)

	# Split the text into its 5 components
	nfa_parts = []
	current_part = ''
	depth = 0

	# Depth based parsing to handle nested parentheses because we didn't want to use recursion to simulate a recursive descent parser
	for char in text:
		if char == '(':
			depth += 1
			current_part += char
		elif char == ')':
			depth -= 1
			current_part += char
		elif char == ',' and depth == 0:
			if current_part.strip():
				nfa_parts.append(current_part.strip())
				current_part = ''
		else:
			current_part += char

	if current_part.strip():
		nfa_parts.append(current_part.strip())

	if len(nfa_parts) != 5:
		return []

	alphabet = nfa_parts[0]
	states = nfa_parts[1][1:-1].replace(' ', '').split(',')
	init_state = nfa_parts[2]
	final_state = nfa_parts[3][1:-1].replace(' ', '').split(',')
	transitions = nfa_parts[4].strip('()').replace(' ', '').split('),(')
	transitions = [tuple(t.split(',')) for t in transitions]

	return alphabet, states, init_state, final_state, transitions


"""
Parse Input function to open and parse the input file.

Inputs: infile - name of the input file (without .txt extension)
Outputs: nfa (the 5-tuple) and beta (the input string)
"""
def parse_input(infile):
	# Getting the absolute path of the input file
	infile_path = infile + ".txt"
	nfa = []

	# Opening the File and reading the contents
	with open(infile_path, 'r') as f:
		file = f.read().strip()
	lines = file.split('\n')

	# Get input strings (beta)
	beta = lines[-2].strip()[1:-1].split(',')
	beta = [b.strip() for b in beta]

	# Remove all parts of the file that are not alpha
	alpha = lines[2:-3]
	nfa = flatten_nfa(alpha)

	return nfa, beta


"""
Main function to run the NFA
"""
if __name__ == "__main__":
	infile = input("Please input the file name: ").strip()
	nfa, beta = parse_input(infile)

	if not nfa:
		print("Error parsing NFA from input file.")
		exit(1)

	if beta == ['']:
		empty_beta(nfa)
	else:
		non_empty_beta(nfa, beta)