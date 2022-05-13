for i in range(1, 100):
    if i % 3 == 0:
        if i % 7 == 0:
            print("AçıkKaynak")
        else:
            print("Açık")
    elif i % 7 == 0:
        print("Kaynak")
    else:
        print(i)
