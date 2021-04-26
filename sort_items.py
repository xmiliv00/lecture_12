import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    #file_path = os.path.join(cwd_path, file_name)
    with open(file_name, 'r', encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter ='\t')
            for line in reader:
                row = [int(number) for number in line]
            return row
                #for number in line: druga mogucnost-isto radi(ovo je 2 for ciklus)
                    #row.append(int(number))



def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    with open(file_name, 'r', encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file) #vec su tam carky u csv,delimiter smazeme
            for line_idx,line in enumerate(reader):
                if line_idx == row_number:
                    row = [int(number) for number in line]
            return row


def selection_sort(number_array,direction):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    #hlavni cyklus prochazeni sekvence
    for count, _ in enumerate(number_array):
        extreme_ind = count
        for num_idx,number in enumerate(number_array[count:]):
            if direction == "ascending":
                 if number < number_array[extreme_ind]: #ako ovde promenim u < ,bude sestupne
                     extreme_ind = num_idx + count
            elif direction == "descending":
                if number > number_array[extreme_ind]:  # ako ovde promenim u < ,bude sestupne
                    extreme_ind = num_idx + count

        number_array[count],number_array[extreme_ind] = number_array[extreme_ind], number_array[count]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    for idx in range(len(number_array)-1):
        for idx_inner in range(0,len(number_array) - 1 - idx):
            if number_array[idx_inner] > number_array[idx_inner + 1]:
                number_array[idx_inner],number_array[idx_inner + 1] = number_array[idx_inner + 1],number_array[idx_inner]

    return number_array
def main():

    # Ukol: Selection Sort
    file_name = 'numbers_one.csv'
    row_numbers = read_row(file_name)
    sorted_numbers = selection_sort(row_numbers,"ascending")
    #print(sorted_numbers)
    #print(row_numbers)

    # Ukol: Selection Sort - se smerem razeni
    selected_row = read_rows("numbers_two.csv", 2)
    #print(selected_row)

    # Ukol: Bubble Sort
    sorted_sel_row = bubble_sort(selected_row)
    print(sorted_sel_row)

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

