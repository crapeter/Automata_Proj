from sys import argv

# Group Members:
# 	Craig Peterson
# 	Ethan Norales De La Rosa

# Assumptions:
# 	- The NFA is represented as a 5-tuple: (alphabet, states, init_state, final_states, transitions) along with Beta (input strings)
# 
# 	- Assume that the input can span multiple lines in the input file instead of a single line per string, i.e. alphabet can be on more the one line etc...
# 
# 	- There is always a ")," line that separates the NFA definition from the input strings (Beta).
# 
# 	- The first two lines of the input file are open parentheses that start the NFA definition and the below ")," are not a part of the alpha tuple.
# 		- Assuming that we can remove those lines when parsing the alpha tuple
# 		 ( removed
# 			( removed
# 				(0, 1),
# 				(q0, q1, q2),
# 				q0,
# 				(q2),
# 				((q0, 0, q0), (q0, 1, q0),(q0, 0, q1),(q1, 1, q2))
# 			), removed 
# 			() removed
# 		) removed


"""
'BFS' implementation of NFA
	Explore all possible steps for each symbol in the input string at the same time

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

		print(f"{'Accepted' if NFA(nfa, b) else 'Rejected'}")
		count += 1


"""
Run the NFA on the given beta.
"""
def non_empty_beta(nfa, beta):
	# Process each string in beta and append the result to string_accepted
	strings_accepted = ["accepted" if NFA(nfa, b) else "rejected" for b in beta]
	print("(" + ', '.join(strings_accepted) + ")", end='')


"""
Flatten the NFA definition from multiple lines into a single 5-tuple.

Inputs: alpha - input file as a string
Outputs: nfa - a 5-tuple representing the NFA
"""
def flatten_nfa(alpha):
	# Converts multi-line NFA definition into a single line
	nfa_text = ' '.join(line.strip() for line in alpha)

	# Split the text into its 5 components
	nfa_parts = []
	current_part = ''
	depth = 0

	# Depth based parsing to handle nested parentheses because we didn't want to use recursion to simulate a recursive descent parser
	for char in nfa_text:
		if char == '(':
			depth += 1
		elif char == ')':
			depth -= 1
		elif char == ',' and depth == 0:
			nfa_parts.append(current_part.strip())
			current_part = ''
			continue
		current_part += char

	if current_part.strip():
		nfa_parts.append(current_part.strip())

	if len(nfa_parts) != 5:
		return []

	alphabet = nfa_parts[0]
	states = nfa_parts[1][1:-1].replace(' ', '').split(',')
	init_state = nfa_parts[2]
	final_state = nfa_parts[3][1:-1].replace(' ', '').split(',')
	transitions = [tuple(t.split(',')) for t in nfa_parts[4].strip('()').replace(' ', '').split('),(')]

	return alphabet, states, init_state, final_state, transitions


"""
Parse Input function to open and parse the input file.

Inputs: infile - name of the input file (without .txt extension)
Outputs: nfa (the 5-tuple) and beta (the input string)
"""
def parse_input(infile):
	# Opening the file and reading the contents
	with open(infile, 'r') as f:
		file = f.read().strip()
	lines = [f.strip() for f in file.split('\n')]

	# Find the line where beta starts, if no beta is given then it's an invalid input
	try:
		start_idx = lines.index('),') + 1
	except ValueError:
		print("Error: No beta input strings found in the input file.")
		exit(1)

	# Get all possible lines of the beta input strings
	beta = [b.strip() for b in ' '.join(lines[start_idx:-1]).strip()[1:-1].split(',')]

	# Remove all parts of the file that are not alpha
	nfa = flatten_nfa(lines[2:start_idx - 1])

	return nfa, beta


"""
Main function to run the NFA
"""
if __name__ == "__main__":
	if len(argv) < 2:
		print("Please provide the input file name as a command-line argument.\nUsage: python runNFA.py <input_file_name>")
		exit(1)

	nfa, beta = parse_input(argv[1])

	if not nfa:
		print("Error parsing NFA from input file.")
		exit(1)

	empty_beta(nfa) if beta == [''] else non_empty_beta(nfa, beta)