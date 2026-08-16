"""MathEdu core: framework-independent math logic.

Nothing in this package imports Django, so every module is testable in
isolation and reusable from a CLI, an API, or a different web framework.
"""

from . import algebra, expressions, finance, graphics, roots

__all__ = ["algebra", "expressions", "finance", "graphics", "roots"]