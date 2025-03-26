import logging

logger = logging.getLogger(__name__)

class PalindromeChecker:
    """Проверка числа на палиндром"""
    
    @staticmethod
    def is_palindrome(number: int) -> bool:
        """
        Проверяет, является ли число палиндромом
        """
        if not isinstance(number, int):
            logger.error(f"Получен неверный тип данных: {type(number)}")
            raise ValueError("Должно быть целое число")
            
        if number < 0:
            logger.error("Отрицательное число для проверки палиндрома")
            raise ValueError("Число должно быть неотрицательным")
            
        num_str = str(number)
        result = num_str == num_str[::-1]
        logger.info(f"Проверка палиндрома для {number}: {result}")
        return result
