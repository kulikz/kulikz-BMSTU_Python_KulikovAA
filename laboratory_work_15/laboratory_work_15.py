import ctypes

my_variable = 42
print(f"Значение переменной: {my_variable}")

addres_my_variable = id(my_variable)
print(f"Адрес объекта переменной: {hex(addres_my_variable)}")

object_by_adress = ctypes.cast(addres_my_variable, ctypes.py.object)
print(f"Объект по адресу: {object_by_adress}")
print(f"Значение переменной: {object_by_adress.value}")

my_list =[]
print(f"Размер списка из {len(my_list)} элементов: ", )
