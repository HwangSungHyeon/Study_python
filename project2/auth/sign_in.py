
# login.py를 가져왔을 경우
import valid as _v
from member_service import login

def signIn(id,pw):
    if not _v.id_len_check(id):
        print("아이디는 4 ~ 12자")
    elif not _v.pw_len_check(pw):
        print("비밀번호는 최소 6자")
    else:
        return login.login_process(id,pw)


# login.py를 가져오지 않았을 경우
# import valid as _v
# from data import db as _db

# def signIn(id,pw):
#     if not _v.id_len_check(id):
#         print("아이디는 4 ~ 12자")
#     elif not _v.pw_len_check(pw):
#         print("비밀번호는 최소 6자")
#     else:
#         uid, upw = _db.find_by_id(id)
#         if uid==id and upw == pw:
#             print("로그인 성공")
#         else:
#             print("아이디 또는 비밀번호가 잘못되었습니다.")