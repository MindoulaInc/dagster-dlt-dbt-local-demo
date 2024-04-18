import dlt

try:
    from .filesystem import readers  # type: ignore
except ImportError:
    from filesystem import (
        readers,
    )

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="63_load_duckdb",
        destination="filesystem",
        dataset_name="63_load",
        import_schema_path="schemas/import",
        export_schema_path="schemas/export",
        progress="log",
    )

    input_data_path = "file://input_data/63"

    # load all the CSV data, excluding headers
    medical = readers(
        bucket_url="{0}/medical/".format(input_data_path), file_glob="*.txt"
    ).read_csv_duckdb(chunk_size=10000, header=True, use_pyarrow=True)

    pharmacy = readers(
        bucket_url="{0}/pharmacy/".format(input_data_path), file_glob="*.txt"
    ).read_csv_duckdb(chunk_size=10000, header=True)

    # load_info = pipeline.run(
    #     medical, loader_file_format="parquet", table_name="63_medical"
    # )
    load_info = pipeline.run(
        pharmacy, loader_file_format="parquet", table_name="63_pharmacy"
    )

    print(load_info)
    print(pipeline.last_trace.last_normalize_info)
