from laba_3D import Car, Train 

def main():
    c1 = Car("KIA", 300, 3)
    print(c1.info())

    t1 = Train("RZD", 200, 12)
    print(t1.info())

if __name__ == "__main__":
    main()