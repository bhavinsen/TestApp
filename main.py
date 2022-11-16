from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def json_data():
    with open('search.json',mode='r') as myfile:
        json_data = json.load(myfile)
        data_arr = []
        for i in json_data:
            operator = i["operator"]
            if i.get("operating_manager",None) is not None:
                operating_manager = i["operating_manager"]
                data_arr.append(operating_manager)
            site = i["site"]
            ordz = i["ordz"]
            category = i["category"]
            description = i["description"]
            next_inspection = i["next_inspection"]
            data_arr.extend((operator, site, ordz, category, description ,next_inspection))

        return data_arr