class Token:
    def __init__(self, token_type, token_value, token_name, line, pos):
        self.token_type = token_type
        self.token_value = token_value
        self.token_name = token_name
        self.line = line
        self.pos = pos