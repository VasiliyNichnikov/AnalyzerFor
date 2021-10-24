from typing import List

from _token import Token
from basic_parameters import *
from states import States


class Lexer:
    __info: str = ""

    def __init__(self, info: str) -> None:
        self.__info: str = info
        self.__description_error: str = ""
        self.__state = States.H
        self.__tokens: List[Token] = []

    @property
    def tokens(self) -> List[Token]:
        return self.__tokens.copy()

    def run(self) -> None:
        while len(self.__info):
            match self.__state:
                case States.H:
                    self.__check_state_h()

                case States.ID:
                    _id = self.__check_state_id()
                    if _id is not None:
                        self.__tokens.append(_id)

                case States.NM:
                    nm = self.__check_state_nm()
                    if nm is not None:
                        self.__tokens.append(nm)

                case States.ASGN:
                    asgn = self.__check_state_asgn()
                    if asgn is not None:
                        self.__tokens.append(asgn)

                case States.DLM:
                    dlm = self.__check_state_dlm()
                    if dlm is not None:
                        self.__tokens.append(dlm)

                case States.ERR:
                    self.__check_state_err()
                    return

    def __check_state_h(self) -> None:
        while self.__info[0] in JSON_WHITESPACE:
            self.__info = self.__info[1:]

        if self.__info[0] == COLON:
            self.__info = self.__info[1:]
            self.__state = States.ASGN
            return

        elif self.__info[0] == UNDERLINING or self.__info[0].isalpha():
            self.__state = States.ID
            return

        elif self.__info[0] in NUMBERS + ['-', '+', '.']:
            self.__state = States.NM
            return

        else:
            self.__state = States.DLM
            return

    def __check_state_asgn(self) -> Token | None:
        if self.__info[0] == EQUALLY:
            self.__info = self.__info[1:]
            self.__state = States.H
            return Token("ASSIGNMENT", ":=")
        else:
            self.__description_error = f"(ASGN) Unknown character ({self.__info[0]}) when processing ASGN."
            self.__state = States.ERR
            return None

    def __check_state_id(self) -> Token:
        value: str = ""
        while self.__info[0] in [UNDERLINING] + NUMBERS or self.__info[0].isalpha():
            value += self.__info[0]
            self.__info = self.__info[1:]
        self.__state = States.H
        if value in KEYWORDS:
            return Token("KEYWORD", value)
        return Token("ID", value)

    def __check_state_nm(self) -> Token | None:
        value: str = ""
        while self.__info[0] in NUMBERS + ['-', '+', '.']:
            value += self.__info[0]
            self.__info = self.__info[1:]

        if self.__is_digit(value):
            self.__state = States.H
            return Token("NUMBER", value)
        self.__description_error = f"(NM) The resulting value ({value}) is not a number."
        self.__state = States.ERR
        return None

    @staticmethod
    def __is_digit(value) -> bool:
        if value.isdigit():
            return True
        else:
            try:
                float(value)
                return True
            except ValueError:
                return False

    def __check_state_dlm(self) -> Token | None:
        value: str = ""
        value += self.__info[0]
        self.__info = self.__info[1:]
        if value in SEPARATORS:
            self.__state = States.H
            return Token("DLM", value)
        self.__description_error = f"(DLM) The symbol ({value}) is not a separator."
        self.__state = States.ERR
        return None

    def __check_state_err(self) -> None:
        print(f"Error: {self.__description_error}")
