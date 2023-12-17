def Addition(A: float, B: float) -> float:
    return A + B

def Difference(A: float, B: float) -> float:
    return A - B
  
def Division (A: float, B :float) -> float:
    if B == 0:
        print("Error: division by zero")
        return 0
    return A/B

def Multiplication(A: float, B: float) -> float:
    return A * B


def main():
    print("BogoSort, leader's role: DevOps, leader's github ID: mikoogla")
    print("BogoSort, role: developer, github ID: jacekdebski")
    print("BogoSort, role: tester, github ID: rfilipczak")
    print("BogoSort, role: DevOps, github ID: mikoogla")
    print("BogoSort, role: Developer, github ID: Mati-IR")

    print(f"2 + 3 = {Addition(2, 3)}")
    print("3 - 1 = ", Difference(3, 1))
    print(f'2 * 2 = {Multiplication(2, 2)}')
    print("6 / 3 = ", Division(6,3))

if __name__ == "__main__":
    main()