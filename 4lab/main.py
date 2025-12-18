if __name__ == "__main__":

    class Shape:
        def area(self):
            return 0

        def perimeter(self):
            return 0

        def vertices(self):
            return 0

        def name(self):
            return "Фигура"



    class Triangle(Shape):
        def __init__(self, x1, y1, x2, y2, x3, y3):
            self.x1 = float(x1)
            self.y1 = float(y1)
            self.x2 = float(x2)
            self.y2 = float(y2)
            self.x3 = float(x3)
            self.y3 = float(y3)

        def area(self):

            return abs(
                (self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2)) / 2)

        def perimeter(self):

            import math
            a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
            b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
            c = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
            return a + b + c

        def vertices(self):
            return 3

        def name(self):
            return "Треугольник"



    class Rectangle(Shape):
        def __init__(self, x1, y1, x2, y2):
            self.x1 = float(x1)
            self.y1 = float(y1)
            self.x2 = float(x2)
            self.y2 = float(y2)

        def area(self):
            width = abs(self.x2 - self.x1)
            height = abs(self.y2 - self.y1)
            return width * height

        def perimeter(self):
            width = abs(self.x2 - self.x1)
            height = abs(self.y2 - self.y1)
            return 2 * (width + height)

        def vertices(self):
            return 4

        def name(self):
            return "Прямоугольник"



    class Circle(Shape):
        def __init__(self, x, y, r):
            self.x = float(x)
            self.y = float(y)
            self.r = float(r)

        def area(self):
            import math
            return math.pi * self.r * self.r

        def perimeter(self):
            import math
            return 2 * math.pi * self.r

        def vertices(self):
            return 0

        def name(self):
            return "Круг"



    class Polygon(Shape):
        def __init__(self, x, y, r, n):
            self.x = float(x)
            self.y = float(y)
            self.r = float(r)
            self.n = int(n)

        def area(self):
            import math

            return (self.n * self.r * self.r * math.sin(2 * math.pi / self.n)) / 2

        def perimeter(self):
            import math

            side = 2 * self.r * math.sin(math.pi / self.n)
            return side * self.n

        def vertices(self):
            return self.n

        def name(self):
            return f"Многоугольник({self.n}-угольник)"



    def main():
        shapes = []

        print("=== ПРОГРАММА ДЛЯ РАБОТЫ С ГЕОМЕТРИЧЕСКИМИ ФИГУРАМИ ===")
        print("Доступные команды для создания фигур:")
        print("  triangle x1 y1 x2 y2 x3 y3  - создать треугольник")
        print("  rectangle x1 y1 x2 y2       - создать прямоугольник")
        print("  circle x y r               - создать круг")
        print("  polygon x y r n            - создать правильный n-угольник")
        print("  done                       - закончить ввод фигур")
        print("  help                       - показать справку")
        print()

        while True:
            user_input = input("Введите команду: ").strip()

            if user_input == "done":
                break
            elif user_input == "help":
                print("Доступные команды для создания фигур:")
                print("  triangle x1 y1 x2 y2 x3 y3  - создать треугольник")
                print("  rectangle x1 y1 x2 y2       - создать прямоугольник")
                print("  circle x y r               - создать круг")
                print("  polygon x y r n            - создать правильный n-угольник")
                print("  done                       - закончить ввод фигур")
                continue

            parts = user_input.split()

            if len(parts) == 0:
                continue

            command = parts[0]

            try:
                if command == "triangle":
                    if len(parts) != 7:
                        print("Ошибка: нужно 6 чисел для треугольника")
                    else:
                        triangle = Triangle(parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
                        shapes.append(triangle)
                        print(f"Добавлен треугольник")

                elif command == "rectangle":
                    if len(parts) != 5:
                        print("Ошибка: нужно 4 числа для прямоугольника")
                    else:
                        rectangle = Rectangle(parts[1], parts[2], parts[3], parts[4])
                        shapes.append(rectangle)
                        print(f"Добавлен прямоугольник")

                elif command == "circle":
                    if len(parts) != 4:
                        print("Ошибка: нужно 3 числа для круга")
                    else:
                        circle = Circle(parts[1], parts[2], parts[3])
                        shapes.append(circle)
                        print(f"Добавлен круг")

                elif command == "polygon":
                    if len(parts) != 5:
                        print("Ошибка: нужно 4 числа для многоугольника")
                    else:
                        polygon = Polygon(parts[1], parts[2], parts[3], parts[4])
                        shapes.append(polygon)
                        print(f"Добавлен {parts[4]}-угольник")

                else:
                    print(f"Неизвестная команда: {command}")

            except ValueError:
                print("Ошибка: все параметры должны быть числами")

        print(f"\nВсего создано фигур: {len(shapes)}")


        if len(shapes) > 0:
            print("\nСозданные фигуры:")
            for i, shape in enumerate(shapes):
                print(
                    f"{i + 1}. {shape.name()}: площадь={shape.area():.2f}, периметр={shape.perimeter():.2f}, углов={shape.vertices()}")


        print("\n=== АНАЛИЗ ФИГУР ===")
        print("Доступные команды анализа:")
        print("  area      - общая площадь всех фигур")
        print("  perimeter - суммарный периметр всех фигур")
        print("  vertices  - суммарное количество углов")
        print("  all       - показать все характеристики")
        print("  exit      - выйти из программы")

        while True:
            command = input("\nВведите команду анализа: ").strip().lower()

            if command == "exit":
                print("Выход из программы...")
                break

            if len(shapes) == 0:
                print("Нет фигур для анализа!")
                continue

            if command == "area":
                total_area = 0
                for shape in shapes:
                    total_area += shape.area()
                print(f"Общая площадь всех фигур: {total_area:.2f}")

            elif command == "perimeter":
                total_perimeter = 0
                for shape in shapes:
                    total_perimeter += shape.perimeter()
                print(f"Суммарный периметр всех фигур: {total_perimeter:.2f}")

            elif command == "vertices":
                total_vertices = 0
                for shape in shapes:
                    total_vertices += shape.vertices()
                print(f"Суммарное количество углов: {total_vertices}")

            elif command == "all":
                total_area = 0
                total_perimeter = 0
                total_vertices = 0

                for shape in shapes:
                    total_area += shape.area()
                    total_perimeter += shape.perimeter()
                    total_vertices += shape.vertices()

                print(f"Общая площадь: {total_area:.2f}")
                print(f"Суммарный периметр: {total_perimeter:.2f}")
                print(f"Суммарное количество углов: {total_vertices}")

            else:
                print(f"Неизвестная команда: {command}")



if __name__ == "__main__":
    main()
