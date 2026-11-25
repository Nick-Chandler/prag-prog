from pathlib import Path
from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar(Path(__file__).with_name("time.peg").read_text())


class TimeVisitor(NodeVisitor):
  def visit_time(self, node, children):
    return children[0]

  def visit_time12_long(self, node, children):
    hour, _, minute, ampm = children
    return to_24(hour, ampm) * 60 + minute

  def visit_time12_short(self, node, children):
    hour, ampm = children
    return to_24(hour, ampm) * 60

  def visit_time24(self, node, children):
    hour, _, minute = children
    return hour * 60 + minute

  def visit_hour12(self, node, children):
    return int(node.text)

  def visit_hour24(self, node, children):
    return int(node.text)

  def visit_minute(self, node, children):
    return int(node.text)

  def visit_ampm(self, node, children):
    return node.text

  def generic_visit(self, node, children):
    return children or node


def to_24(hour, ampm):
  return hour % 12 + (12 if ampm == "pm" else 0)


def minutes_past_midnight(text):
  return TimeVisitor().visit(grammar.parse(text))


if __name__ == "__main__":
  for t in ["4pm", "7:38pm", "23:42", "3:16", "3:16am"]:
    print(f"{t:>7} -> {minutes_past_midnight(t)}")
