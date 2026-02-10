from abc import ABCMeta, abstractmethod
import logging
import threading


class SingletonMeta(metaclass=ABCMeta):
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass


class Logger(BaseLogger):

    def __init__(self, name="Singleton_Logger"):
        # Set up the logger
        print("Initializing logger")
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)

        # Create file handler and set its level to DEBUG
        file_handler = logging.FileHandler("basic_file.log")
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formater and add it to both handlers
        formater = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formater)
        console_handler.setFormatter(formater)

        # Add the handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)