#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number_of_origami = int(input("Ведите кол-во журавликов: "))

x = number_of_origami // 6

print(f"Петя\t{x}")
print(f"Катя\t{4 * x}")
print(f"Сережа\t{x}")