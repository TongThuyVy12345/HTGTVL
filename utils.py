from TimViec.models import User,UserRole
import hashlib
from TimViec import db,app
from sqlalchemy import func
from sqlalchemy.sql import extract
from datetime import datetime
import hashlib

def get_nguoidung_id(user_id):
    return User.query.get(user_id)

def check_login(username,password,role=UserRole.NguoiDung):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.taiKhoan.__eq__(username.strip()),User.matKhau.__eq__(password),User.user_role.__eq__(role),User.active.__eq__(1)).first()

def get_role(username,password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        getrole =  User.query.filter(User.taiKhoan.__eq__(username.strip()),User.matKhau.__eq__(password),User.active.__eq__(1)).first()
    return getrole.user_role



def add_user(name,username,password,SDT,role=UserRole.NguoiDung, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(tenNguoiDung=name,
                taiKhoan=username,
                matKhau=password,
                gioiTinh=kwargs.get('gender'),
                namSinh=kwargs.get('birthday'),
                avatar=kwargs.get('avatar'),
                email=kwargs.get('email'),
                diaChi=kwargs.get('address'),
                user_role=role,
                SDT=SDT)
    db.session.add(user)
    db.session.commit()

def loaduser(username):
    uu = User.query.filter(User.active == True, User.taiKhoan.__eq__(username)).first()
    return uu

def eq_user(username):
    eq_user = User.query.filter(User.taiKhoan.__eq__(username)).first()
    return eq_user.taiKhoan

def getuser(username,sdt):
    uu = User.query.filter(User.tenNguoiDung.__eq__(username),User.SDT.__eq__(sdt)).first()
    return uu



