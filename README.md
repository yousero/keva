# keva

Minimal key-value store for Python with two backends and a tiny HTTP API.

## Installation

With Poetry (recommended):

```sh
poetry install
```

Or classic `pip` from source:

```sh
pip install .
```

## Usage

### In-memory backend

```python
from keva import keva_mem

keva_mem.reset()
keva_mem.set("name", "keva")
print(keva_mem.get("name"))  # "keva"
```

### String backend

```python
from keva import keva_str

keva_str.reset()
keva_str.set("version", "0.0.1")
print(keva_str.get("version"))  # "0.0.1"
```

Both backends expose the same functions:

- `set(key, value)`
- `get(key)` → returns `""` if key is missing
- `reset()`
- `delete(key)` (safe if key does not exist)

## HTTP server

There is a tiny HTTP wrapper around the in-memory backend:

```sh
python -m keva.keva_server
```

By default it listens on port `8000` and supports:

- `GET /get?key=foo`
- `POST /set?key=foo&value=bar`
- `POST /delete?key=foo`
- `POST /reset`

All responses are JSON.

## Tests

After installing dev dependencies with Poetry:

```sh
poetry run pytest
```
