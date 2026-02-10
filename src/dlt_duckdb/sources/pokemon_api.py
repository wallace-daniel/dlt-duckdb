"""PokeAPI source — demonstrates what dlt gives you for free."""


from dlt.sources.rest_api import rest_api_source
from dlt_duckdb.config import Settings

def pokemon_source():
    """Creates a dlt source that pulls from the PokeAPI.

    dlt handles all of this automatically:
    - Pagination (follows next links until exhausted)
    - Nested JSON normalization (flattens into relational tables)
    - Schema inference (creates columns from the response shape)
    - Pipeline metadata (_dlt_load_id, _dlt_id on every row)
    """
    settings = Settings() #type: ignore[import]
    return rest_api_source(
        {
            "client": {
                "base_url": settings.POKEMON_API,
            },
            "resource_defaults": {
                "endpoint": {
                    "params": {
                        "limit": 100,
                    },
                },
            },
            "resources": [
                "pokemon",
            ],
        },
        name="pokemon",
    )