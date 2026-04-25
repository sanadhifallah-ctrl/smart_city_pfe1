from sqlalchemy import Column, Integer,String,Boolean,Enum,ForeignKey,Float,DateTime
from app.core.database import Base
import enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class ReportStatus(str, enum.Enum):
    pending='pending'
    in_progress='in_progress'
    resolved='resolved'
class Report(Base):
    __table_name__="reports" 

    id=Column(Integer,primary_key=True,index=True)

    citizen_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    audio_path=Column(String(100),nullable=False)

    latitude=Column(Float,nullable=False)


    longitude=Column(Float,nullable=False)


    adresse_txt=Column(String(100),nullable=False)

    status=Column(Enum(ReportStatus), default=ReportStatus.pending, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    citizen = relationship("User")


    
