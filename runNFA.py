import sys

infile = sys.argv[1]
file = open(infile).read().strip()
lines = file.split('\n')


"""
BFS implementation of NFA

Inputs: nfa - a 5-tuple representing the NFA
				beta - the input string to process

Outputs: True if beta is accepted by the NFA, False otherwise
"""
def NFA(nfa, beta):
	alphabet, states, init_state, final_states, transitions = nfa

	if not set(beta) == set(alphabet):
		return False

	current_states = set([init_state])
	for b in beta:
		next_states = set()
		for state in current_states:
			for t in transitions:
				if t[0] == state and t[1] == b:
					next_states.add(t[2])
		current_states = next_states
		# Print current states and input symbol for visualization if needed
		# print(f"{b}: {current_states}")

	return final_states in current_states

"""
Take user input and run the NFA on it.
"""
def empty_beta(nfa):
	while True:
		b = input("Please input a string: ").strip()
		if b == "":
			print("Bye bye")
			break
		if NFA(nfa, b):
			print("Accepted.")
		else:
			print("Rejected.")

"""
Run the NFA on the given beta.
"""
def non_empty_beta(nfa, beta):
	string_accepted = []
	for b in beta:
		if NFA(nfa, b):
			# print(f"{b}: Accepted.")
			string_accepted.append("accepted")
		else:
			# print(f"{b}: Rejected.")
			string_accepted.append("rejected")
	print("(" + ', '.join(string_accepted) + ")", end='')

if __name__ == "__main__":
	alpha = lines[2:7]
	alpha = [line.strip().removesuffix(',') for line in alpha]

	beta = lines[-2].strip()[1:-1].split(',')
	beta = [b.strip() for b in beta]

	alphabet = alpha[0][1:-1].split(',')
	alphabet = [a.strip() for a in alphabet]

	states = alpha[1][1:-1].split(',')

	init_state = alpha[2]

	final_states = alpha[3][1:-1]

	transitions = alpha[4]
	transitions = transitions[1:-1].split(')')
	transitions = [t[t.index('q'):] for t in transitions if t.strip() != '']
	transitions = [t.split(',') for t in transitions]
	for t in transitions:
		for i in range(len(t)):
			t[i] = t[i].strip()


	nfa = [alphabet, states, init_state, final_states, transitions]

	if beta == ['']:
		empty_beta(nfa)
	else:
		non_empty_beta(nfa, beta)


