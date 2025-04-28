def wave(people):
    array = []
    for i in range(len(people)):
        if people[i] == ' ':  # пропускаем пробелы
            continue
        waved = people[:i] + people[i].upper() + people[i + 1:]
        array.append(waved)
    return array
    # return [ people[:i] + people[i].upper() + people[i + 1:]  for i in range(len(people)) if people[i].isalpha()]




print(wave("hello")) #["Hello", "hEllo", "heLlo", "helLo", "hellO"])