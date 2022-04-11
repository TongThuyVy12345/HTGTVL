import numpy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy.linalg import norm
import csv

def cosine(x, y):
    cos_sim = np.dot(x, y)/(norm(x)*norm(y))
    return cos_sim

def arrx(arr,n, x):
    a = []
    for i in range(n):
        a.append(arr[x, i])
    return a


data =[]
congviec = []
with open('data/data.csv', newline='',encoding="utf-8" ) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        congviec.append(row["congviec"])
        data.append(row['key'])
print(data)
print(congviec)
test1 ="Hệ thống thông tin/Công nghệ phần mềm"
test =[]
test.append(test1)


# khởi tạo
counter = CountVectorizer(min_df=1)
# tạo data bằng counter
tf_matrix = counter.fit_transform(data)
arr = tf_matrix.todense()

# khởi tạo
v = TfidfVectorizer()
# tạo data bằng vectorizen
vectors_train = v.fit_transform(data)
arrv =vectors_train.todense()

# vector hóa dữ liệu test
vt =counter.transform(test).toarray()
vy= arrx(vt,len(counter.vocabulary_) ,0)#chuyển lại mãng 1 chiều

cvthichhop =0
phuhop =0
for i in range(0, len(congviec)):
    vx = arrx(arrv,len(counter.vocabulary_) ,i)#chuyển 1 chiều của vector công việc thứ i
    print(cosine(vy, vx))
    if cosine(vy,vx) >phuhop:
        phuhop =cosine(vy,vx)
        cvthichhop=i

print(congviec[cvthichhop])






