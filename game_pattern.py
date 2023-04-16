class Game_pattern:
    def singleton_p(self):
        print("Очередной порождающий паттерн. С помощью него обеспечивается наличие единственного экземпляра класса"
              " с глобальной точкой доступа в однопоточном приложении.")
        print("Введите правильный ответ")
        right_answer = "singleton"
        answer = input()
        return right_answer, answer