import ParserTable

class Parser:
    def __init__(self):
        self.grammar = ParserTable.grammar
        self.non_terminal = ParserTable.non_terminal
        self.terminal = ParserTable.terminal
        self.stack = []
        self.tokens = []
        self.errors = []

    def get_token(self):
        return self.tokens.pop()

    def parse_loop(self):
        token = self.get_token()
        self.stack.append("$")
        self.stack.append("Doc")
        while True:
            symbol = self.stack.pop()
            if symbol == '$' and token.token_value == '$':
                return
            if symbol in self.terminal:
                if token.token_value != symbol:
                    self.errors.append(f"ERROR terminal found at ({token.line}:{token.pos})")
                    while token.token_value != symbol:
                        if len(self.tokens) == 0:
                            return
                        token = self.get_token()
                token = self.get_token()
            if symbol in self.non_terminal:
                if token.token_value not in self.grammar[symbol]:
                    self.errors.append(f"ERROR non_terminal found at ({token.line}:{token.pos})")
                    while token.token_value not in self.grammar[symbol]:
                        if len(self.tokens) == 0:
                            return
                        token = self.get_token()
                self.stack.extend(self.grammar[symbol][token.token_value][::-1])

    def parse(self, tokens):
        self.tokens = tokens[::-1]
        self.parse_loop()
        for error in self.errors:
            print(error)
        return len(self.errors) == 0