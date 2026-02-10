import dlt
from dlt_duckdb.sources.pokemon_api import pokemon_source
from dlt_duckdb.sources.team_rosters import team_rosters_source

from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO")

def main(): 
    pipeline = dlt.pipeline(
        pipeline_name="dlt_pokemon",
        destination="duckdb",
        dataset_name="pokemon_data",
    )

    # Source 1: PokeAPI
    load_info = pipeline.run(pokemon_source())
    logger.info(load_info)

    # Source 2: CSV team rosters
    load_info = pipeline.run(team_rosters_source())
    logger.info(load_info)
