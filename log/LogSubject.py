from log.LogObserver import LogObserver

class LogSubject:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(LogSubject, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.log_observers = []
            self.initialized = True

    def attach_log_observer(self, log_observer: LogObserver):
        self.log_observers.append(log_observer)

    def notify_log_observer(self, log_event: str):
        for log_observer in self.log_observers:
            log_observer.update_log(log_event)