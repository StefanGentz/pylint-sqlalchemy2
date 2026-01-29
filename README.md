# pylint-sqlalchemy2

A modern Pylint plugin for SQLAlchemy 2.x compatibility.

Fixes false positive errors when using Pylint with SQLAlchemy, particularly for dynamically generated SQL functions like `func.count()`, `func.sum()`, `func.max()`, etc.

## Installation

```bash
pip install pylint-sqlalchemy2
```

Or install from GitHub:

```bash
pip install git+https://github.com/StefanGentz/pylint-sqlalchemy2.git
```

See also: [pylint-sqlalchemy2 on PyPi](https://pypi.org/project/pylint-sqlalchemy2/)

## Usage

Add the plugin to your `.pylintrc`:

```ini
[MASTER]
load-plugins=pylint_sqlalchemy2
```

Or use it via command line:

```bash
pylint --load-plugins=pylint_sqlalchemy2 your_module.py
```

## What it fixes

### E1102: not-callable for `func.*`

SQLAlchemy's `func` object dynamically generates SQL function calls. Pylint cannot analyze this and reports false positives:

```python
from sqlalchemy import func, select
from sqlalchemy.orm import Session

# Without this plugin, pylint reports:
# E1102: func.count is not callable (not-callable)
query = select(func.count()).select_from(User)
```

This plugin teaches Pylint that `func.count()`, `func.sum()`, `func.max()`, and all other `func.*` attributes are callable.

## Compatibility

- Python 3.9+
- Pylint 3.0+
- Astroid 3.0+
- SQLAlchemy 1.4+ / 2.x

## Why not pylint-sqlalchemy?

The original [pylint-sqlalchemy](https://github.com/gwax/pylint-sqlalchemy) package is deprecated and doesn't handle `func.*` callable issues. This plugin is a modern replacement focused on SQLAlchemy 2.x compatibility.

## License

MIT License
