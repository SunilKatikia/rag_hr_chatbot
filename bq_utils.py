from google.cloud import bigquery
from secret_manager import config

client = bigquery.Client(project=config.project_id)

def perform_vector_search(query_vector, top_k=5):
    query = f"""
    SELECT content, filename, distance
    FROM VECTOR_SEARCH(
        TABLE `{config.project_id}.{config.dataset_id}.{config.table_id}`,
        'embedding',
        (SELECT {query_vector} AS query_v),
        top_k => {top_k},
        distance_type => 'COSINE'
    )
    """
    return [dict(row) for row in client.query(query)]

def insert_to_bq(rows):
    table_ref = f"{config.project_id}.{config.dataset_id}.{config.table_id}"
    errors = client.insert_rows_json(table_ref, rows)
    return errors
