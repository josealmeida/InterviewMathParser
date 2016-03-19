import argparse
import logging
import logging.config


class InterviewMathParser:

    def __init__(self):
        self.input = None
        self.tokens = []

        logging.config.fileConfig('logging.conf')
        self.logger = logging.getLogger('InterviewMathParser')

        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('input', help="input string expression", type=str)
        self.input = arg_parser.parse_args().input

    def prepare_tokens(self, input_string):
        """Creates a list of tokens from the input string
        :param input_string:
        """

        input_list = list(input_string)
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
        self.logger.debug(self.tokens)

if __name__ == '__main__':
    math_parser = InterviewMathParser()
    math_parser.prepare_tokens(math_parser.input)
