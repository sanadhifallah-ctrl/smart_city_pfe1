from fastapi import FASTAPI 
app= FASTAPI()
@app.get('/')
def root():
    return {"message": "Project running"}
   