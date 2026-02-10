"""Team rosters CSV source — demonstrates schema evolution."""

from dlt.sources.filesystem import filesystem, read_csv

from dlt_duckdb.config import Settings


def team_rosters_source():
    """Creates a dlt source that loads team rosters from CSV.

    dlt handles:
    - Schema inference (column names and types from the CSV)
    - Schema evolution (detects new columns on subsequent runs)
    - Pipeline metadata (_dlt_load_id, _dlt_id on every row)
    """
    settings = Settings() # type: ignore[import]

    csv_source = filesystem(
        bucket_url=f"file://{settings.DATA_DIR.resolve()}",
        file_glob="pokemon_teams.csv",
    ) | read_csv()

    return csv_source.with_name("team_rosters")

