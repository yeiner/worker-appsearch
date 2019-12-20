from abc import ABC, abstractmethod

class CommandBase(ABC):
    """docstring for ComandBase.
        Clase base con la estructura de un comando."""

    def __init__(self, arguments):
        self.arguments = arguments

    def get_arguments(self):
        """Se obtienen los argumentos del comando."""
        return self.arguments

    @abstractmethod
    def exe_command(self):
        """Este methodo ejecuta el comando."""
        pass
