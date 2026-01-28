"""Pylint plugin for SQLAlchemy compatibility.

This plugin fixes false positives when using pylint with SQLAlchemy,
particularly for dynamically generated attributes like `func.count()`.
"""

from pylint_sqlalchemy2.func_callable import register_func_transforms

__version__ = "0.1.0"


def register(linter):
    """Register the plugin with pylint.

    Args:
        linter: The pylint linter instance.
    """
    register_func_transforms()
