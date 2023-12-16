def Addition(A: float, B: float) -> float:
    return A + B

def Difference(A: float, B: float) -> float:
    return A - B

def Multiplication(A: float, B: float) -> float:
    return A * B

# Main function
def main():
    print("BogoSort, leader's role: DevOps, leader's github ID: mikoogla")
    print("BogoSort, role: developer, github ID: jacekdebski")
    print("BogoSort, role: tester, github ID: rfilipczak")
    print("BogoSort, role: DevOps, github ID: mikoogla")
    print("BogoSort, role: Developer, github ID: Mati-IR")

    print(f"2 + 3 = {Addition(2, 3)}")
    print("3 - 1 = ", Difference(3, 1))
    print(f'2 * 2 = {Multiplication(2, 2)}')

if __name__ == "__main__":
    main()