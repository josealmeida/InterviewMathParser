import unittest
from interview_math_parser.interview_math_parser import InterviewMathParser


class TestInterviewMathParser(unittest.TestCase):

    def test_input_1(self):
        math_parser_1 = InterviewMathParser('3a2c4')
        self.assertEqual(math_parser_1.result, 20)

    def test_input_2(self):
        math_parser_2 = InterviewMathParser('32a2d2')
        self.assertEqual(math_parser_2.result, 17)

    def test_input_3(self):
        math_parser_3 = InterviewMathParser('500a10b66c32')
        self.assertEqual(math_parser_3.result, 14208)

    def test_input_4(self):
        math_parser_4 = InterviewMathParser('3ae4c66fb32')
        self.assertEqual(math_parser_4.result, 235)

    def test_input_5(self):
        math_parser_1 = InterviewMathParser('3c4d2aee2a4c41fc4f')
        self.assertEqual(math_parser_1.result, 990)

if __name__ == '__main__':
    unittest.main()
