from ..elastic_cloud.config import ElasticCloudIndexConfig
from ..elastic_cloud.elastic_cloud import ElasticCloud


class AliyunElasticsearch(ElasticCloud):
    def __init__(
        self,
        dim: int,
        db_config: dict,
        db_case_config: ElasticCloudIndexConfig,
        indice: str | None = None,  # must be lowercase
        id_col_name: str = "id",
        vector_col_name: str = "vector",
        drop_old: bool = False,
        **kwargs,
    ):
        # Get indice from db_config if not provided as parameter
        if indice is None:
            indice = db_config.pop("indice", "vdb_bench_indice")
        elif "indice" in db_config:
            db_config.pop("indice")  # Remove from db_config to avoid duplication

        super().__init__(
            dim=dim,
            db_config=db_config,
            db_case_config=db_case_config,
            indice=indice,
            id_col_name=id_col_name,
            vector_col_name=vector_col_name,
            drop_old=drop_old,
            **kwargs,
        )
