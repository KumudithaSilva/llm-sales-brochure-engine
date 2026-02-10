import os
import json
from dotenv import find_dotenv, load_dotenv
from logs.logger_singleton import Logger

class BaseUtils:
    def __init__(self):
        self.logger = Logger(name="BaseUtils")
        self.logger.info("BaseUtils initialized")
        
    def load_env_variables(self):
            try:
                dotenv_path = find_dotenv()
                if dotenv_path:
                    load_dotenv(dotenv_path)
                    self.logger.info(f".env file found and loaded from: {dotenv_path}")
                    return "env found"
                else:
                    self.logger.warning(".env file not found; using existing environment variables")
                    return "dotenv missing"
            except ImportError:
                self.logger.warning("python-dotenv not installed; using existing environment variables")
                return "dotenv missing"
            except Exception as e:
                self.logger.error(f"Error loading .env file: {e}")
                return f"error: {e}"

           