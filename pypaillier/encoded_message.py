from .publickey import PublicKey

class EncodedMessage:
    def __init__(self, message, public_key: PublicKey):
        self.m = message
        self.n = public_key.n
        self.n2 = public_key.n2

    def __add__(self, other) -> "EncodedMessage":
        if not isinstance(other, EncodedMessage):
            raise TypeError("Addition is only supported between EncodedMessage")

        return EncodedMessage(self.m * other.m % self.n2)

    def __mul__(self, other) -> "EncodedMessage":
        if type(other) is not int:
            raise TypeError("Multiplication is only supported with integer")

        return EncodedMessage(self.m ** other % self.n2)

    def __int__(self) -> int:
        return self.m

    def __str__(self) -> str:
        return str(self.m)