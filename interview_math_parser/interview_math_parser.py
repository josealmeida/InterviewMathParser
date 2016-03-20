import argparse
import logging
import logging.config
import os


class InterviewMathParser:
    """
    Implementation of a custom mathematical parser that takes a string
    expression and computes its numerical value.

    The parser implements an order of precedence of left to right.
    Brackets are used to explicitly denote precedence by grouping parts
    of an expression that should be evaluated first again left to right.

    Rules: a = '+', b = '-', c = '*', d = '/', e = '(', f = ')'
    """

    def __init__(self, expression_input=None):
        self.input = expression_input
        self.tokens = []
        self.sub_tokens = []
        self.current_token = None
        self.result = None

        logging.config.fileConfig(
            os.path.dirname(os.path.abspath(__file__)) +
            os.sep +
            'logging.conf')
        self.logger = logging.getLogger('InterviewMathParser')

        self.prepare_tokens()
        self.result = int(self.parse_expression())

    def prepare_tokens(self):
        """Creates a list of tokens from the input string
        """

        input_list = list(self.input)
        for i in range(len(input_list)):
            if i > 0:
                # appends sequential digits
                if input_list[i].isdigit() and self.tokens[-1].isdigit():
                    self.tokens[-1] += input_list[i]
                elif input_list[i] == 'a':
                    self.tokens.append('+')
                elif input_list[i] == 'b':
                    self.tokens.append('-')
                elif input_list[i] == 'c':
                    self.tokens.append('*')
                elif input_list[i] == 'd':
                    self.tokens.append('/')
                elif input_list[i] == 'e':
                    self.tokens.append('(')
                elif input_list[i] == 'f':
                    self.tokens.append(')')
                else:
                    self.tokens.append(input_list[i])
            else:
                self.tokens.append(input_list[i])

        self.sub_tokens = self.tokens
        self.current_token = self.tokens[0]
        self.logger.debug('tokens: {0}'.format(self.tokens))

    def parse_expression(self):
        """
        Parses an expression

        :return: the result of the expression calculation
        """
        result = self.term()
        while self.current_token in ('+', '-', '*', '/'):
            if self.current_token == '+':
                self.next_token()
                result += self.term()
            if self.current_token == '-':
                self.next_token()
                result -= self.term()
            if self.current_token == '*':
                self.next_token()
                result *= self.term()
            if self.current_token == '/':
                self.next_token()
                result /= self.term()
        return result

    def term(self):
        """
        Evaluates current token as term or expression with precedence

        :return: the current term or expression
        """
        result = None
        if self.current_token.isdigit():
            result = int(self.current_token)
            self.next_token()
        elif self.current_token is '(':
            self.next_token()
            result = self.parse_expression()
            self.next_token()
        return result

    def next_token(self):
        """
        Updates the current token
        """
        self.sub_tokens = self.sub_tokens[1:]
        self.current_token = self.sub_tokens[0] \
            if len(self.sub_tokens) > 0 \
            else None

if __name__ == '__main__':
    # If invoked from the command line
    # the parser takes the fist argument as input
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input', help="input string expression", type=str)
    arg_input = arg_parser.parse_args().input

    math_parser = InterviewMathParser(arg_input)
    print(math_parser.result)
