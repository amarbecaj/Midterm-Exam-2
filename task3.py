"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def main():
    def recur_sum(n):

        if n <= 1:
            return n
        else:
            return n + recur_sum(n - 1)

    num = int(input("Upisite broj: "))

    if num < 0:
        print("Unesite pozitivan broj: ")
    else:
        print("Suma je: ", recur_sum(num))

if __name__ == "__main__":
    main()


