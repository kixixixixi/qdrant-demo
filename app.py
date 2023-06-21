from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient("http://qdrant:6333")


client.upsert(
    collection_name="rgb_collection",
    points=[
        PointStruct(
            id=1,
            vector=[255.0, .0, 0.0],
            payload={"color": "red"}
        ),
        PointStruct(
            id=2,
            vector=[0.0, 255.0, 0.0],
            payload={"color": "green"}
        ),
        PointStruct(
            id=3,
            vector=[0.0, 0.0, 255.0],
            payload={"color": "blue"}
        ),
        PointStruct(
            id=4,
            vector=[255.0, 105.0, 180.0],
            payload={"color": "pink"}
        )
    ]
)

hits = client.search(
    collection_name="rgb_collection",
    query_vector=[255.0, 255.0, 0.0],
    limit=3
)

print(hits)
