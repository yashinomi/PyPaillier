import pathlib

from .encoded_message import EncodedMessage
from .utils import safe_random_below


class PublicKey:
    def __init__(self, n: int, g: int):
        self.n = n
        self.n2 = n ** 2
        self.g = g

    def encrypt(self, message: int) -> EncodedMessage:
        r = safe_random_below(self.n2, self.n)
        c = pow(self.g, message, self.n2)
        c *= pow(r, self.n, self.n2)
        c %= self.n2
        return EncodedMessage(c, self)

    def export_key(self, path):
        p = pathlib.Path(path)
        with open(p.resolve(), "w") as file:
            file.writelines(str(line) + "\n" for line in [self.n, self.g])

    @staticmethod
    def import_key(path):
        p = pathlib.Path(path)
        with open(p.resolve(), "r") as file:
            n, g = map(int, file.readlines())

        return PublicKey(n, g)