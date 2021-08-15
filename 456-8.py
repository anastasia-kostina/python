def add_item(items, name, model, count):
    """ Добавляет в список словарей данные об оргтехнике.

    items -- список, содержащий информацию об оргтехнике (list[dict{}])
    name -- название фирмы-производителя (str)
    model -- название модели (str)
    count-- количество (int)

    возвращает items (list[dict{}])
    """

    k1 = 0
    l1 = 0
    l2 = 0
    for el3 in items:
        eq_name1 = el3.get(name)
        if eq_name1:
            l2 += 1
            d1 = eq_name1.get('model')
            for el4 in d1:
                if el4 == model:
                    a1 = eq_name1.get('count')
                    a1[k1] += count
                    l1 += 1
                k1 = k1 + 1
            if l1 == 0:
                d1.append(model)
                a1 = eq_name1.get('count')
                a1.append(count)
    if l2 == 0:
        items.append({name: {'model': [model], 'count': [count]}})

    return items


class Storage:
    # словарь, содержащий информацию о хранящейся на складе оргтехнике
    equipment_dict = {'printer': [], 'xerox': [], 'scaner': []}
    # список, хранящий информацию о принтерах, переданных в подразделение  "Принтеры"
    printer_subdivision = [{'Siemens': {'model': ['EP_123'], 'count': [100]}}]
    # список, хранящий информацию о сканерах, переданных в подразделение  "Сканеры"
    scaner_subdivision = [{'Canon': {'model': ['Can_1'], 'count': [200]}}]
    # список, хранящий информацию о ксероксах, переданных в подразделеление "Ксероксы"
    xerox_subdivision = [{'HP': {'model': ['Jet_Pro'], 'count': [10]}}]

    # метод, принимающий оргтехнику на склад
    @classmethod
    def storage_to(cls, eq_type, name, model, count):
        # проверка, что count - целое число
        try:
            int(count)
            # если проверка пройдена, отправляем на склад count единиц техники
            equipment_type = cls.equipment_dict.get(eq_type)
            if eq_type in cls.equipment_dict:
                add_item(equipment_type, name, model, count)
            print(cls.equipment_dict)
        except:
            print("Field 'count' must be of type 'int'")

    # метод, отправляющий оргтехнику в подразделения "Принтеры", "Ксероксы", "Сканеры"
    @classmethod
    def storage_from(cls, eq_type, name, model, count):
        k = 0
        l1 = 0
        l2 = 0
        # проверка, что count - целое число
        try:
            int(count)
            # если проверка пройдена, то отправляем в соответсвующее подразделение count единиц техники и удаляем их со
            # склада
            equipment_type = cls.equipment_dict.get(eq_type)
            if equipment_type:
                for el in equipment_type:
                    equipment_name = el.get(name)
                    if equipment_name:
                        l2 += 1
                        d = equipment_name.get('model')
                        for el2 in d:
                            if el2 == model:
                                a = equipment_name.get('count')
                                if a[k] >= count:
                                    a[k] -= count
                                    if eq_type == 'printer':
                                        add_item(cls.printer_subdivision, name, model, count)
                                        print(cls.printer_subdivision)
                                    if eq_type == 'xerox':
                                        add_item(cls.xerox_subdivision, name, model, count)
                                        print(cls.xerox_subdivision)
                                    if eq_type == 'scaner':
                                        add_item(cls.scaner_subdivision, name, model, count)
                                        print(cls.scaner_subdivision)
                                    l1 += 1
                                else:
                                    print(f"На складе нет {count} единиц техники!")
                                    return
                            k = k + 1
                        if l1 == 0:
                            print("Данная модель не присутствует на складе")
                            return
                if l2 == 0:
                    print("Данная модель не присутствует на складе")
                    return
            print(cls.equipment_dict)
        except:
            print("Field 'count' must be of type 'int'")


class Equipment:
    def __init__(self, eq_type, name, model, count):
        self.eq_type = eq_type
        self.model = model
        self.name = name
        self.count = count


class Printer(Equipment):
    def __init__(self, eq_type, name, model, count, color, type_p):
        super().__init__(eq_type, name, model, count)
        self.color = color
        self.type = type_p
        is_Print = self.eq_type == 'printer'

        if is_Print:
            try:
                count1 = int(self.count)
                print(f'Принтер {name} {model}, количество {count1}, печать {color}, тип {type_p}')
                Storage.storage_to(eq_type, name, model, count1)
            except:
                print("Field 'count' must be of type 'int'")
        else:
            print("Field 'eq_type' must be 'printer'.")


class Xerox(Equipment):
    def __init__(self, eq_type, name, model, count, copy_rate, resource):
        super().__init__(eq_type, name, model, count)
        self.copy_rate = copy_rate
        self.resource = resource
        is_Xerox = self.eq_type == 'xerox'

        if is_Xerox:
            try:
                count1 = int(self.count)
                int(self.copy_rate)
                int(self.resource)
                print(f'Ксерокс {name} {model}, количество {count1}, скорость копирования {copy_rate} коп/мин, '
                      f'ресурс {resource} коп/день')
                Storage.storage_to(eq_type, name, model, count1)
            except:
                print("Fields 'count', 'copy_rate', 'resource' must be of type 'int'")
        else:
            print("Field 'eq_type' must be 'xerox'.")


class Scaner(Equipment):
    def __init__(self, eq_type, name, model, count, kind):
        super().__init__(eq_type, name, model, count)
        self.kind = kind
        is_Scan = self.eq_type == 'scaner'

        if is_Scan:
            try:
                count1 = int(self.count)
                print(f'Сканер {name} {model}, количество {count1}, тип {kind}')
                Storage.storage_to(eq_type, name, model, count1)
            except:
                print("Field 'count' must be of type 'int'")
        else:
            print("Field 'eq_type' must be 'scaner'.")


printer1 = Printer('printer', 'Siemens', 'EP_123', 'd', 'black-and-white', 'laser')
print(" ")
printer2 = Printer('printer', 'Siemens', 'EP_123', 4, 'black-and-white', 'laser')
printer3 = Printer('printer', 'Siemens', 'NM_21', 5, 'color', 'jet')
print(" ")
xerox1 = Xerox('xerox', 'kyocera', 'taskalfa', 15, 20, 100)
print(" ")
scaner1 = Scaner('scaner', 'HР', 'DJ_1550', 20, 'planchete')
print(" ")
Storage.storage_from('printer', 'Siemens', 'EP_123', 500)
Storage.storage_from('printer', 'LG', '423', 500)
print(" ")
Storage.storage_from('printer', 'Siemens', 'EP_123', 2)
print(" ")
Storage.storage_from('xerox', 'kyocera', 'taskalfa', 2)
print(" ")
Storage.storage_from('scaner', 'HР', 'DJ_1550', 5)




