from constants import *
import global_variables as g
from LexicalAnalyzer import *
from ExecutingProgram import * 
from ActivationRecord import *
class ParsingProgram:
    def __init__(self):
        self.function_names = []
        self.local_variables = []

        self.lexical_analyzer = LexicalAnalyzer()

    def statement(self):
        # print("Enter <statement>")
        if g.next_token == CALL:
            self.lexical_analyzer.lexical()

            if g.next_token == IDENT :
                self.lexical_analyzer.lexical()
                if g.next_token == SEMI_COLON:
                    self.lexical_analyzer.lexical()
                else:
                    print("\"Syntax Error.\"")
                    exit()
            else:
                print("\"Syntax Error.\"")
                exit()
        elif g.next_token == PRINT_ARI or  g.next_token == IDENT:
            self.lexical_analyzer.lexical()
            if g.next_token == SEMI_COLON:
                self.lexical_analyzer.lexical()
            else:
                print("\"Syntax Error.\"")
                exit()
        else:
            print("\"Syntax Error.\"")
            exit()
        self.line_number = 0 
        # print("Exit <statement>")

    def statements(self):
        # print("Enter <statements>")
        while g.next_token == CALL or  g.next_token == PRINT_ARI or g.next_token == IDENT:
            self.statement()
        # print("Exit <statements>")
        
    def var_list(self):
        # print("Enter <var_list>")
        # print("!!!!!!",g.token_string)
        if g.token_string in self.local_variables:
            print("\"Duplicate declaration of the identifier:",g.token_string+"\"")
        else:
            self.local_variables.append(g.token_string)
        if g.next_token == IDENT:
            self.lexical_analyzer.lexical()
            while g.next_token == COMMA:
                self.lexical_analyzer.lexical()
                # print("!!!!!!!!!",g.token_string)
                if g.token_string in self.local_variables:
                    print("\"Duplicate declaration of the identifier:",g.token_string+"\"")
                else:
                    self.local_variables.append(g.token_string)
                if g.next_token == IDENT:
                    self.lexical_analyzer.lexical()
                else:
                    print("\"Syntax Error.\"")
                    exit()
        else:
            print("\"Syntax Error.\"")
            exit()
        # print("Exit <var_list>")

    def var_definition(self):
        # print("Enter <var_definition>")
        if g.next_token == VARIABLE:
            self.lexical_analyzer.lexical()
            self.var_list()
            if g.next_token == SEMI_COLON:
                self.lexical_analyzer.lexical()
            else:
                print("\"Syntax Error.\"")
                exit()
        else:
            print("\"Syntax Error.\"")
            exit()
        # print("Exit <var_definition>")

    def var_definitions(self):
        # print("Enter <var_definitions>")
        self.var_definition()
        while g.next_token == VARIABLE:
            self.lexical_analyzer.lexical()
            self.var_definition()
        # print("Exit <var_definitions>")

    def function_body(self):
        # print("Enter <function_body>")
        self.local_variables = []
        if g.next_token == VARIABLE:
            self.var_definitions()
            self.statements()
        elif g.next_token == CALL or g.next_token == PRINT_ARI or g.next_token == IDENT:
            self.statements()
        else:
            print("\"Syntax Error.\"")
            exit()
        # print("LOCAL_VARIABLES", self.local_variables)
        # print("Exit <function_body>")

    def function(self):
        # print("Enter <function>")
        if g.next_token == IDENT:
            # print("!!!!!!!!!!",g.token_string)
            if g.token_string in self.function_names:
                print("\"Duplicate declaration of the function name:",g.token_string+"\"")
                exit()
            self.function_names.append(g.token_string)
            self.lexical_analyzer.lexical()
            if g.next_token == LEFT_BRACE:
                self.lexical_analyzer.lexical()
                self.function_body()
                if g.next_token == RIGHT_BRACE:
                    self.lexical_analyzer.lexical()
                else:
                    print("\"Syntax Error.\"")
                    exit()
            else:
                print("\"Syntax Error.\"")
                exit()
        else:
            print("\"Syntax Error.\"")
            exit()
        # print("Exit <function>")

    def functions(self):
        # print("Enter <functions>")
        self.function()

        while g.next_token == IDENT:
            self.function()
        if g.next_token != EOF:
            print("\"Syntax Error.\"")
            exit()
        # print("Exit <functions>")

    def start(self):
        # print("Enter <start>")
        self.functions()
        # print(self.function_names)
        if "main" not in self.function_names:
            print("No starting function.")
        else:
            print("\"Syntax O.K.\"")
            g.function_names = self.function_names
            # executer = ExecutingProgram()
            # executer.start()
        # print("Exit <start>")
