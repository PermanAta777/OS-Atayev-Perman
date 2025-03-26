from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FibonacciGenerator:
    """Генератор чисел Фибоначчи"""
    
    @staticmethod
    def generate_fibonacci(n: int) -> List[int]:
        """
        Генерирует первые n чисел Фибоначчи
        
        Args:
            n: Количество чисел для генерации
            
        Returns:
            List[int]: Список чисел Фибоначчи
            
        Raises:
            ValueError: Если n отрицательное или не является целым числом
        """
        try:
            if not isinstance(n, int):
                raise ValueError("Input must be an integer")
            if n < 0:
                raise ValueError("Input must be non-negative")
            
            if n == 0:
                return []
                
            fib = [0, 1]
            if n <= 2:
                return fib[:n]
                
            for _ in range(2, n):
                fib.append(fib[-1] + fib[-2])
            return fib
            
        except ValueError as e:
            logger.error(f"Invalid input: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
