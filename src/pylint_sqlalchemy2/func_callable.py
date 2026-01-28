"""Fix for SQLAlchemy's func module false positives.

SQLAlchemy's `func` object dynamically generates SQL function calls like
`func.count()`, `func.sum()`, `func.max()`, etc. Pylint cannot analyze
this dynamic behavior and reports E1102 (not-callable) errors.

This module registers an Astroid brain to tell pylint that any attribute
access on `sqlalchemy.sql.functions.func` returns a callable.
"""

import astroid
from astroid import MANAGER


FUNC_MODULE_CODE = """
class _FunctionGenerator:
    '''Represents sqlalchemy.sql.functions.func.'''

    def __getattr__(self, name: str) -> '_GenericFunction':
        '''Return a callable function generator for any attribute.'''
        ...

    def __call__(self, *args, **kwargs):
        '''Make the function generator itself callable.'''
        ...


class _GenericFunction:
    '''Represents a SQLAlchemy SQL function like count(), sum(), etc.'''

    def __call__(self, *args, **kwargs):
        '''SQL functions are callable.'''
        ...

    def __getattr__(self, name: str) -> '_GenericFunction':
        '''Allow chaining like func.array_agg.filter().'''
        ...


func = _FunctionGenerator()
"""


def _transform_func_module(module):
    """Transform the sqlalchemy.sql.functions module.

    Adds type information so pylint knows `func` attributes are callable.
    """
    if module.name == "sqlalchemy.sql.functions":
        fake_module = astroid.parse(FUNC_MODULE_CODE)
        for node in fake_module.body:
            if isinstance(node, astroid.ClassDef):
                module.locals[node.name] = [node]
            elif isinstance(node, astroid.Assign):
                for target in node.targets:
                    if isinstance(target, astroid.AssignName):
                        module.locals[target.name] = [node.value]


def register_func_transforms():
    """Register Astroid transforms for SQLAlchemy func module."""
    MANAGER.register_transform(astroid.Module, _transform_func_module)
