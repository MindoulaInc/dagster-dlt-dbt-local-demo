import dlt

try:
    from .filesystem import readers  # type: ignore
except ImportError:
    from filesystem import (
        readers,
    )


def mindoula_s3_source(file_glob: str):

    pharmacy = readers(file_glob=file_glob).read_csv_duckdb(
        chunk_size=10000, header=True, use_pyarrow=True
    )

    return pharmacy


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="63_load_duckdb",
        destination="filesystem",
        dataset_name="63_load",
        import_schema_path="schemas/import",
        export_schema_path="schemas/export",
        progress="log",
        full_refresh=True,
    )

    input_source = mindoula_s3_source("63/pharmacy/*.txt")

    load_info = pipeline.run(
        input_source, loader_file_format="parquet", table_name="63_pharmacy"
    )

    print(load_info)
    print(pipeline.last_trace.last_normalize_info)
