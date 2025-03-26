from typing import List
import logging

logger = logging.getLogger(__name__)

class FibonacciGenerator:
    """Генератор чисел Фибоначчи"""
    
    @staticmethod
    def generate(n: int) -> List[int]:
        """
        Генерирует первые n чисел Фибоначчи
        """
        if not isinstance(n, int):
            logger.error(f"Получен неверный тип данных: {type(n)}")
            raise ValueError("n должно быть целым числом")
            
        if n < 0:
            logger.error("Отрицательное число для генерации Фибоначчи")
            raise ValueError("n должно быть неотрицательным")
            
        if n > 1000:
            logger.error(f"Превышен лимит: {n}")
            raise ValueError("n не должно превышать 1000")
            
        if n == 0:
            return []
            
        result = [0, 1]
        if n <= 2:
            return result[:n]
            
        for _ in range(2, n):
            result.append(result[-1] + result[-2])
            
        logger.info(f"Сгенерировано {n} чисел Фибоначчи")
        return result
