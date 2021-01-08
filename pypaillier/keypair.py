import Crypto.PublicKey.RSA

from .utils import safe_random_below
from .publickey import PublicKey
from .privatekey import PrivateKey


class KeyPair:
    """
    Provides an interface to manage a private key and its public key.

    Parameters
    ----------
    public_key : PublicKey
    private_key : PrivateKey
    """
    def __init__(self, public_key: PublicKey, private_key: PrivateKey):
        if not isinstance(public_key, PublicKey) or not isinstance(private_key, PrivateKey):
            raise TypeError("public_key must be an instance of PublicKey and "
                            "private_key must be an instance of PrivateKey")

        self.public_key: PublicKey = public_key
        self.private_key: PrivateKey = private_key

    def __eq__(self, other) -> bool:
        if not isinstance(other, KeyPair):
            return False
        elif self.public_key == other.public_key and self.private_key == other.private_key:
            return True
        else:
            return False

    @staticmethod
    def generate_key_pair(key_length: int) -> "KeyPair":
        """
        Generates a pair of private key and its public key.

        Parameters
        ----------
        key_length : int
            The bit length of the key that is going to be generated.

        Returns
        -------
        KeyPair
            An instance of KeyPair including a private key and its public key.
        """
        # generate prime numbers by using the crypto module.
        rsa: Crypto.PublicKey.RSA.RsaKey = Crypto.PublicKey.RSA.generate(key_length)

        n: int = rsa.n
        p: int = rsa.p
        q: int = rsa.q

        k: int = safe_random_below(n ** 2, n)
        g: int = (1 + k * n) % (n ** 2)

        return KeyPair(PublicKey(n, g), PrivateKey(p, q, g))

    def export_keys(self, pub_path: str, private_path: str):
        self.public_key.export_key(pub_path)
        self.private_key.export_key(private_path)

    @staticmethod
    def import_keys(pub_path, private_path) -> "KeyPair":
        pub_key: PublicKey = PublicKey.import_key(pub_path)
        private_key: PrivateKey = PrivateKey.import_key(private_path)

        return KeyPair(pub_key, private_key)
