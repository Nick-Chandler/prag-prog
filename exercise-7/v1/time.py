from parsimonious import Grammar, NodeVisitor

def create_tree(filename:str):
	
	with open(filename,"r") as f:
		grammar_raw = f.read()
		grammar = Grammar(grammar_raw)

	return grammar

class TimeVisitor(NodeVisitor):
			
	def visit_time_12(self,node,visited_children):
		hour,minutes,period = visited_children

		if minutes is None:
			minutes = 0

		minutes_past_midnight = hour%12 * 60 + minutes 

		if period == "pm":
			minutes_past_midnight += (12 * 60)

		return minutes_past_midnight

	def visit_time_24(self,node,visited_children):
		hours,minutes = visited_children
		return hours * 60 + minutes
				
	def visit_hour_12(self,node,visited_children):
		return int(node.text)

	def visit_hour_24(self,node,visited_children):
		return int(node.text)

	def visit_minutes_part(self,node,visited_children):
		minutes = node.text.split(":")[1]
		return int(minutes)
		
	def visit_period(self,node,visited_children):
		return node.text

	def generic_visit(self,node,visited_children):
		if len(visited_children) == 1:
			return visited_children[0]
		return

def minutes_after_midnight(time_str: str):
	tree = grammar.parse(time_str)
	minutes_after_midnight = TimeVisitor().visit(tree)
	return minutes_after_midnight

if __name__ == "__main__":
	filename = "time.peg"
	
	grammar = create_tree(filename)

	for t in ["4pm", "7:38pm", "23:42", "3:16", "3:16am"]:
		print(f"{t} -> {minutes_after_midnight(t)} minutes")
	
