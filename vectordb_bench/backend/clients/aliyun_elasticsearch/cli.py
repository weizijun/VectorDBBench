"""CLI for Aliyun Elasticsearch.

This CLI inherits from ElasticCloud CLI, only overriding the connection parameters.
The index configuration (HNSW parameters, shard settings, etc.) is shared with ElasticCloud.
"""

from typing import Annotated, TypedDict, Unpack

import click
from pydantic import SecretStr

from vectordb_bench.backend.clients import DB
from vectordb_bench.backend.clients.elastic_cloud.cli import (
    ElasticCloudHNSWParamsTypedDict,
    ElasticCloudIndexTypedDict,
)
from vectordb_bench.cli.cli import (
    CommonTypedDict,
    cli,
    click_parameter_decorators_from_typed_dict,
    run,
)

DBTYPE = DB.AliyunElasticsearch


class AliyunElasticsearchTypedDict(TypedDict):
    """Connection parameters for Aliyun Elasticsearch.

    Unlike ElasticCloud which uses cloud_id, Aliyun Elasticsearch uses
    traditional host/port connection parameters.
    """

    scheme: Annotated[
        str,
        click.option(
            "--scheme",
            type=str,
            help="Protocol in use to connect to the node (http or https)",
            required=False,
            default="http",
            show_default=True,
        ),
    ]
    host: Annotated[
        str,
        click.option(
            "--host",
            type=str,
            help="Elasticsearch host address",
            required=True,
        ),
    ]
    port: Annotated[
        int,
        click.option(
            "--port",
            type=int,
            help="Elasticsearch port",
            required=False,
            default=9200,
            show_default=True,
        ),
    ]
    user: Annotated[
        str,
        click.option(
            "--user",
            type=str,
            help="Username for authentication",
            required=False,
            default="elastic",
            show_default=True,
        ),
    ]
    password: Annotated[
        str,
        click.option(
            "--password",
            type=str,
            help="Password for authentication",
            required=True,
        ),
    ]
    indice: Annotated[
        str,
        click.option(
            "--indice",
            type=str,
            help="Elasticsearch index name (must be lowercase)",
            required=False,
            default="vdb_bench_indice",
            show_default=True,
        ),
    ]


class AliyunElasticsearchHNSWTypedDict(
    CommonTypedDict,
    AliyunElasticsearchTypedDict,
    ElasticCloudIndexTypedDict,
    ElasticCloudHNSWParamsTypedDict,
):
    """Full parameter set for Aliyun Elasticsearch HNSW index.

    Inherits:
    - CommonTypedDict: Common benchmark parameters (case_type, k, etc.)
    - AliyunElasticsearchTypedDict: Connection parameters (host, port, etc.)
    - ElasticCloudIndexTypedDict: Index parameters (shards, replicas, etc.)
    - ElasticCloudHNSWParamsTypedDict: HNSW algorithm parameters (m, ef_construction, etc.)
    """


@cli.command()
@click_parameter_decorators_from_typed_dict(AliyunElasticsearchHNSWTypedDict)
def AliyunElasticsearchHNSW(**parameters: Unpack[AliyunElasticsearchHNSWTypedDict]):
    """Run benchmark with Aliyun Elasticsearch using HNSW index."""
    from ..api import IndexType
    from ..elastic_cloud.config import ElasticCloudIndexConfig, ESElementType
    from .config import AliyunElasticsearchConfig

    run(
        db=DBTYPE,
        db_config=AliyunElasticsearchConfig(
            db_label=parameters["db_label"],
            scheme=parameters["scheme"],
            host=parameters["host"],
            port=parameters["port"],
            user=parameters["user"],
            password=SecretStr(parameters["password"]),
            indice=parameters["indice"],
        ),
        db_case_config=ElasticCloudIndexConfig(
            index=IndexType.ES_HNSW,
            M=parameters["m"],
            efConstruction=parameters["ef_construction"],
            num_candidates=parameters["num_candidates"],
            element_type=ESElementType(parameters["element_type"]),
            number_of_shards=parameters["number_of_shards"],
            number_of_replicas=parameters["number_of_replicas"],
            refresh_interval=parameters["refresh_interval"],
            merge_max_thread_count=parameters["merge_max_thread_count"],
            use_force_merge=parameters["use_force_merge"],
            use_routing=parameters["use_routing"],
            use_rescore=parameters["use_rescore"],
            oversample_ratio=parameters["oversample_ratio"],
            number_of_indexing_clients=parameters["number_of_indexing_clients"],
        ),
        **parameters,
    )


@cli.command()
@click_parameter_decorators_from_typed_dict(AliyunElasticsearchHNSWTypedDict)
def AliyunElasticsearchHNSWInt8(**parameters: Unpack[AliyunElasticsearchHNSWTypedDict]):
    """Run benchmark with Aliyun Elasticsearch using HNSW Int8 quantization index."""
    from ..api import IndexType
    from ..elastic_cloud.config import ElasticCloudIndexConfig, ESElementType
    from .config import AliyunElasticsearchConfig

    run(
        db=DBTYPE,
        db_config=AliyunElasticsearchConfig(
            db_label=parameters["db_label"],
            scheme=parameters["scheme"],
            host=parameters["host"],
            port=parameters["port"],
            user=parameters["user"],
            password=SecretStr(parameters["password"]),
            indice=parameters["indice"],
        ),
        db_case_config=ElasticCloudIndexConfig(
            index=IndexType.ES_HNSW_INT8,
            M=parameters["m"],
            efConstruction=parameters["ef_construction"],
            num_candidates=parameters["num_candidates"],
            element_type=ESElementType(parameters["element_type"]),
            number_of_shards=parameters["number_of_shards"],
            number_of_replicas=parameters["number_of_replicas"],
            refresh_interval=parameters["refresh_interval"],
            merge_max_thread_count=parameters["merge_max_thread_count"],
            use_force_merge=parameters["use_force_merge"],
            use_routing=parameters["use_routing"],
            use_rescore=parameters["use_rescore"],
            oversample_ratio=parameters["oversample_ratio"],
            number_of_indexing_clients=parameters["number_of_indexing_clients"],
        ),
        **parameters,
    )


@cli.command()
@click_parameter_decorators_from_typed_dict(AliyunElasticsearchHNSWTypedDict)
def AliyunElasticsearchHNSWInt4(**parameters: Unpack[AliyunElasticsearchHNSWTypedDict]):
    """Run benchmark with Aliyun Elasticsearch using HNSW Int4 quantization index."""
    from ..api import IndexType
    from ..elastic_cloud.config import ElasticCloudIndexConfig, ESElementType
    from .config import AliyunElasticsearchConfig

    run(
        db=DBTYPE,
        db_config=AliyunElasticsearchConfig(
            db_label=parameters["db_label"],
            scheme=parameters["scheme"],
            host=parameters["host"],
            port=parameters["port"],
            user=parameters["user"],
            password=SecretStr(parameters["password"]),
            indice=parameters["indice"],
        ),
        db_case_config=ElasticCloudIndexConfig(
            index=IndexType.ES_HNSW_INT4,
            M=parameters["m"],
            efConstruction=parameters["ef_construction"],
            num_candidates=parameters["num_candidates"],
            element_type=ESElementType(parameters["element_type"]),
            number_of_shards=parameters["number_of_shards"],
            number_of_replicas=parameters["number_of_replicas"],
            refresh_interval=parameters["refresh_interval"],
            merge_max_thread_count=parameters["merge_max_thread_count"],
            use_force_merge=parameters["use_force_merge"],
            use_routing=parameters["use_routing"],
            use_rescore=parameters["use_rescore"],
            oversample_ratio=parameters["oversample_ratio"],
            number_of_indexing_clients=parameters["number_of_indexing_clients"],
        ),
        **parameters,
    )


@cli.command()
@click_parameter_decorators_from_typed_dict(AliyunElasticsearchHNSWTypedDict)
def AliyunElasticsearchHNSWBBQ(**parameters: Unpack[AliyunElasticsearchHNSWTypedDict]):
    """Run benchmark with Aliyun Elasticsearch using HNSW BBQ (Binary Quantization) index."""
    from ..api import IndexType
    from ..elastic_cloud.config import ElasticCloudIndexConfig, ESElementType
    from .config import AliyunElasticsearchConfig

    run(
        db=DBTYPE,
        db_config=AliyunElasticsearchConfig(
            db_label=parameters["db_label"],
            scheme=parameters["scheme"],
            host=parameters["host"],
            port=parameters["port"],
            user=parameters["user"],
            password=SecretStr(parameters["password"]),
            indice=parameters["indice"],
        ),
        db_case_config=ElasticCloudIndexConfig(
            index=IndexType.ES_HNSW_BBQ,
            M=parameters["m"],
            efConstruction=parameters["ef_construction"],
            num_candidates=parameters["num_candidates"],
            element_type=ESElementType(parameters["element_type"]),
            number_of_shards=parameters["number_of_shards"],
            number_of_replicas=parameters["number_of_replicas"],
            refresh_interval=parameters["refresh_interval"],
            merge_max_thread_count=parameters["merge_max_thread_count"],
            use_force_merge=parameters["use_force_merge"],
            use_routing=parameters["use_routing"],
            use_rescore=parameters["use_rescore"],
            oversample_ratio=parameters["oversample_ratio"],
            number_of_indexing_clients=parameters["number_of_indexing_clients"],
        ),
        **parameters,
    )
