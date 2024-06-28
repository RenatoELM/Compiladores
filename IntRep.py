class IntRep:
    def __init__(self):
        self.stack = []
        self.tokens = []
        self.output = ""
        self.col_cont = 0

    def get_token(self):
        return self.tokens.pop()

    def markdown_open(self, token):
        if token.token_value == "h1":
            self.output += "# "
        if token.token_value == "h2":
            self.output += "## "
        if token.token_value == "h3":
            self.output += "### "
        if token.token_value == "p":
            self.output += "\n"
        if token.token_value == "b":
            self.output += " **"
        if token.token_value == "i":
            self.output += "*"
        if token.token_value == "ib":
            self.output += " ***"
        if token.token_value == "list":
            self.output += "\n"
        if token.token_value == "item":
            self.output += "- "
        if token.token_value == "url":
            self.output += "<"
        if token.token_value == "img":
            self.output += "![img]("
        if token.token_value == "table":
            self.output += "\n|"
        if token.token_value == "hr":
            self.col_cont = 0 
        if token.token_value == "r":
            self.output += "\n|"

    def markdown_close(self, token):
        if token.token_value == "h1":
            self.output += "\n"
        if token.token_value == "h2":
            self.output += "\n"
        if token.token_value == "h3":
            self.output += "\n"
        if token.token_value == "p":
            self.output += "\n"
        if token.token_value == "b":
            self.output += "** "
        if token.token_value == "i":
            self.output += "*"
        if token.token_value == "ib":
            self.output += "*** "
        if token.token_value == "list":
            self.output += "\n"
        if token.token_value == "item":
            self.output += "\n"
        if token.token_value == "url":
            self.output += "> "
        if token.token_value == "img":
            self.output += ")"
        if token.token_value == "table":
            self.output += "\n"
        if token.token_value == "hr":
            self.output += "\n|" + ("-|" * self.col_cont)
        if token.token_value == "c":
            self.col_cont += 1
            self.output += "|"

    def translate(self, tokens):
        self.tokens = tokens[::-1]
        self.stack.append(self.get_token())
        while len(self.tokens) > 0:
            if len(self.stack) == 0:
                return self.output

            curr_token = self.get_token()
            if self.stack[-1].token_value == curr_token.token_value:
                self.markdown_close(self.stack.pop())
            else:
                if curr_token.token_value == "text":
                    text = curr_token.token_name
                    text = text.rstrip()
                    text = text.lstrip()
                    self.output += text
                else:
                    self.markdown_open(curr_token)
                    self.stack.append(curr_token)

        return self.output