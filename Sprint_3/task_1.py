class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def get_name_items(self):
        return self.__name_items

    @property
    def get_number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        try:
            if len(name) > 40 or len(name) == 0:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            elif name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            self.__name_items.append(name)
            self.__number_items += 1
        except NameError as e:
            print(e)
        except ValueError as e:
            print(e)

    def delete_item_from_check(self, name):
        try:
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в чеке')
            self.__name_items.remove(name)
            self.__number_items -= 1
        except NameError as e:
            print(e)

    def check_amount (self):
        total = []
        for item in self.__name_items:
            if item in self.__item_price:
                total.append(self.__item_price[item])
        sum_total = sum(total)
        if len(total) > 10:
            sum_total *= 0.9
        return sum_total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item, tax in self.__tax_rate.items():
            if tax == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        if len(total) > 10:
            twenty_percent_nds = sum(total) * 0.18
        else:
            twenty_percent_nds = sum(total) * 0.2
        return twenty_percent_nds

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item, tax in self.__tax_rate.items():
            if tax == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        if len(total) > 10:
            ten_percent_nds = sum(total) * 0.09
        else:
            ten_percent_nds = sum(total) * 0.1
        return ten_percent_nds

    def total_tax(self):
        total = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total

    @staticmethod
    def get_telephone_number(telephone_number):
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        return f'+7{telephone_number}'