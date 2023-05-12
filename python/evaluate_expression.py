"""
You are given a string representing a mathematical expression with integers, parentheses, and the four arithmetic operations (+, -, *, /). Write a program that evaluates the expression.

For example, if the input string is "3+4*5-(6/2)", the program should return 17.

Assume that the input string is well-formed and contains only valid characters.
"""

from typing import List
import unittest

def evaluate_expression(expression: str) -> int:
    stack: List = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = int(expression[i])
            j = i + 1
            while j < len(expression) and expression[j].isdigit():
                num = num * 10 + int(expression[j])
                j += 1
            stack.append(num)
            i = j
        elif expression[i] in "+-*/":
            if len(stack) < 2:
                raise ValueError("Invalid input string")      
            op = expression[i]
            b = stack.pop()
            a = stack.pop()
            if op == "+":
                stack.append(a + b)
            elif op == "-":
                stack.append(a - b)
            elif op == "*":
                stack.append(a * b)
            elif op == "/":
                stack.append(a // b)
            i += 1
        elif expression[i] == "(":
            stack.append(expression[i])
            i += 1
        elif expression[i] == ")":
            while stack[-1] != "(":
                if len(stack) < 3:
                    raise ValueError("Mismatched parentheses")
                b = stack.pop()
                op = stack.pop()
                a = stack.pop()
                if op == "+":
                    stack.append(a + b)
                elif op == "-":
                    stack.append(a - b)
                elif op == "*":
                    stack.append(a * b)
                elif op == "/":
                    stack.append(a // b)
            stack.pop()
            i += 1
        else:
            i += 1
    return stack[0]

class TestEvaluateExpression(unittest.TestCase):
    def test_evaluate_expression(self):
        expression = "1+2*(3*4+5"
        with self.assertRaises(ValueError):
            evaluate_expression(expression)

        expression = "1+2*(3*4+5))"
        with self.assertRaises(ValueError):
            evaluate_expression(expression)

        expression = "1+2*(3*4+5)+"
        with self.assertRaises(ValueError):
            evaluate_expression(expression)



if __name__ == "__main__":
    unittest.main()