from . import db
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MathRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(50), nullable=False)
    input = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class MathRequestSchema(BaseModel):
    id: Optional[int] = None
    operation: str
    input: str
    result: str
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True
