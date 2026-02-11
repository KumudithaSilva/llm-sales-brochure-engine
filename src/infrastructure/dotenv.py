from dotenv import find_dotenv, load_dotenv
from interfaces.i_env_loader import IEnvLoader
from logs.logger_singleton import Logger

class DotEnvLoader(IEnvLoader):
    """
    Base DotEnvLoader class for loadenvironment variable.
    """
    def __init__(self):
        """
        Initialize the DotEnvLoader class and configure the logger.
        """
        self.logger = Logger(self.__class__.__name__)
    
    def load_env_variables(self) -> None:
            """
            Load environment variables from a .env file if present.
            """
            try:
                dotenv_path = find_dotenv()
                if dotenv_path:
                    load_dotenv(dotenv_path)    
                    self.logger.info(f".env file found and loaded from: {dotenv_path}")
                else:
                    self.logger.warning(".env file not found; using existing environment variables")
            except ImportError:
                self.logger.warning("python-dotenv not installed; using existing environment variables")
            except Exception as e:
                self.logger.error(f"Error loading .env file: {e}")