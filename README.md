# dlt + DuckDB — Auto-Pagination, Schema Evolution, and Zero Config

Companion repo for the video on dlt + DuckDB. https://youtu.be/mQ1t0To-1LE 

I pointed dlt at a REST API, a CSV file, and DuckDB. It handled pagination, schema inference, nested JSON normalization, and schema evolution — without me writing any of it.

No Airflow. No Spark. No enterprise licensing. Just dlt, DuckDB, and Python.

## What's in here

```
dlt-duckdb/
├── src/
│   └── dlt_duckdb/
│       ├── __init__.py          # Entry point (uv run dlt-duckdb)
│       ├── config.py            # Pydantic Settings (.env loader)
│       └── sources/
│           ├── __init__.py
│           ├── pokemon_api.py   # PokeAPI — rest_api_source()
│           └── team_rosters.py  # CSV — filesystem + read_csv()
├── data/
│   └── pokemon_teams.csv        # Sample team roster data
├── .dlt/
│   └── config.toml              # dlt configuration
├── .env                         # Environment variables (not committed)
├── pyproject.toml
└── README.md
```

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone <repo-url>
cd dlt-duckdb
```

Create a `.env` file in the project root:

```env
POKEMON_API=https://pokeapi.co/api/v2/
```

Run the pipeline:

```bash
uv run dlt-duckdb
```

That's it. dlt creates a local `dlt_pokemon.duckdb` file with your data.

## What dlt does for free

**PokeAPI source (`pokemon_api.py`)** — Uses `rest_api_source()`, the high-level declarative interface. You give it a base URL and a resource name. dlt figures out pagination (follows `next` links automatically), flattens nested JSON into relational tables, infers the schema, and adds pipeline metadata (`_dlt_load_id`, `_dlt_id`) to every row. No paginator config, no response parsing, no schema definition.

**CSV source (`team_rosters.py`)** — Uses `filesystem()` piped into `read_csv()`. Same pattern as the API source but for local files. dlt handles schema inference from the CSV headers and schema evolution when columns change between runs.

## Schema evolution demo

The video demonstrates schema evolution live. Run the pipeline once, then add a `region` column to `pokemon_teams.csv` and run it again. dlt detects the new column and adds it to the DuckDB table automatically — existing rows get `NULL` for the new column, no migration scripts needed.

dlt's default schema contract (`evolve`) handles three scenarios:

- **Add a column** — new column appears in the destination, old rows get NULL
- **Remove a column** — column stays in the table, new rows get NULL (never drops columns)
- **Rename a column** — treated as add + remove, both columns exist

## Why the scaffolding was updated

The video starts by running `dlt init rest_api duckdb` and immediately hitting four broken imports in the generated file. The scaffolding is reference code, not production code. This repo is the production version — proper package structure, Pydantic Settings for config, Loguru for logging, and source modules that separate concerns.

## Stack

- **[uv](https://docs.astral.sh/uv/)** — package management
- **[dlt](https://dlthub.com/)** — data loading
- **[DuckDB](https://duckdb.org/)** — local analytical database
- **[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** — configuration
- **[Loguru](https://github.com/Delgan/loguru)** — logging



---

*// made with blueberry lemonade*