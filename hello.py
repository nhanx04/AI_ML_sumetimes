def sap_xep(score):
    leng = len(score)

    for i in range(0, leng - 1):
        for j in range(i + 1, leng):
            if (score[i] > score[j]):
                tmp = score[i]
                score[i] = score[j]
                score[j] = tmp
    return score  

def tinh_trung_binh(score):
    tong = sum(score)
    return tong/n

def rest(sted):
    if len(sted) > 2:
        to_removed = sted[2:]  
        return sum(to_removed) / len(to_removed)
    else:
        return 0  

n = int(input("Nhap so phan tu cua mang: "))
score = []

for i in range(0, n):
    a = int(input("Nhap phan tu cua score: "))
    score.append(a)

for i in range(0, n):
    if (score[i] > 100):
        print("A value over 100 has been entered")
        break

sted = sap_xep(score)
trung_binh = tinh_trung_binh(score)
trung_binh2 = rest(sted)
print("Phan tu lon nhat: ", sted[n - 1])
print("Phan tu nho nhat: ", sted[0])
print("Gia tri trung binh cua mang: ",trung_binh)
print("Gia tri lon thu hai: ", sted[n-2])
print("Gia tri trung binh khi da loai bo hai phan tu nho nhat", trung_binh2)
    