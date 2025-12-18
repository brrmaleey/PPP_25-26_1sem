import os


if __name__ == "__main__":
    def explore_directory(path=".", level=0):
        items = os.listdir(path)

        for item in items:
            full_path = os.path.join(path, item)

            indent = "  " * level

            if os.path.isdir(full_path):
                print(f"{indent} {item}/")
                explore_directory(full_path, level + 1)
            else:
                print(f"{indent} {item}")


    def collect_directory_structure(path="."):
        structure = []
        items = os.listdir(path)

        for item in items:
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                folder_info = {
                    "name": item,
                    "type": "directory",
                    "path": full_path,
                    "content": collect_directory_structure(full_path)
                }
                structure.append(folder_info)
            else:
                file_info = {
                    "name": item,
                    "type": "file",
                    "path": full_path
                }
                structure.append(file_info)

        return structure


    if __name__ == "__main__":
        print("=== ОБХОД ДИРЕКТОРИЙ И ФАЙЛОВ ===")
        print("\n1. Дерево каталогов:")

        start_path = input("Введите путь к папке (нажмите Enter для текущей): ").strip()
        if not start_path:
            start_path = "."

        if not os.path.exists(start_path):
            print("Ошибка: такой папки не существует!")
        else:
            explore_directory(start_path)

            print("\n2. Сохраненная структура:")
            directory_structure = collect_directory_structure(start_path)


            def print_structure(struct, level=0):
                indent = "  " * level
                for item in struct:
                    if item["type"] == "directory":
                        print(f"{indent} {item['name']}/")
                        print_structure(item["content"], level + 1)
                    else:
                        print(f"{indent} {item['name']}")


            print_structure(directory_structure)

            # Простая статистика
            print("\n3. Статистика:")


            def count_items(struct):
                folders = 0
                files = 0
                for item in struct:
                    if item["type"] == "directory":
                        folders += 1
                        sub_folders, sub_files = count_items(item["content"])
                        folders += sub_folders
                        files += sub_files
                    else:
                        files += 1
                return folders, files


            total_folders, total_files = count_items(directory_structure)
            print(f"Всего папок: {total_folders}")
            print(f"Всего файлов: {total_files}")
