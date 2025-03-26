class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    """Односвязный список с методом разворота"""
    
    def __init__(self):
        self.head = None
    
    def append(self, value: int) -> None:
        """Добавление элемента в конец списка"""
        if not self.head:
            self.head = Node(value)
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
    
    def reverse(self) -> None:
        """
        Итеративный разворот связного списка
        
        Raises:
            ValueError: Если список пуст
        """
        try:
            if not self.head:
                raise ValueError("Cannot reverse empty list")
                
            prev = None
            current = self.head
            
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            self.head = prev
            
        except Exception as e:
            logger.error(f"Error reversing list: {e}")
            raise
    
    def to_list(self) -> List[int]:
        """Конвертация в список для удобства тестирования"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
