from argparse import ArgumentParser

from .api import whych


def cli() -> None:
    parser = ArgumentParser()
    parser.add_argument("module", help="target Python module")
    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument(
        "-v", "--version", action="store_true", help="print module version"
    )
    command_group.add_argument(
        "-i", "--info", action="store_true", help="print module name, path, and version"
    )
    args = parser.parse_args()
    if args.info:
        query = "info"
    elif args.version:
        query = "version"
    else:
        query = "path"
    res = whych(module_name=args.module, query=query)
    print(res)
    if res is None:
        exit(1)


if __name__ == "__main__":
    cli()