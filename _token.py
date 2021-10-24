class Token:
    def __init__(self, key: str, value: str) -> None:
        self.__key = key
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @property
    def value(self) -> str:
        return self.__value
