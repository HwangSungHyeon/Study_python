
from fastapi import HTTPException

from models.attend import Attend
from models.student import Student
from schemas.attend_schema import AttendResponse

def create_attend_service(attend, db):
    attendData = [attend.attend, attend.late, attend.absent, attend.early_leave]

    for value in attendData:
        if value < 0:
            raise HTTPException(
                status_code=400,
                detail="0 이상만 입력 가능합니다."
            )

    student = db.query(Student).filter(Student.id == attend.student_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            message="학생 정보를 찾을 수 없습니다."
        )
    new_attend = Attend(
        student_id = attend.student_id,
        attend = attend.attend,
        late = attend.late,
        absent = attend.absent,
        early_leave = attend.early_leave
    )
    db.add(new_attend)
    db.commit()
    db.refresh(new_attend)

def get_attend_list(db):
    attend_list = db.query(Attend, Student).join(Student, Attend.student_id == Student.id).all()

    result = []
    for attend, std in attend_list:
        total_count = (attend.attend + attend.late + attend.absent + attend.early_leave)
        if total_count == 0:
            attendance_rate = 0
        else:
            attendance_rate = (attend.attend / total_count) * 100

        result.append( AttendResponse(
            id= attend.id,
            student_id= std.id,
            student_name= std.name,
            attend= attend.attend,
            late= attend.late,
            absent= attend.absent,
            early_leave= attend.early_leave,
            total_count= total_count,
            attendance_rate= round(attendance_rate, 2),
            create_at= attend.create_at
        ))
    return result
