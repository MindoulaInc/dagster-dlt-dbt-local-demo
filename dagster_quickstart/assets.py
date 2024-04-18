import json
import requests

import pandas as pd

from dagster import MaterializeResult, MetadataValue, asset, get_dagster_logger
from dagster_quickstart.configurations import HNStoriesConfig
from .resources import DltResource
from .dlt63 import mindoula_s3_source


# @asset
# def payer_63_pipeline(pipeline: DltResource):
#
#     dlt_source = mindoula_s3_source(file_glob="63/pharmacy/*.txt")
#     logger = get_dagster_logger()
#     results = pipeline.create_pipeline(dlt_source, table_name="63_pharmacy")
#     logger.info(results)
@asset
def payer_63_pharmacy(pipeline: DltResource):
    """Copy over all pharmacy 63 data from flatfiles to parquet files"""

    logger = get_dagster_logger()
    dlt_source = mindoula_s3_source(file_glob="63/pharmacy/*.txt")
    results = pipeline.create_pipeline(dlt_source, table_name="63_pharmacy")
    logger.info(results)


@asset
def hackernews_top_story_ids(config: HNStoriesConfig):
    """Get top stories from the HackerNews top stories endpoint."""
    top_story_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    ).json()

    with open(config.hn_top_story_ids_path, "w") as f:
        json.dump(top_story_ids[: config.top_stories_limit], f)


@asset(deps=[hackernews_top_story_ids])
def hackernews_top_stories(config: HNStoriesConfig) -> MaterializeResult:
    """Get items based on story ids from the HackerNews items endpoint."""
    with open(config.hn_top_story_ids_path, "r") as f:
        hackernews_top_story_ids = json.load(f)

    results = []
    for item_id in hackernews_top_story_ids:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        results.append(item)

    df = pd.DataFrame(results)
    df.to_csv(config.hn_top_stories_path)

    return MaterializeResult(
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(str(df[["title", "by", "url"]].to_markdown())),
        }
    )
