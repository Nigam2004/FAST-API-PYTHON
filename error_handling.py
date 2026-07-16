from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()
student_deatails={
    101:{"name":"nigam","roll_no":20,"grade":"A","class_":"7th"},
    102:{"name":"raj","roll_no":22,"grade":"B","class_":"7th"},
    103:{"name":"suman","roll_no":25,"grade":"c","class_":"7th"},
}

@app.get("/student/{s_id}")
def stu_info(s_id:int):
    if s_id not in student_deatails:
        raise HTTPException(status_code=404, detail=f"student not found for id {s_id}")
    return ( student_deatails[s_id])
        
    
class student_sub(BaseModel):
    s_id:int
    sub:str
    mark:int

## Ex-----2

@app.post("/students_sub")
def su_suv(s_sub:student_sub):
    if  s_sub.s_id not in student_deatails  :
        raise HTTPException(
            status_code=404,
            detail={
                "error":f'the provided id {s_sub.s_id} not found'
            }
        )

    if  s_sub.mark <0 :
        raise HTTPException(
            status_code=400,
            detail={
                "error":f'the provided imark {s_sub.mark} is less than 0'
            }
        )
    if  s_sub.sub.strip()=="" :
        raise HTTPException(
            status_code=400,
            detail={
                "error":"subject is empty please fill the subject"
            }
        )
    try:
        student_deatails[s_sub.s_id]["mark"]=s_sub.mark
        return {
            "student":student_deatails[s_sub.s_id],
            "mark":s_sub.mark,
        }
    except Exception as err:
        raise HTTPException(
            status_code=400,
            detail=f"error found{err}"

        )
 
    
    