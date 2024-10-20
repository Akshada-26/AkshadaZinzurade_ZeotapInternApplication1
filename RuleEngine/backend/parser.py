from lark import Lark, Transformer, v_args
from lark.exceptions import UnexpectedToken, UnexpectedInput

# Grammar definition for the rule language
rule_grammar = """
    ?start: expression
    ?expression: or_expr
    ?or_expr: and_expr ("OR" and_expr)*
    ?and_expr: comparison ("AND" comparison)*
    ?comparison: operand operator operand
    operand: /\w+/
    operator: ">" | "<" | "==" | "!="
    %import common.WS
    %ignore WS
"""

# Transformer to convert the parsed tree into an AST
@v_args(inline=True)
class ASTTransformer(Transformer):
    def or_expr(self, *args):
        if len(args) == 1:
            return args[0]
        return {"type": "operator", "value": "OR", "left": args[0], "right": args[1]}

    def and_expr(self, *args):
        if len(args) == 1:
            return args[0]
        return {"type": "operator", "value": "AND", "left": args[0], "right": args[1]}

    def comparison(self, left, op, right):
        return {"type": "operand", "value": f"{left} {op} {right}"}

parser = Lark(rule_grammar, parser='lalr', transformer=ASTTransformer())

# Function to parse the rule string into an AST
def parse_rule(rule_string):
    try:
        return parser.parse(rule_string)
    except (UnexpectedToken, UnexpectedInput) as e:
        raise ValueError(f"Invalid rule syntax: {e}")

# Advanced algorithm to combine multiple ASTs
def combine_rules(rules_ast):
    if not rules_ast:
        return None

    combined = rules_ast[0]
    for rule_ast in rules_ast[1:]:
        combined = merge_asts(combined, rule_ast)

    return combined

# Simple merging logic for combining two ASTs
def merge_asts(ast1, ast2):
    return {"type": "operator", "value": "AND", "left": ast1, "right": ast2}
