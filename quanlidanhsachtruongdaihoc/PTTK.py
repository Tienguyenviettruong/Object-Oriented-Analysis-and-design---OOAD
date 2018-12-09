import sys
import os
import math
def menu():
    print("CHƯƠNG TRÌNH QUẢN LÍ DANH SÁCH CÁC TRƯỜNG ĐẠI HỌC")
    print("1: Thêm mới")
    print("2: Sửa")
    print("3: Xóa")
    print("4: Hiển thị danh sách")
    print("5: Tìm kiếm")
    print("6: Hiển thị danh sách trường có tuổi lớn hơn n")
    print("0: Out")
Tentruong=''
Tenviettat=''
Namthanhlap=0
diachi=''
n=0
class UNI():

    def __init__(self, Tentruong, Tenviettat, Namthanhlap, diachi):
        self.Tentruong = Tentruong
        self.Tenviettat = Tenviettat
        self.Namthanhlap = Namthanhlap
        self.diachi = diachi
    def gettenviettat(self):
        return self.Tenviettat
    def getnamthanhlap(self):
        return self.Namthanhlap
    def getDiachi(self):
        return self.diachi
    def getTinh(self):
        y = 2018 - self.Namthanhlap
        return y

def nhap():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    print("Tên trường: ")
    Tentruong = str(input())
    print("Tên viết tắt: ")
    Tenviettat = input()
    print("Năm thành lập: ")
    Namthanhlap = int(input())
    print("Địa chỉ: ")
    diachi = input()
def xuat():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    print("-------------------------------------------------------------------")
    print("Tên trường: ",Tentruong)
    print("Tên viết tắt: ",Tenviettat)
    print("Năm thành lập: ",Namthanhlap)
    print("Địa chỉ: ",diachi)

def add():
    global n
    print("Nhập sô trường: ")
    n = int(input())
#    file = open('data.txt','w')
    for i in range(1,n+1):
        nhap()
    for i in range(1,n+1):
        xuat()
def fixfullname():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    global n
    d = input("Nhập tên trường cần thay đổi: ")
    e = input("Nhập tên muốn thay đổi: ")
    for i in range(1,n+1):
            if  d == Tentruong:
                Tentruong = e
                return Tentruong
            else:
                print("Không có trường này")
def fixname():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    global n
    f = input("Nhập tên viết tắt muốn thay đổi: ")
    g = input("Nhập tên viết tắt cần thay đổi: ")
    for i in range(1,n+1):
            if  f == Tenviettat:
                Tenviettat = g
    return Tenviettat
def fixyear():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    global n
    h = int(input("Nhập năm muốn thay đổi"))
    i = int(input("Nhập địa chỉ cần thay đổi: "))
    for i in range(1,n+1):
            if  h == Namthanhlap:
                 Namthanhlap= h
    return Namthanhlap
def fixadd():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    global n
    w = input("Nhập địa chỉ muốn thay đổi: ")
    z = input("Nhập địa chỉ cần thay đổi: ")
    for i in range(1,n+1):
            if  w == diachi:
                diachi = z
    return diachi
def fix():
    def show():
        print("Chọn thông tin muốn sửa")
        print("1: Tên Trường")
        print("2: Tên viết tắt")
        print("3: Năm thành lập")
        print("4: Địa chỉ")
        print("0: Out")
    show()
    chon = int(input("Mời chọn: "))
    while chon != 0:
            if chon == 0:
                break
            elif chon == 1:
                fixfullname()
                xuat()
            elif chon ==2:
                fixname()
                xuat()
            elif chon == 3:
                fixyear()
                xuat()
            elif choice == 4:
                fixadd()
                xuat()
            else:
                print("Không có chức năng")
            chon = int(input("Mời chọn"))
def delete():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    global n
    b = input("Nhập tên cần tìm: ")
    for i in range(1,n+1):
        if b!=Tentruong:
            print("Không có trong danh sách")
        else:
            del Tentruong
            del Tenviettat
            del Namthanhlap
            del diachi
            print("Xóa trường")

def viewall():
    global n
    print("Hiển thị tất cả")
    for i in range(1,n+1):
        xuat()

def find():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    print("Tìm trường")
    a = input("Nhập tên cần tìm: ")
    if a==Tentruong:
        print(Tentruong,Tenviettat,Namthanhlap,diachi)
    else:
        print("Không tìm thấy trường [ \n ]")

def year():
    global Tentruong
    global Tenviettat
    global Namthanhlap
    global diachi
    global n
    k = int(input("Nhập tuổi: "))
    for i in range(1,n+1):
        x = 2018-Namthanhlap
    if x > k:
        print(Tentruong)
    else:
        print("Không có")


menu()
choice = int(input("Mời chọn chức năng: "))
while choice != 0:
        if choice == 0:
            break
        elif choice == 1:
            add()
        elif choice ==2:
            fix()
        elif choice == 3:
            delete()
        elif choice == 4:
            viewall()
        elif choice == 5:
            find()
        elif choice == 6:
            year()
        else:
            print("Không có chức năng")
        choice = int(input("Mời chọn chức năng: "))
print("Cảm ơn")
