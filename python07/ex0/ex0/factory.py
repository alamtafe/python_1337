#!/usr/bin/env python3
from abc import abstractmethod, ABC


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass
