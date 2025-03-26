class PalindromeChecker:
    """Проверка числа на палиндром"""
    
    @staticmethod
    def is_palindrome(number: int) -> bool:
        """
        Проверяет, является ли число палиндромом
        
        Args:
            number: Число для проверки
            
        Returns:
            bool: True если палиндром, False иначе
            
        Raises:
            ValueError: Если входные данные некорректны
        """
        try:
            if not isinstance(number, int):
                raise ValueError("Input must be an integer")
            if number < 0:
                raise ValueError("Negative numbers are not supported")
                
            return str(number) == str(number)[::-1]
            
        except ValueError as e:
            logger.error(f"Invalid input: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
