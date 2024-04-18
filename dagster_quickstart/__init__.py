from dagster import Definitions, load_assets_from_modules

from . import assets
from .resources import DltResource

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "pipeline": DltResource(
            pipeline_name="63_load_duckdb",
            destination="filesystem",
            dataset_name="63_load",
            import_schema_path="schemas/import",
            export_schema_path="schemas/export",
            progress="log",
            full_refresh=True,
        ),
    },
)
