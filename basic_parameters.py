EQUALLY = '='
COLON = ':'
LEFT_BRACKET = '('
RIGHT_BRACKET = ')'
SEMICOLON = ';'
SIGN_MORE = '>'
SIGN_LESS = '<'
UNDERLINING = '_'

JSON_WHITESPACE = [' ', '\t', '\b', '\n', '\r']
KEYWORDS = ["for", "do"]
SEPARATORS = [SEMICOLON, LEFT_BRACKET, RIGHT_BRACKET, EQUALLY, SIGN_MORE, SIGN_LESS]
NUMBERS = [str(d) for d in range(0, 9)]

NAME = {
    '=': "EQUALLY",
    ':': "COLON",
    '(': "LEFT_BRACKET",
    ')': "RIGHT_BRACKET",
    ';': "SEMICOLON",
    '>': "SIGN_MORE",
    '<': "SIGN_LESS",
    '_': "UNDERLINING"
}
