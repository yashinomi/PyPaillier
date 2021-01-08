import unittest

from pypaillier import KeyPair, PrivateKey, PublicKey


class TestPaillierEncryption(unittest.TestCase):
    def test_enc_to_dec(self):
        print("simple")
        keys: KeyPair = KeyPair(PublicKey(35, 386), PrivateKey(5, 7, 386))
        message: int = 3
        self.assertEqual(message, keys.sk.decrypt(keys.pk.encrypt(message)))
        message = 10
        self.assertEqual(message, keys.sk.decrypt(keys.pk.encrypt(message)))

        print("hard")
        keys: KeyPair = KeyPair(PublicKey(11639, 23279), PrivateKey(103, 113, 23279))
        message: int = 3
        self.assertEqual(message, keys.sk.decrypt(keys.pk.encrypt(message)))
        message = 10
        self.assertEqual(message, keys.sk.decrypt(keys.pk.encrypt(message)))

        print("complicated")
        keys = KeyPair.generate_key_pair(1024)
        print("keygen done")
        message: int = 3
        self.assertEqual(message, keys.sk.decrypt(keys.pk.encrypt(message)))

    def test_export_to_import(self):
        keys: KeyPair = KeyPair(PublicKey(11639, 23279), PrivateKey(103, 113, 23279))
        keys.export_keys("./dummy.pub", "./dummy.secret")
        imported_keys = KeyPair.import_keys("./dummy.pub", "./dummy.secret")
        self.assertEqual(keys, imported_keys)

    def test_addition(self):
        keys: KeyPair = KeyPair(PublicKey(35, 386), PrivateKey(5, 7, 386))
        message1, message2 = 3, 5  # type: int, int
        self.assertEqual(
            (message1 + message2) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message1) + keys.pk.encrypt(message2))
            )
        message1, message2 = 10, 15
        self.assertEqual(
            (message1 + message2) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message1) + keys.pk.encrypt(message2))
        )

        keys: KeyPair = KeyPair(PublicKey(11639, 23279), PrivateKey(103, 113, 23279))
        message1, message2 = 3, 5  # type: int, int
        self.assertEqual(
            (message1 + message2) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message1) + keys.pk.encrypt(message2))
        )
        message1, message2 = 100, 515
        self.assertEqual(
            (message1 + message2) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message1) + keys.pk.encrypt(message2))
        )

        keys = KeyPair.generate_key_pair(1024)
        message1, message2 = 100, 515
        self.assertEqual(
            (message1 + message2) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message1) + keys.pk.encrypt(message2))
        )

    def test_multiplication(self):
        keys: KeyPair = KeyPair(PublicKey(35, 386), PrivateKey(5, 7, 386))
        message, multiplier = 3, 5  # type: int, int
        self.assertEqual(
            (message * multiplier) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message) * multiplier)
            )
        message, multiplier = 10, 11
        self.assertEqual(
            (message * multiplier) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message) * multiplier)
        )

        keys: KeyPair = KeyPair(PublicKey(11639, 23279), PrivateKey(103, 113, 23279))
        message, multiplier = 3, 5
        self.assertEqual(
            (message * multiplier) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message) * multiplier)
        )
        message, multiplier = 100, 515
        self.assertEqual(
            (message * multiplier) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message) * multiplier)
        )

        keys = KeyPair.generate_key_pair(1024)
        message1, message2 = 100, 515
        self.assertEqual(
            (message1 + message2) % keys.pk.n,
            keys.sk.decrypt(keys.pk.encrypt(message1) + keys.pk.encrypt(message2))
        )


if __name__ == '__main__':
    unittest.main()
