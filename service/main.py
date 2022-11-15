import uvicorn
from fastapi import FastAPI
import api_data
import random

app = FastAPI()

@app.get("/")
def index():
    return{
        "message":"Bienvenido a DuckDuckGo. Recuerda, la privacidad es lo más importante."
    }

@app.get("/catch/tracker")
async def trackerCatcher():
    catched = []
    cantidad = random.randint(1,10)

    for x in range(cantidad):
        tracker = await api_data.catchTracker()
        trackInfo = {"nombre":tracker.bank_name, "addressID":tracker.uid}
        catched.append(trackInfo)
    return catched

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)