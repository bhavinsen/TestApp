from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/chat/recieve')
def recieve_massages():
    with open('search.json',mode='r') as myfile:
        json_data = json.load(myfile)
        data_info_arr= []
        for i in json_data:
            data_arr = []
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
            data_info_arr.append(data_arr)

        return data_info_arr