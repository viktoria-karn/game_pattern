class Game_pattern:
    def check_answer(self, right_answer, answer):
        if right_answer == answer:
            print("Это правильный ответ!")
            return 0
        else:
            print("Это неправильный ответ!")
            return 1
    def singleton_p(self):
        print("Очередной порождающий паттерн. С помощью него обеспечивается наличие единственного экземпляра класса"
              " с глобальной точкой доступа в однопоточном приложении.")
        print("Введите правильный ответ")
        right_answer = "singleton"
        answer = input()
        return right_answer, answer
    def builder_p(self):
        print("Полезный порождающий паттерн, который, по сути, является методом создания составного объекта."
              "Он дифференцирует сложный объект на конструирование и представление."
              "Благодаря этому при выполнении одной и той же операции конструирования вы можете "
              "получить разные представления.")
        print("Введите правильный ответ")
        right_answer = "builder"
        answer = input()
        return right_answer, answer