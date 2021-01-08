import argparse
from typing import NoReturn

from pypaillier import KeyPair, PrivateKey, PublicKey


def comm_gen(args: argparse.Namespace):
    """
    Provides the action when sub command 'generate' is provided.

    Parameters
    ----------
    args
        command line arguments
    """
    keypair: KeyPair = KeyPair.generate_key_pair(args.length)
    keypair.export_keys(args.pk, args.sk)


def comm_enc(args: argparse.Namespace):
    """
    Provides the action when sub command 'encrypt' is provided.

    Parameters
    ----------
    args
        command line arguments
    """
    public_key: PublicKey = PublicKey.import_key(args.pk)
    if args.m:
        print(public_key.encrypt(args.m))
    else:
        message = input()
        while message != "exit":
            print(public_key.encrypt(int(message)))
            message = input()


def comm_dec(args: argparse.Namespace):
    """
    Provides the action when sub command 'decrypt' is provided.

    Parameters
    ----------
    args
        command line arguments
    """
    private_key: PrivateKey = PrivateKey.import_key(args.sk)
    if args.c:
        print(private_key.decrypt(args.c))
    else:
        message = input()
        while message != "exit":
            print(private_key.decrypt(int(message)))


def main() -> NoReturn:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="Paillier crypto system command line tool")
    command_parsers = parser.add_subparsers(
        title="sub command",
        description="a command what to do",
        required=True,
        help="Subcommands"
        )

    parser_gen = command_parsers.add_parser("generate", help="generates key pair")
    parser_gen.add_argument("-pk", type=str, required=True, help="path to save public key")
    parser_gen.add_argument("-sk", type=str, required=True, help="path to save private key")
    parser_gen.add_argument("-l", "--length", type=int, default=1024, help="key length")
    parser_gen.set_defaults(func=comm_gen)

    parser_enc = command_parsers.add_parser("encrypt", help="encrypts an integer with a public key")
    parser_enc.add_argument("-pk", type=str, required=True, help="path to the public key")
    parser_enc.add_argument("-m", type=int, help="message (integer) to encrypt")
    parser_enc.set_defaults(func=comm_enc)

    parser_dec = command_parsers.add_parser("decrypt", help="decrypts an encrypted message with a secret key")
    parser_dec.add_argument("-sk", type=str, required=True, help="path to the private key")
    parser_dec.add_argument("-c", type=int, help="encrypted message (integer) to decrypt")
    parser_dec.set_defaults(func=comm_dec)

    args = parser.parse_args()
    # calls the appropriate function
    args.func(args)


if __name__ == '__main__':
    main()
