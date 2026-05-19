
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from database.db import Base

class Attend(Base):
    __tablename__ = "attend"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    attend = Column(Integer)
    late = Column(Integer)
    absent = Column(Integer)
    early_leave = Column(Integer)
    create_at = Column(DateTime, default=datetime.now)