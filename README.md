# MathEdu

A web-based math education tool that solves common secondary-school and
university-level math problems with step-by-step working.

Live at: `mathedu.pythonanywhere.com` _(planned)_

## Features

- **Simple & compound interest** — amount, interest, and breakdown for any rate, time, and compounding frequency
- **Quadratic equations** — real and complex roots, discriminant analysis
- **DDA line generation** — digitized line points with a table of `x`, `y`, and error terms
- **Transcendental root-finding** — Bisection, Newton–Raphson, and Successive Approximation with full iteration tables
- **Responsive dual-theme UI** — mobile-first, dark/light themes (respects your system preference, persisted in `localStorage`)

## Why it stands out

- **Security-first parsing** — user equations are parsed with sympy's restricted
  parser, never `eval()`. Builtins are removed and only a whitelist of math
  functions is allowed, blocking code-injection attempts. Verified against
  `os.system()`, `__import__('os')`, and `eval()` payloads.
- **Framework-free core** — all math lives in `mathedu_core/`, a pure-Python
  package with zero Django imports. It's unit-tested in isolation and reusable
  from a CLI, API, or any framework.
- **Tested** — 29 core tests + 42 view tests, all passing.
- **Stateless architecture** — no database, no sessions; every request is
  self-contained and cheap to host.

## Tech stack

- **Backend:** Django 5, class-based views
- **Math:** sympy (safe expression parsing), numpy
- **Config:** python-decouple (`.env` or environment variables)
- **Frontend:** Bootstrap 5, custom CSS design system with CSS variables
- **Deployment:** Whitenoise (static files), WSGI (Gunicorn / PythonAnywhere)

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Optional: create a local .env
cp .env.example .env

python manage.py runserver
```

Then open http://127.0.0.1:8000.

## Configuration

Settings are read with **python-decouple** from a `.env` file (git-ignored) or
from real environment variables. `.env` values take precedence.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | dev-only fallback | Signing key. **Must** be set to a real random value in production. |
| `DJANGO_DEBUG` | `false` | Enable/disable debug mode (`true`/`false`). |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,mathedu.pythonanywhere.com` | Comma-separated allowed hosts. |
| `DJANGO_LOG_LEVEL` | `INFO` | Root log level. |

Generate a real secret key:

```bash
python -c 'import secrets; print(secrets.token_urlsafe(48))'
```

No database is required — the application is intentionally stateless.

## Running tests

```bash
# Core math package (pure Python, no Django needed)
python -m unittest discover -s mathedu_core

# Django view tests
python manage.py test
```

## Deployment on PythonAnywhere

1. Push this repo to GitHub, then in a PythonAnywhere Bash console:
   ```bash
   git clone https://github.com/<you>/mathedu.git
   cd mathedu
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Create a `.env` file (or set the values in the WSGI file on the **Web tab**):
   ```
   DJANGO_SECRET_KEY=<your generated key>
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=mathedu.pythonanywhere.com
   ```
3. Collect static files: `python manage.py collectstatic --noinput`
4. On the **Web tab**: point the WSGI file at `mathedu.wsgi`, add `mathedu` and its
   `.venv` to `sys.path`, then hit **Reload**.

## Project structure

```
mathedu_core/          # pure-Python math library (no Django imports)
  expressions.py       # safe parsing of user equations (sympy, no eval)
  finance.py           # simple & compound interest
  algebra.py           # quadratic solver
  graphics.py          # DDA line algorithm
  roots/               # bisection, Newton–Raphson, successive approximation
  tests/               # unit tests
mathedu/               # Django project (settings, urls, wsgi)
secondary_math/        # Django app: interest, quadratic, DDA
university_math/       # Django app: transcendental root-finding
templates/             # HTML templates (single shared base + partials)
static/                # CSS design system / JS / images
```

## Security

- User equations are parsed with **sympy**, never `eval()`. The parser runs
  with Python builtins removed and a whitelist of math functions, blocking
  code-injection attempts.
- `SECRET_KEY` and other secrets come from `.env` / environment variables, never
  the repository (`.env` is git-ignored).
- Inputs are validated (intervals, tolerance, numeric coefficients) before use.