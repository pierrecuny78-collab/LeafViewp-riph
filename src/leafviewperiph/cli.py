"""Small offline diagnostic CLI."""
from __future__ import annotations

import argparse

from leafviewperiph import __version__


def main() -> None:
    parser = argparse.ArgumentParser(prog="leafviewperiph")
    parser.add_argument("command", choices=("list", "version"), nargs="?", default="version")
    args = parser.parse_args()
    if args.command == "version":
        print(f"LeafViewpériph {__version__}")
    elif args.command == "list":
        print("No devices registered. Hardware discovery adapters are not installed yet.")


if __name__ == "__main__":
    main()
