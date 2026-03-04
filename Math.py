import random
import math
import time

# =========================
# Power Modular this Binary Exponentiation
def power_modular(base, exponent, modular):
    result = 1
    base %= modular
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modular
        exponent //= 2
        base = (base * base) % modular
    return result

# =========================
# 1.make this function for Trial Division (Deterministic)
def trial_division(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# =========================
# 2. Fermat Primality Test 
def fermat_test(n, k=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if power_modular(a, n - 1, n) != 1:
            return False
    return True

# =========================
# 3. make this use for Miller-Rabin Primality Test 
def miller_rabin(n, k= 50):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    # write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power_modular(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = power_modular(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# =========================
# Main Program (User Input)
def main():
    while True:
        print("\nChoose Algorithm:")
        print("1. Trial Division")
        print("2. Fermat Test")
        print("3. Miller-Rabin Test")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "4":

            print("\nProgram exited.")
            break

        try:
            n = int(input("Enter a number to test: "))
            if n < 2:
                print("Number must be >= 2")
                continue
        except ValueError:
            print("Invalid input!")
            continue

        start = time.time()

        if choice == "1":
            result = trial_division(n)
            algorithm_name = "Trial Division"
        elif choice == "2":
            result = fermat_test(n)
            algorithm_name = "Fermat Test"
        elif choice == "3":
            result = miller_rabin(n)
            algorithm_name = "Miller-Rabin Test"
        else:
            print("Invalid choice!")
            continue

        elapsed = time.time() - start
        print("-"*50)
        print(f"\nAlgorithm: {algorithm_name}")
        print(f"Number: {n}")
        print(f"Result: {'PRIME' if result else 'COMPOSITE'}")
        print(f"Time: {elapsed:.20f} seconds\n")
        print("-" * 50)
        

# =========================
# program entry point
if __name__ == "__main__":
    main()
