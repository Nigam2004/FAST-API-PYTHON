from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class loan_application(BaseModel):
    applicant_name:str
    applicant_age:int
    applicant_income:int
    applicant_loan_amount:int

@app.post("/loan_application")
def loan_application(application:loan_application):
     
     if application.applicant_age >20 and application.applicant_income>50000:
         decission="approved"
     else:
        decission="rejected"

     return{
        "applicant_name":application.applicant_name,
        "applicant_income":application.applicant_income,
         "Response":decission
     }
   
