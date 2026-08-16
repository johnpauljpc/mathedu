# MathEdu

A web-based math education tool for solving common secondary-school and
university-level math problems.

- **Secondary math:** simple & compound interest, quadratic equations, DDA line generation
- **University math:** root-finding for algebraic and transcendental equations (Bisection, Newton–Raphson, Successive Approximation) with step-by-step iteration tables

## Tech stack

- **Backend:** Django 5, class-based views
- **Math:** sympy (safe expression parsing), numpy, matplotlib (graph rendering)
- **Deployment:** Whitenoise (static), Gunicorn/WSGI

The math logic lives in `mathedu_core/` — a framework-free, pure-Python package
with no Django imports. It can be reused by a CLI, an API, or another web
framework, and is covered by unit tests.

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

### Configuration

All configuration is read from environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | dev-only fallback | Signing key. **Must** be set in production. |
| `DJANGO_DEBUG` | `false` | Enable/disable debug mode (`true`/`false`). |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,mathedu.pythonanywhere.com` | Comma-separated allowed hosts. |
| `DJANGO_LOG_LEVEL` | `INFO` | Root log level. |

Example:

```bash
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DJANGO_DEBUG=false
export DJANGO_ALLOWED_HOSTS="mathedu.pythonanywhere.com"
```

No database is required — the application is stateless.

## Running tests

```bash
# Core math package (pure Python, no Django needed)
python -m unittest discover -s mathedu_core

# Django view tests
python manage.py test
```

## Project structure

```
mathedu_core/          # pure-Python math library (no Django imports)
  expressions.py       # safe parsing of user equations (sympy, no eval)
  finance.py           # simple & compound interest
  algebra.py           # quadratic solver
  graphics.py          # DDA line algorithm
  roots/               # bisection, Newton–Raphson, successive approximation
  tests/               # unit tests
secondary_math/        # Django app: interest, quadratic, DDA
university_math/       # Django app: transcendental root-finding
templates/             # HTML templates (Bootstrap + custom themes)
static/                # CSS / JS / images
```

## Security

- User-supplied equations are parsed with **sympy**, never `eval()`. The parser
  runs with Python builtins removed and a whitelist of math functions, blocking
  code-injection attempts.
- `SECRET_KEY` comes from the environment, not the repository.
- Inputs are validated (intervals, tolerance, numeric coefficients) before use.