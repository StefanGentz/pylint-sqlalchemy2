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

## Known Limitations

### C0121: singleton-comparison

Pylint reports `singleton-comparison` (C0121) when comparing with `True`, `False`, or `None` using `==` instead of `is`:

```python
from sqlalchemy import select
from myapp.models import User

# Pylint reports: C0121: Comparison 'User.is_active == True' should be
# 'User.is_active is True' (singleton-comparison)
query = select(User).where(User.is_active == True)

# Pylint reports: C0121: Comparison 'User.deleted_at == None' should be
# 'User.deleted_at is None' (singleton-comparison)
query = select(User).where(User.deleted_at == None)
```

**Why this is a false positive:** In SQLAlchemy, `==` is the correct operator for column comparisons. It generates proper SQL (`WHERE is_active = TRUE`). Using `is True` or `is None` would not work as expected because it would use Python's identity comparison instead of SQLAlchemy's SQL generation.

**Workaround:** Disable `singleton-comparison` for your SQLAlchemy code. See [.pylintrc.example](.pylintrc.example) for a recommended configuration.

**Why this plugin doesn't fix it:** Unlike `func.*` callable issues (which can be fixed via type inference), `singleton-comparison` is a pure syntax check that cannot be suppressed programmatically without fragile hacks that would break on Pylint updates.

## Why not pylint-sqlalchemy?

The original [pylint-sqlalchemy](https://github.com/gwax/pylint-sqlalchemy) package is deprecated and doesn't handle `func.*` callable issues. This plugin is a modern replacement with automatic activation.

## License

[MIT License](https://github.com/StefanGentz/pylint-sqlalchemy2/blob/main/LICENSE "MIT License")

## Statistics

[ClickPy Stats](https://clickpy.clickhouse.com/dashboard/pylint-sqlalchemy2)
