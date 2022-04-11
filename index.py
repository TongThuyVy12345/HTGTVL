from flask import render_template, url_for
from TimViec import app, login
from flask_login import login_user
# from twilio.rest import Client
import cloudinary.uploader
import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy.linalg import norm
import csv



@app.route("/")
def TrangChu():


    return render_template("TrangChu.html")

@app.route('/admin-login',methods=['post'])
def admin_login():
    war = ""
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        role = utils.get_role(username=username, password=password)
        admin = utils.check_login(username=username, password=password, role=role)
        if admin:
            login_user(user=admin)
    except Exception as ex:
        war = 'Không tồn tại người dùng'

    return redirect('/admin')

@login.user_loader
def load_nguoidung(user_id):
    return utils.get_nguoidung_id(user_id=user_id)

@app.route('/user-signin', methods=['get', 'post'])
def user_signin():
    warning_err = ''
    if request.method.__eq__('POST'):
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            role_user = utils.get_role(username=username, password=password)
            if str(role_user) == 'UserRole.NguoiDung':
                user = utils.check_login(username, password)
            elif str(role_user) == 'UserRole.NguoiQuanTri':
                user = utils.check_login(username, password, role_user)
            else:
                user = utils.check_login(username, password)
            if user:
                login_user(user=user)
                return redirect(url_for('TrangChu'))
            else:
                warning_err = 'Thông tin đăng nhập không chính xác !!!'
        except Exception as ex:
            warning_err = "Không tồn tại người dùng"

    return render_template('login.html',warning_err=warning_err)

@app.route('/user-signout')
def user_signout():
    logout_user()
    return redirect(url_for('user_signin'))

@app.route('/register', methods=['get','post'])
def user_register():
    err_register = ""
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        email = request.form.get('email')
        gender = request.form.get('gender')
        address = request.form.get('address')
        birthday = request.form.get('birthday')
        SDT = request.form.get('SDT')
        avatar_path = None
        try:
            if password.strip().__eq__(confirm.strip()):
                avatar = request.files.get('avatar')
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path = res['secure_url']
                utils.add_user(name=name, username=username, password=password, email=email, gender=gender, address=address, birthday=birthday, avatar=avatar_path, SDT=SDT)
                return redirect(url_for('user_signin'))
            else:
                err_register = "Mật khẩu không khớp"

        except Exception as ex:
            err_register = "Trùng tài khoản hoặc sai thông tin (sdt phải khác nhau)"

    return render_template('dangki.html',err_register=err_register)

@app.route('/timviec',methods=['get','post'])
def timviec():
    mota =[]
    x = request.args.get("mota")
    mota.append(str(x))
    print(x)
    data = []
    congviec = []
    with open('data/data.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            congviec.append(row["congviec"])
            data.append(row['key'])
    # khởi tạo
    counter = CountVectorizer(min_df=1)
    # tạo data bằng counter
    tf_matrix = counter.fit_transform(data)
    arr = tf_matrix.todense()

    # khởi tạo
    v = TfidfVectorizer()
    # tạo data bằng vectorizen
    vectors_train = v.fit_transform(data)
    arrv = vectors_train.todense()

    vt = counter.transform(mota).toarray()
    vy = arrx(vt, len(counter.vocabulary_), 0)  # chuyển lại mãng 1 chiều

    cvthichhop = 0
    phuhop = 0
    for i in range(0, len(congviec)):
        vx = arrx(arrv, len(counter.vocabulary_), i)  # chuyển 1 chiều của vector công việc thứ i
        print(cosine(vy, vx))
        if cosine(vy, vx) > phuhop:
            phuhop = cosine(vy, vx)
            cvthichhop = i

    if phuhop>0.4:
        return render_template("TrangChu.html",thongbao=congviec[cvthichhop])
    return render_template("TrangChu.html", thongbao="không có")

def cosine(x, y):
    cos_sim = np.dot(x, y)/(norm(x)*norm(y))
    return cos_sim

def arrx(arr,n, x):
    a = []
    for i in range(n):
        a.append(arr[x, i])
    return a

if __name__ == '__main__':
    from TimViec.admin import *
    app.run(debug=True)

