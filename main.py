from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "1st api through puthon"}

@app.get("/home")
def  home_page():
    return ("this is my home page")