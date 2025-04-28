def in_array(array1, array2):

    array3 = []
    for i in array1:
        for j in array2:
            if i in j:
                array3.append(i)


    return sorted(set(array3))

# def in_array(array1, array2):
#     # Используем list comprehension для того, чтобы найти подстроки
#     array3 = [i for i in array1 if any(i in j for j in array2)]
#     return sorted(set(array3))  # Убираем дубли и сортируем

print(in_array(["arp", "live", "strong"],["lively", "alive", "harp", "sharp", "armstrong"] )) # ["arp", "live", "strong"]
print(in_array(["tarp", "mice", "bull"],  ["lively", "alive", "harp", "sharp", "armstrong"])) # []
