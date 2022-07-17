from abc import ABC, abstractmethod
from typing import List

import numpy as np

from dto.Pcd import Pcd


class Associator(ABC):
    def __init__(self):
        pass

    @staticmethod
    def array_to_string(array: np.array) -> str:
        channels = [str(num) for num in array]
        string = "#".join(channels)

        return string

    @abstractmethod
    def associate(self, pcd_s: List[Pcd]):
        pass
