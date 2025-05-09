import modules_of_functions as m

def display_menu():
    print("\nSelect an option:")
    print("1. Spy Number")
    print("2. Sum of Digits")
    print("3. Product of Digits")
    print("4. Count Digits in Number")
    print("5. Check Perfect Square")
    print("6. Prime Factors of a Number")
    print("7. Count Prime Digits")
    print("8. Sum of Squares of First N Natural Numbers")
    print("9. Sum of Digits of Factorial")
    print("10. Count Zero Digits")
    print("11. Transpose of Matrix")
    print("12. Subtraction of Two Matrices")
    print("13. Number Divisible by 5")
    print("14. Area of Circle")
    print("15. Area of Triangle")
    print("16. Area of Square")
    print("17. Repeated Word in String")
    print("18. HCF & LCM")
    print("19. GCD & LCM")
    print("20. Reverse of Number")
    print("0. Exit")

while True:
    display_menu()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print(m.spy_numbers())
    elif choice == 2:
        print(m.sum_of_digits())
    elif choice == 3:
        print(m.product_of_digits())
    elif choice == 4:
        print(m.count_digits_in_a_number())
    elif choice == 5:
        print(m.check_if_a_number_is_a_perfect_square())
    elif choice == 6:
        print(m.find_prime_factors_of_a_number())
    elif choice == 7:
        print(m.count_number_of_prime_digits_in_a_number())
    elif choice == 8:
        print(m.sum_of_square_of_first_n_natural_numbers())
    elif choice == 9:
        print(m.sum_of_digits_of_factorial_of_a_number())
    elif choice == 10:
        print(m.count_zero_digits_in_a_number())
    elif choice == 11:
        print(m.find_transpose_of_a_matrice())
    elif choice == 12:
        print(m.subtraction_of_two_matrices())
    elif choice == 13:
        print(m.number_divisible_by_5())
    elif choice == 14:
        print(m.area_of_circle())
    elif choice == 15:
        print(m.area_of_triangle())
    elif choice == 16:
        print(m.area_of_square())
    elif choice == 17:
        print(m.repeated_word_in_string())
    elif choice == 18:
        print(m.hcf_lcm_of_two_numbers())
    elif choice == 19:
        print(m.gcd_lcm_of_two_numbers())
    elif choice == 20:
        print(m.reverse_of_number())
    elif choice == 0:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
