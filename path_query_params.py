from fastapi import FastAPI

app=FastAPI()

student_deatails={
    101:{"name":"nigam","roll_no":20,"grade":"A","class_":"7th"},
    102:{"name":"raj","roll_no":22,"grade":"B","class_":"7th"},
    103:{"name":"suman","roll_no":25,"grade":"c","class_":"7th"},
}
## PATH PARAMETERS
@app.get("/s_detail/{student_id}")
# to get the data:-http://127.0.0.1:8000/s_detail/102
# to get error msg:-http://127.0.0.1:8000/s_detail/104
def student_info(student_id:int):
    if student_id not in student_deatails:
        return {"error":f"student roll no {student_id} not found"}
    profile=student_deatails[student_id]
    return{
        "s_roll_id":student_id,
        "s_name":profile["name"],
        "s_rollno":profile["roll_no"],
        "s_grade":profile["grade"]
      
    }


## QUERY PARAMETERS

@app.get("/s_detail")
#to get the data:- http://127.0.0.1:8000/s_detail?s_id=102
# to get error msg:-http://127.0.0.1:8000/s_detail?s_id=105
def student_info(s_id:int):
    if s_id not in student_deatails:
        return{"error":f"student details not found for student id {s_id}" }
    profile=student_deatails[s_id]
    return{
        "s_roll_id":s_id,
        "s_name":profile["name"],
        "s_rollno":profile["roll_no"],
        "s_grade":profile["grade"]
    }

student_dtl=[
    {"id":101,"name":"nigam","roll_no":20,"grade":"A","class_":"7th"},
    {"id":102,"name":"raj","roll_no":22,"grade":"A","class_":"7th"},
    {"id":103,"name":"suman","roll_no":26,"grade":"c","class_":"8th"},
    {"id":104,"name":"deepak","roll_no":24,"grade":"A","class_":"7th"},
    {"id":105,"name":"ram","roll_no":28,"grade":"c","class_":"8th"},
]

@app.get("/s_dtl")
# to get the data:-http://127.0.0.1:8000/s_dtl?grade=A&class_=7th
def s_dtl(grade:str,class_:str):
   filtered=[ s for s in student_dtl
            if s["grade"]==grade and s["class_"]==class_ ] 
   print(filtered)
   return{
       "grade":grade,
        "class_":class_,
        "count":len(filtered),
        "res":filtered
   }
    