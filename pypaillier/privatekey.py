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
