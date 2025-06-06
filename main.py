import config
from utils import helper_function

class Context7Service:
    def __init__(self, api_key):
        self.api_key = api_key
        print(f"Context7Service инициализирован с API ключом: {self.api_key[:5]}...")

    def get_documentation(self, library_name: str, topic: str = None):
        """Получает документацию для указанной библиотеки."""
        # Улучшенный вывод информации
        print(f"[INFO] Запрос документации для библиотеки: {library_name}, тема: {topic if topic else 'общая'}")
        # Здесь могла бы быть реальная логика запроса к Context7
        return f"Документация по {library_name} (тема: {topic if topic else 'общая'}) ...содержимое..."

    def analyze_code_snippet(self, code: str):
        """Анализирует фрагмент кода с помощью Context7."""
        print(f"Анализ фрагмента кода: {code[:30]}...")
        # Здесь могла бы быть реальная логика анализа
        return "Анализ кода завершен. Замечаний не найдено."

    def validate_api_key(self):
        """Проверяет валидность API ключа."""
        if len(self.api_key) < 10:
            print("[WARNING] API ключ слишком короткий!")
            return False
        return True

if __name__ == "__main__":
    # Пример использования
    # Для реального использования API ключ нужно получить от сервиса Context7
    # и безопасно его хранить, например, в переменных окружения.
    service = Context7Service(api_key="YOUR_CONTEXT7_API_KEY_HERE")

    # Проверка валидности ключа
    is_valid = service.validate_api_key()
    print(f"API ключ валиден: {is_valid}")

    doc = service.get_documentation(library_name="requests", topic="Quickstart")
    print(f"Получена документация: {doc}")

    analysis_result = service.analyze_code_snippet("import os\nprint(os.getenv('HOME'))")
    print(f"Результат анализа кода: {analysis_result}")

    print("Программа успешно завершена.") 