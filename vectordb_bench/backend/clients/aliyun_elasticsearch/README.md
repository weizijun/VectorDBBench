# Aliyun Elasticsearch CLI

Aliyun Elasticsearch 的命令行工具，用于运行 VectorDBBench 基准测试。

## 概述

此 CLI 继承自 ElasticCloud CLI，复用了索引配置参数（HNSW 参数、分片设置等），仅覆盖了连接参数。Aliyun Elasticsearch 使用传统的 `host:port` 方式连接，而 ElasticCloud 使用 `cloud_id` 方式连接。

## 安装

```bash
pip install vectordb-bench
```

## 可用命令

| 命令 | 描述 |
|------|------|
| `AliyunElasticsearchHNSW` | 使用 HNSW 索引运行基准测试 |
| `AliyunElasticsearchHNSWInt8` | 使用 HNSW Int8 量化索引运行基准测试 |
| `AliyunElasticsearchHNSWInt4` | 使用 HNSW Int4 量化索引运行基准测试 |
| `AliyunElasticsearchHNSWBBQ` | 使用 HNSW BBQ (Binary Quantization) 索引运行基准测试 |

## 连接参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|------|------|------|--------|------|
| `--scheme` | str | 否 | `http` | 连接协议 (http 或 https) |
| `--host` | str | 是 | - | Elasticsearch 主机地址 |
| `--port` | int | 否 | `9200` | Elasticsearch 端口 |
| `--user` | str | 否 | `elastic` | 认证用户名 |
| `--password` | str | 是 | - | 认证密码 |
| `--indice` | str | 否 | `vdb_bench_indice` | Elasticsearch 索引名称（必须小写） |

## 索引配置参数

以下参数继承自 ElasticCloud CLI：

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|------|------|------|--------|------|
| `--number-of-shards` | int | 否 | `1` | 分片数量 |
| `--number-of-replicas` | int | 否 | `0` | 副本数量 |
| `--refresh-interval` | str | 否 | `30s` | 索引刷新间隔 |
| `--merge-max-thread-count` | int | 否 | `8` | 合并最大线程数 |
| `--use-force-merge` | bool | 否 | `True` | 是否使用强制合并 |
| `--use-routing` | bool | 否 | `False` | 是否使用路由 |
| `--use-rescore` | bool | 否 | `False` | 是否使用重打分 |
| `--oversample-ratio` | float | 否 | `2.0` | 重打分过采样比例 |

### HNSW 参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|------|------|------|--------|------|
| `--m` | int | 否 | `16` | HNSW M 参数 |
| `--ef-construction` | int | 否 | `100` | HNSW efConstruction 参数 |
| `--num-candidates` | int | 否 | `100` | 搜索候选数量 |
| `--element-type` | str | 否 | `float` | 向量元素类型 (`float` 或 `byte`) |

## 通用基准测试参数

以下参数继承自 CommonTypedDict：

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|------|------|------|--------|------|
| `--case-type` | str | 否 | `Performance1536D50K` | 测试用例类型 |
| `--db-label` | str | 否 | 当前时间 ISO 格式 | 数据库标签 |
| `--k` | int | 否 | `100` | 搜索最近邻数量 |
| `--drop-old/--skip-drop-old` | bool | 否 | `--drop-old` | 是否删除旧数据 |
| `--load/--skip-load` | bool | 否 | `--load` | 是否加载数据 |
| `--search-serial/--skip-search-serial` | bool | 否 | `--search-serial` | 是否执行串行搜索 |
| `--search-concurrent/--skip-search-concurrent` | bool | 否 | `--search-concurrent` | 是否执行并发搜索 |
| `--load-concurrency` | int | 否 | CPU 核心数 | 数据加载并发数 |
| `--concurrency-duration` | int | 否 | `30` | 并发搜索持续时间（秒） |
| `--num-concurrency` | str | 否 | `1,5,10,20,50,100` | 并发数列表（逗号分隔） |
| `--dry-run` | bool | 否 | `False` | 仅打印配置，不执行 |
| `--task-label` | str | 否 | - | 任务标签 |
| `--config-file` | path | 否 | - | YAML 配置文件路径 |

## 使用示例

### 基本用法

```bash
# 使用 HNSW 索引运行基准测试
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --port 9200 \
    --password your-password

# 使用 HTTPS 连接
vectordbbench AliyunElasticsearchHNSW \
    --scheme https \
    --host your-es-host.aliyuncs.com \
    --port 9200 \
    --user elastic \
    --password your-password

# 自定义索引名称
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --indice my_custom_index

# 使用 Int8 量化索引
vectordbbench AliyunElasticsearchHNSWInt8 \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --m 32 \
    --ef-construction 200
```

### 指定测试用例

```bash
# 使用特定测试用例
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --case-type Performance768D500K \
    --db-label "my-benchmark-test"

# 跳过数据加载，只执行搜索测试
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --skip-load \
    --search-serial
```

### 自定义索引配置

```bash
# 自定义分片和 HNSW 参数
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --number-of-shards 3 \
    --number-of-replicas 1 \
    --m 32 \
    --ef-construction 256 \
    --num-candidates 200 \
    --refresh-interval 60s

# 使用重打分功能
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --use-rescore \
    --oversample-ratio 3.0
```

### 使用配置文件

创建 YAML 配置文件 `aliyun_es_config.yml`:

```yaml
AliyunElasticsearchHNSW:
  host: your-es-host.aliyuncs.com
  port: 9200
  password: your-password
  scheme: https
  indice: my_benchmark_index
  m: 32
  ef-construction: 200
  number-of-shards: 2
  case-type: Performance1536D50K
  db-label: "config-file-test"
```

使用配置文件运行:

```bash
vectordbbench AliyunElasticsearchHNSW --config-file aliyun_es_config.yml
```

### 仅查看配置（Dry Run）

```bash
# 打印配置但不执行
vectordbbench AliyunElasticsearchHNSW \
    --host your-es-host.aliyuncs.com \
    --password your-password \
    --dry-run
```

## 与 ElasticCloud CLI 的区别

| 特性 | AliyunElasticsearch | ElasticCloud |
|------|---------------------|--------------|
| 连接方式 | `--host` + `--port` | `--cloud-id` |
| 用户名 | 可配置 `--user` | 固定为 `elastic` |
| 索引名称 | 可配置 `--indice` | 固定为 `vdb_bench_indice` |
| 索引配置 | 完全相同 | - |
| 命令名称 | `AliyunElasticsearch*` | `ElasticCloud*` |

## 支持的索引类型

| 索引类型 | 命令 | 描述 |
|----------|------|------|
| HNSW | `AliyunElasticsearchHNSW` | 标准 HNSW 索引 |
| HNSW Int8 | `AliyunElasticsearchHNSWInt8` | Int8 量化，减少内存占用 |
| HNSW Int4 | `AliyunElasticsearchHNSWInt4` | Int4 量化，更小的内存占用 |
| HNSW BBQ | `AliyunElasticsearchHNSWBBQ` | Binary Quantization，最小内存占用 |

## 查看帮助

```bash
# 查看所有可用命令
vectordbbench --help

# 查看特定命令的帮助
vectordbbench AliyunElasticsearchHNSW --help
```
