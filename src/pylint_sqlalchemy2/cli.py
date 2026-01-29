"""CLI wrapper that runs pylint with pylint_sqlalchemy2 auto-loaded."""

import sys

from pylint import run_pylint


def main():
    """Run pylint with pylint_sqlalchemy2 plugin automatically loaded."""
    # Inject --load-plugins if not already specified
    args = sys.argv[1:]

    # Check if user already specified load-plugins
    has_load_plugins = any(
        arg.startswith("--load-plugins") for arg in args
    )

    if has_load_plugins:
        # Append our plugin to existing ones
        new_args = []
        for arg in args:
            if arg.startswith("--load-plugins="):
                arg = arg + ",pylint_sqlalchemy2"
            new_args.append(arg)
        args = new_args
    else:
        # Add our plugin
        args = ["--load-plugins=pylint_sqlalchemy2"] + args

    sys.argv = [sys.argv[0]] + args
    run_pylint()


if __name__ == "__main__":
    main()
