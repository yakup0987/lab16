"""
Конфигурационный файл для проекта.
Содержит настройки для работы с Context7.
"""

# Настройки API
API_URL = "https://api.context7.example.com/v1"
API_TIMEOUT = 30  # секунды

# Настройки логирования
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Настройки кэширования
CACHE_ENABLED = True
CACHE_TTL = 3600  # время жизни кэша в секундах

def get_config():
    """Возвращает все настройки в виде словаря."""
    return {
        "api": {
            "url": API_URL,
            "timeout": API_TIMEOUT
        },
        "logging": {
            "level": LOG_LEVEL,
            "format": LOG_FORMAT
        },
        "cache": {
            "enabled": CACHE_ENABLED,
            "ttl": CACHE_TTL
        }
    }

if __name__ == "__main__":
    import json
    print(json.dumps(get_config(), indent=4)) 