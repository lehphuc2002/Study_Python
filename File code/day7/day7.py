import random
import hangman_art
import day7_hangmanWords
print(hangman_art.logo)
soMangConLai = 6
# step 1:
chuoikhoangtrang = []
#word_list = ["ardvark", "baboon", "camel"]
chuoinayne = random.choice(day7_hangmanWords.word_list)
for i in range(0, len(chuoinayne)):
    chuoikhoangtrang += "_"
print(f"Chuoi duoc chon la: {chuoinayne}")
"""
print(f"Chuoi khoang trang: {chuoikhoangtrang}")
kytune = input("nhap ky tu tim kiem di nao: ")
for i in range(0, len(chuoinayne)):
    if kytune == chuoinayne[i]:
        print("Right")
    else:
        print("Wrong")
# step2
for i in range(0, len(chuoinayne)):
    if kytune == chuoinayne[i]:
        chuoikhoangtrang[i] = kytune
print(f"chuoikhoangtrang la : {chuoikhoangtrang}")
"""
# step3
checkMap = 0
while checkMap == 0:
    checkCoiCoNhapKyTuCuKhong = 0;
    kytune = input("\nNhap ky tu tim kiem di nao: ")
    if kytune in chuoikhoangtrang:
        print("Nhap ky tu nay roi ma nhap hoai dm")
        checkCoiCoNhapKyTuCuKhong = 1;
    if(checkCoiCoNhapKyTuCuKhong == 0):
        print(f"You da nhap ky tu la: {kytune}")
        for i in range(0, len(chuoinayne)):
            if kytune == chuoinayne[i]:
                chuoikhoangtrang[i] = kytune
        if kytune not in chuoinayne:
            print(f"Rat tiec, {kytune} khong nam trong chuoi random he, mat 1 diem nha'")
            soMangConLai -= 1
            print(hangman_art.stages[soMangConLai])
            if soMangConLai == 0:
                print(hangman_art.stages[soMangConLai])
                checkMap = 1
                print("Thua roi haha")
        print(f"chuoikhoangtrang la : {chuoikhoangtrang}")
        if "_" not in chuoikhoangtrang:
            checkMap = 1
            print("Thang roi, hen day")
# print(f"Xong game roi dmm luon")

# step4
