from dagster import ConfigurableResource
import dlt


class DltResource(ConfigurableResource):
    pipeline_name: str
    dataset_name: str
    destination: str
    import_schema_path: str
    export_schema_path: str
    progress: str
    full_refresh: bool

    def create_pipeline(self, resource_data, table_name):

        # configure the pipeline with your destination details
        pipeline = dlt.pipeline(
            pipeline_name=self.pipeline_name,
            destination=self.destination,
            dataset_name=self.dataset_name,
        )

        # run the pipeline with your parameters
        load_info = pipeline.run(
            resource_data, table_name=table_name, loader_file_format="parquet"
        )

        return load_info
