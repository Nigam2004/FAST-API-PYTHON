from fastapi import FastAPI

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