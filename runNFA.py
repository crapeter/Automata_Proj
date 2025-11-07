"""
Group Members:
	Craig Peterson
	Ethan Norales De La Rosa
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
			Uncomment the following two lines to see the states possible for each beta
		"""
	# 	print(f"Current Symbol \"{b}\": Possible Next States {current_states}")
	# print()

	return final_states in current_states

"""
Take user input and runs the NFA on it.
"""
def empty_beta(nfa):
	count = 0
	while True:
		b = input(f"Please input {"a" if count == 0 else "another"} string: ").strip()

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
parse_input function to open and parse the input file.

inputs: infile - name of the input file (without .txt extension)
outputs: nfa (the 5-tuple) and beta (the input string)
"""
def parse_input(infile):
	# Getting the absolute path of the input file
	infile_path = infile + ".txt"

	# Opening the File and reading the contents
	file = open(infile_path).read().strip()
	lines = file.split('\n')

	# Parsing the input file
	alpha = lines[2:7]
	alpha = [line.strip().removesuffix(',') for line in alpha]

	# Get input strings (beta)
	beta = lines[-2].strip()[1:-1].split(',')
	beta = [b.strip() for b in beta]

	# Parsing the NFA components
	alphabet = alpha[0][1:-1].split(',')
	alphabet = [a.strip() for a in alphabet]

	# Parsing states
	states = alpha[1][1:-1].split(',')
	states = [s.strip() for s in states]

	# Parse initial state
	init_state = alpha[2]

	# Parse final states
	final_states = alpha[3][1:-1]

	# Parse transitions
	transitions = alpha[4]
	transitions = transitions[1:-1].split(')')
	transitions = [t[t.index('q'):] for t in transitions if t.strip() != '']
	transitions = [t.split(',') for t in transitions]
	transitions = [[t.strip() for t in trans if t.strip() != ''] for trans in transitions ]

	# Condense states into a single NFA tuple
	nfa = [alphabet, states, init_state, final_states, transitions]

	return nfa, beta

"""
Main function to run the NFA
"""
if __name__ == "__main__":
	infile = input("Please input the file name: ").strip()
	nfa, beta = parse_input(infile)

	if beta == ['']:
		empty_beta(nfa)
	else:
		non_empty_beta(nfa, beta)