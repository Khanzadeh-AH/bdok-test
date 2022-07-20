from fastapi import FastAPI
from db.mongodb_utils import connect_to_mongo, close_mongo_connection
from api.v1.router import router as apirouter

tags_metadata = [
    {
        "name": "Product",
        "description": "product CRUD",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

app.add_event_handler('startup', connect_to_mongo)
app.add_event_handler('shutdown', close_mongo_connection)

app.include_router(apirouter)
