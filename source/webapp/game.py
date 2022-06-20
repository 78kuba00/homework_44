class Game:
        
    def play(number_guess_list, number_computer_list):
        cow_numbers, bull_numbers = [], [] #два пустых списка скотины
        try: #пытаемся 
            for index in range(len(number_guess_list)):#в диапазоне загадонной комбинации 
                if number_computer_list[index] == int(number_guess_list[index]):#начиная с первой цифры сравниваем на схожесть если да то бык
                    bull_numbers.append(index)
                elif int(number_guess_list[index]) in number_computer_list:#если первое условие не сработало (быки) то второе условие проверяется и если оно сработало тогда это корова
                    cow_numbers.append(index)
            return cow_numbers, bull_numbers #возвращяем эррэй скотины
        except:
            return cow_numbers, bull_numbers
        
    def is_valid_count(number_list):
        if len(number_list) == 4:
            return True
        return False

    def is_unique_numbers(number_list):
        s = set() #создаем пустой лист/обьект
        for x in number_list:
            if x in s: #проверяем цифру (х) на наличие
                return False #проходимся по списку на уникальность 
            s.add(x)#если нету то добавляем аналог аппенд
        return True

    def is_valid_range(number_list):
        for x in number_list:
            if int(x) < 1 or int(x) > 9: 
                return False
        return True