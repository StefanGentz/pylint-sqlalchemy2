"""Pylint plugin for SQLAlchemy compatibility.

This plugin fixes false positives when using pylint with SQLAlchemy,
particularly for dynamically generated attributes like `func.count()`.

The transforms are registered automatically when this module is imported,
enabling "install and forget" usage.
"""

from pylint_sqlalchemy2.func_callable import register_func_transforms

__version__ = "0.2.0"

# Register transforms immediately on import (not just when register() is called)
# This enables automatic registration via .pth file
register_func_transforms()


def register(linter):
    """Register the plugin with pylint.

    This function is called by pylint when using --load-plugins.
    The transforms are already registered on module import, so this
    is a no-op but required for pylint plugin compatibility.

    Args:
        linter: The pylint linter instance.
    """
    pass  # Transforms already registered on import
