from pydantic import BaseModel

class AntiTracker_Model(BaseModel):
    bank_name: str
    uid: str