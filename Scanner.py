from ParserTable import keywords
from class_token import Token
from TokenType import TokenType

class Scanner:
    def __init__(self):
        self.code = ""
        self.pointer = 0
        self.debug = False
        self.keywords = keywords
        self.cur_line = 1
        self.cur_pos = 0

    def read_code_file(self, filename, extension="txt"):
        with open(f"{filename}.{extension}", mode="r", encoding="utf-8") as file:
            self.code = file.read()

    def peek_char(self):
        return self.code[self.pointer]

    def get_char(self):
        char = self.peek_char()
        self.update_debug_data(char)
        self.pointer += 1
        return char

    def update_debug_data(self, char):
        self.cur_pos += 1
        if char == '\n':
            self.cur_line += 1
            self.cur_pos = 0

    def get_token(self):
        cur_char = self.get_char()

        while cur_char in [' ', '\n', '\t']:
            cur_char = self.get_char()

        if cur_char == '#':
            return self.get_comment()

        if cur_char == '$':
            return Token(TokenType.END, '$', "end.", self.cur_line, self.cur_pos)

        if cur_char == '<':
            return self.get_tag()

        return self.get_text(cur_char)

    def get_comment(self):
        comment = ""
        cur_char = self.get_char()
        while cur_char != '\n':
            comment += cur_char
            cur_char = self.get_char()
        return Token(TokenType.COMMENT, "", f"\"{comment}\"", self.cur_line, self.cur_pos)

    def get_tag(self):
        keyword = ""
        cur_char = self.get_char()
        while cur_char != '>':
            if cur_char in [' ', '\n', '\t']:
                return Token(TokenType.ERROR, "Invalid tag name.", "Invalid tag name.", self.cur_line, self.cur_pos)
            keyword += cur_char
            cur_char = self.get_char()

        if keyword not in self.keywords:
            return Token(TokenType.ERROR, "Invalid tag name.", "Invalid tag name.", self.cur_line, self.cur_pos)

        return Token(TokenType.TAG, keyword, f"<{keyword}>", self.cur_line, self.cur_pos)

    def get_text(self, cur_char):
        text = cur_char
        while self.peek_char() not in ['<', '>', '#', '\n']:
            cur_char = self.get_char()
            text += cur_char
        return Token(TokenType.TEXT, "text", f"{text}", self.cur_line, self.cur_pos)

    def scan(self, filename, debug=False):
        self.code = ""
        self.pointer = 0
        self.debug = debug
        self.read_code_file(filename)
        self.code += "\n$"

        tokens = []

        self.debug_print("INFO SCAN - Start scanning…")
        while True:
            cur_token = self.get_token()
            self.debug_print(f"DEBUG SCAN - {cur_token.token_type} {cur_token.token_name} found at ({cur_token.line}:{cur_token.pos})")
            if cur_token.token_type != TokenType.COMMENT:
                tokens.append(cur_token)

            if cur_token.token_type == TokenType.END:
                self.debug_print("INFO SCAN - Completed with 0 errors")
                return tokens

            if cur_token.token_type == TokenType.ERROR:
                self.debug_print("INFO SCAN - Error")
                return tokens

    def debug_print(self, message):
        if self.debug:
            print(message)