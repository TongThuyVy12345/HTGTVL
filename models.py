from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from TimViec import app, db
from datetime import datetime
from flask_login import UserMixin
from enum import Enum as UserEnum

class UserRole(UserEnum):
    NguoiQuanTri = 1
    NguoiDung =2
class Sex(UserEnum):
    Nam = 1
    Nu = 2
    Khac = 3

class User(db.Model,UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenNguoiDung = Column(String(50), nullable=False)
    taiKhoan = Column(String(50), nullable=False, unique=True)
    matKhau = Column(String(50), nullable=False)
    gioiTinh = Column(Enum(Sex), default=Sex.Nam)
    namSinh = Column(DateTime)
    active = Column(Boolean, default=True)
    avatar = Column(String(200))
    email = Column(String(50))
    diaChi = Column(String(500))
    ngayTao = Column(DateTime, default=datetime.now())
    SDT = Column(Integer, nullable=False,unique=True)
    user_role = Column(Enum(UserRole))
    def __str__(self):
        return self.tenNguoiDung


if __name__ == '__main__':
    db.create_all()






