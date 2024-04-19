<div align="center">
  <a target="_blank" href="https://dagster.io" style="background:none">
    <img alt="dagster logo" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/7010804c-05a6-4ef4-bfc8-d9c88d458906" width="auto" height="120px">
  </a>
</div>

# Dagster Quickstart

Get up-and-running with the Dagster quickstart project -- open the project in a GitHub Codespace and start building data pipelines with no local installation required.

For more information on how to use this project, please reference the [Dagster Quickstart guide](https://docs.dagster.io/getting-started/quickstart).

## Running The Project

1. Clone the Dagster Quickstart repository:

2. Install the required dependencies.

    Install `pipx`, `poetry` and Python 3.9 with `brew`.

    ```sh
    # from the project root directory...
    poetry shell
    poetry install
    ```

3. Copy source data into the `input_data` folder at the project root

4. Create your own asset in the `dagster_quickstart/assets.py` file. Be sure to mimic the `payer_63_pharmacy` asset.

5. Run the project!

    ```sh
    dagster dev
    ```

6. Materialize your asset. It should output to a parquet file in `output_data`.

## Development

### Adding new Python dependencies

You can specify new Python dependencies via `poetry add`.

### Unit testing

Tests are in the `dagster_quickstart_tests` directory and you can run tests using `pytest`.

