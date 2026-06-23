# tailor

[![CI](https://github.com/oresttokovenko/tailor/actions/workflows/ci.yml/badge.svg)](https://github.com/oresttokovenko/tailor/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/oresttokovenko/tailor)](https://github.com/oresttokovenko/tailor/blob/main/LICENSE)

Tailoring a resume for every application still takes work, but the file-management part shouldn't. This CLI creates a directory per company, a subdirectory per role, drops in a `job_description.txt`, and copies over whatever template files you keep in `_template`.

Here's a Typst example using the `_template` option:

```
_template/
├── font
│   └── font.otf
└── main.typ
```

Running the tool for a Software Engineer role at Facebook produces:

```
Facebook
└── software_engineer
    ├── font
    │   └── font.otf
    ├── job_description.txt
    └── main.typ
```

## Install

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install git+https://github.com/oresttokovenko/tailor.git
```

## Usage

```sh
tailor -c Facebook -j "software engineer"
```

The `-t` flag copies `_template/` contents into the new job directory (on by default). Use `-T` to skip it:

```sh
tailor -c Facebook -j "software engineer" -t
tailor -c Facebook -j "software engineer" -T
```

If `_template` is empty or missing, nothing gets copied. The tool creates the directories and `job_description.txt` either way.

## Develop

```sh
uv sync
uv run tailor -c facebook -j "software engineer"
```

Run checks:

```sh
uv run ruff check .
uv run pyrefly check
uv run pytest tests/ -v
```

## Roadmap

- Named template folders so you can keep different base resumes for different kinds of roles:

  ```sh
  tailor -c Apple -j "platform engineer" -t _infra_engineer
  ```
