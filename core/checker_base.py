from abc import ABC, abstractmethod
from typing import List
from core.package import Package

class CheckerBase(ABC):
    
    @abstractmethod
    def check_package(self, package_name: str) -> Package:
        pass
    
    @abstractmethod
    def list_installed(self) -> List[str]:
        pass
