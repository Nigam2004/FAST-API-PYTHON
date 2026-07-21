from fastapi import FastAPI
from database_connect import products

app = FastAPI()

@app.get("/")
# URL:-http://127.0.0.1:8000/
def read_root():
    return {"message": "1st api through puthon"}

@app.get("/home")
# URL:-http://127.0.0.1:8000/home
def  home_page():
    return ("this is my home page")

@app.get("/customer")
#input:-http://127.0.0.1:8000/customer?customer_id=123
def customer(customer_id=int):
    return{
        "customer_id":customer_id,
         "Cust_name":"Nigam",
         "Cust_mob":"12346789"

    }


# DatBase-connection-mongodb

@app.post("/products")
async def create_product(product: dict):

    result = await products.insert_one(product)

    return {
        "id": str(result.inserted_id)
    }

@app.get("/products")
async def get_products():

    data = []

    async for product in products.find():

        product["_id"] = str(product["_id"])
        data.append(product)
    return data