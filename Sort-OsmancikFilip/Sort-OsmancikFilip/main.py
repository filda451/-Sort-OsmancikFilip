#Generuje náhodné číslá
import random

#1. Vytvoření pole s 10 random přeházenými hodnotami od 0-100.
random_hodnota = [random.randint(0, 100) for random_hodnota in range (10)]
    
for hodnota in random_hodnota:
    print(hodnota) #Vypsání hodnoty

#2. Vytvoření bubble sortu
    def bubble_sort(numbers): #Je to funkce, která seřadí seznam čísel přes Bubble sort
        for i in range (len(numbers)): #Cyklus, který prochází seznam
            for j in range (len(numbers) - 1 - i): #Cyklus, který porovná prvky
                if numbers[j] > numbers[j + 1]:
                    #Zde se prohodí oba dva prvky
                    numbers[j], numbers[j + 1] = numbers[j]
                    #Vrátí zpátky už seřazený seznam
                    return numbers

numbers_list = [100, 99, 98, 97, 96, 95, 94] #Vypsal jsem čísla, které se budou seřazovat
sorted_numbers = bubble_sort(numbers_list)
print("Výpis listu:", sorted_numbers) #Výpis na závěr

#3. Vytvoření bogo sortu
def is_sorted(numbers): #Funkce, která zkontroluje
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
def bogo_sort(numbers): #Funkce, která přidá ten bogo sort
    while not is_sorted(numbers):
        random.shuffle(numbers) #Random se to prohodí (prostě zamíchá)
        return numbers #Vrátí zpátky už seřazený seznam
    
numbers_list = [1, 2, 3, 4, 5, 6, 7] #Vypsal jsem čísla, které se budou seřazovat
sorted_numbers = bogo_sort(numbers_list) #bogo sort
print("Výpis listu", sorted_numbers) #Výpis na závěr

#4. Zde jsem vytvořil selection sort
def selection_sort(numbers): #Zde se to vše seřadí, ty čísla
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i] #Prohodí se prvky

numbers_list = [50, 51, 52, 53, 54, 55, 56, 57] #Vypsal jsem čísla, které se budou seřazovat
selection_sort(numbers_list) #selection sort
print("Výpis listu:", numbers_list) #Výpis na závěr

#5. Zde jsem se pokusil vytvořit insertion sort :(
def insertion_sort(numbers):
    for i in range()

numbers_list = [10, 11, 12, 13, 14, 15, 16] #Vypsal jsem čísla, které se budou seřazovat
insertion_sort(numbers_list) #insertion sort
print("Výpis listu:", numbers_list) #Výpis na závěr