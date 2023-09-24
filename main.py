def main():



   print("Введіть початок та кінець діапазону")

   start = int(input("Початок: "))

   end = int(input("Кінець: "))
   print("Усі числа, кратні 7:")

   for i in range(start, end + 1):

       if i % 7 == 0:
           print(i, end=" ")

   print()


if __name__ == "__main__":
    main()





