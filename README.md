# pylint-sqlalchemy2

A Pylint plugin for SQLAlchemy 2.x compatibility. **Install and forget!**

Fixes false positive errors when using Pylint with SQLAlchemy, particularly for dynamically generated SQL functions like `func.count()`, `func.sum()`, `func.max()`, etc.

## Installation

```bash
pip install pylint-sqlalchemy2
```

**That's it!** The plugin activates automatically. No configuration needed.

See also: [pylint-sqlalchemy2 on PyPI](https://pypi.org/project/pylint-sqlalchemy2/)

## What it fixes

### E1102: not-callable for `func.*`

SQLAlchemy's `func` object dynamically generates SQL function calls. Pylint cannot analyze this and reports false positives:

```python
from sqlalchemy import func, select

# Without this plugin, pylint reports:
# E1102: func.count is not callable (not-callable)
query = select(func.count()).select_from(User)
```

This plugin teaches Pylint that `func.count()`, `func.sum()`, `func.max()`, and all other `func.*` attributes are callable.

## How it works

The plugin uses a `.pth` file to automatically register Astroid transforms when Python starts. This means it works without any configuration - just install and run pylint as usual.

## Alternative usage

If you prefer explicit configuration, you can also use:

**Command line:**

```bash
pylint --load-plugins=pylint_sqlalchemy2 your_code.py
```

**pylintrc or pyproject.toml:**

```ini
[MASTER]
load-plugins=pylint_sqlalchemy2
```

## Compatibility

- Python 3.9+
- Pylint 3.0+
- Astroid 3.0+
- SQLAlchemy 1.4+ / 2.x

## Why not pylint-sqlalchemy?

The original [pylint-sqlalchemy](https://github.com/gwax/pylint-sqlalchemy) package is deprecated and doesn't handle `func.*` callable issues. This plugin is a modern replacement with automatic activation.

## License

[MIT License](https://github.com/StefanGentz/pylint-sqlalchemy2/blob/main/LICENSE "MIT License")
