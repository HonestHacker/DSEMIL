import sys

code = open(sys.argv[1], 'r').read()

class DSEMILEngine:
	def __init__(self, code):
		self.code = code
		self.vars_values = {}
	def dsemil_eval(self, eq):
		py_eq = ""
		for x in eq:
			if x.isalpha():
				py_eq += str(self.vars_values[x])
			else:
				py_eq += x
		return eval(py_eq)
	def run(self, debug=False):
		instructions = code.split("\n")
		for comstr in instructions:
			com = comstr.split()
			if debug:
				print(com)
			if com[0] == "input":
				if com[1] != "<-":
					raise SyntaxError("DSEMIL syntax is not valided.")
				for arg in com[2:]:
					var = arg.replace(",", "")
					self.vars_values[var] = int(input(f"{var}="))
			elif com[0] == "output":
				if com[1] != "->":
					raise SyntaxError("DSEMIL syntax is not valided.")
				for arg in com[2:]:
					var = arg.replace(",", "")
					print(f"{var}={self.vars_values[var]}")
			elif com[0] == "{":
				description = ""
				if com[-1] != "}":
					raise SyntaxError("DSEMIL syntax is not valided.")
				for x in com[1:-1]:
					description += x + ' '
				print(description)
			elif com[0] == "when":
				condition = self.dsemil_eval(com[1].replace(",", ""))
				if condition:
					self.vars_values[com[2].split("=")[0]] = self.dsemil_eval(com[2].split("=")[1])
			elif com[0].isalpha():
				if com[1] == "=":
					self.vars_values[com[0]] = self.dsemil_eval(com[2:])
if __name__ == '__main__':
	engine = DSEMILEngine(code)
	engine.run()