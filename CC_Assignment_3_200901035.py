import re
import ast

letters = []
numbers = []
punctuators = []
operators = []
others=[]

exp = str(input("Enter an expression: "))

lexicalAnalysis_tokens = re.findall(r"\d|\D", exp)
print(lexicalAnalysis_tokens)
for i in range(len(lexicalAnalysis_tokens)):
    if lexicalAnalysis_tokens[i].isalpha() == True:
        letters.append(lexicalAnalysis_tokens[i])
    elif lexicalAnalysis_tokens[i].isnumeric() == True:
        numbers.append(lexicalAnalysis_tokens[i])
    elif lexicalAnalysis_tokens[i] == '+' or lexicalAnalysis_tokens[i] == '-' or lexicalAnalysis_tokens[i] == '*' or lexicalAnalysis_tokens[i] == '/' or lexicalAnalysis_tokens[i] ==  '^' or lexicalAnalysis_tokens[i] == '|' or lexicalAnalysis_tokens[i] == '=':
        operators.append(lexicalAnalysis_tokens[i])
    elif lexicalAnalysis_tokens[i] == '(' or lexicalAnalysis_tokens[i] == ')' or lexicalAnalysis_tokens[i] == '{' or lexicalAnalysis_tokens[i] == '}' or lexicalAnalysis_tokens[i] == '[' or lexicalAnalysis_tokens[i] == ']' or lexicalAnalysis_tokens[i] == ';' or lexicalAnalysis_tokens[i] == ':' or lexicalAnalysis_tokens[i] == "'" or lexicalAnalysis_tokens[i] == '"':
        punctuators.append(lexicalAnalysis_tokens[i])
    elif lexicalAnalysis_tokens[i] == '!' or lexicalAnalysis_tokens[i] == '@' or lexicalAnalysis_tokens[i] == '#' or lexicalAnalysis_tokens[i] == '$' or lexicalAnalysis_tokens[i] == '%' or lexicalAnalysis_tokens[i] == '&' or lexicalAnalysis_tokens[i] == '_' or lexicalAnalysis_tokens[i] == '?' or lexicalAnalysis_tokens[i] == '<' or lexicalAnalysis_tokens[i] == '>':
        others.append(lexicalAnalysis_token[i])
print("Alphabets: ", letters)
print("Numbers: ", numbers)
print("Operators: ", operators)
print("Special Characters: ", others)
print("")
print("Syntax Analysis")
parsing = ast.parse(exp)
syntaxTree = ast.dump(parsing)
print(syntaxTree)
