import shlex

def _safe_split(string: str, delim: str = " ") -> list[str]:
    if delim == " ":
        return shlex.split(string)
    
    lexer = shlex.shlex(string, posix=True)
    lexer.whitespace = delim
    lexer.whitespace_split = True
    return list(lexer)

    

