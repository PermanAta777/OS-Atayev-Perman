import logging

logger = logging.getLogger(__name__)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value: int):
        """Добавление элемента в конец списка"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def reverse(self) -> None:
        """Итеративный разворот связного списка"""
        if not self.head:
            logger.error("Попытка развернуть пустой список")
            raise ValueError("Список пуст")
            
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
        logger.info("Список успешно развернут")
        
    def to_list(self) -> list:
        """Преобразование в список для тестирования"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
