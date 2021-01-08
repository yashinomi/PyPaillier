import pathlib

from .encoded_message import EncodedMessage
from .utils import lcm, mod_inv

class PrivateKey:
    def __init__(self, p: int, q: int, g: int):
        self.p = p
        self.q = q
        self.n = p * q
        self.n2 = self.n ** 2

        self.l = lcm(p - 1, q - 1)
        self.L_div = mod_inv(self._L(pow(g, self.l, self.n2)), self.n)

    def _L(self, x) -> int:
        return (x - 1) // self.n % self.n

    def decrypt(self, encrypted_message: EncodedMessage) -> int:
        plain_m: int = int(encrypted_message)
        return self._L(pow(plain_m, self.l, self.n2)) * self.L_div % self.n

    def export_key(self, path):
        p = pathlib.Path(path)
        with open(p.resolve(), "w") as file:
            file.writelines(str(line) + "\n" for line in [self.p, self.q, self.g])

    @staticmethod
    def import_key(path):
        p = pathlib.Path(path)
        with open(p.resolve(), "r") as file:
            p, q, g = map(int, file.readlines())

        return PrivateKey(p, q, g)