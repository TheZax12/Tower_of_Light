from abc import ABC, abstractmethod


class LogObserver(ABC):
    
    @abstractmethod
    def update_log(self, event: str):
        pass