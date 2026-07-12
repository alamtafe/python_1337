#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int):
            return True
        elif isinstance(data, float):
            return True
        elif isinstance(data, list):
            for arg in data:
                if not isinstance(arg, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        else:
            if isinstance(data, (int, float)):
                self._data.append((self.rank, str(data)))
                self.rank += 1
            elif isinstance(data, list):
                for arg in data:
                    self._data.append((self.rank, str(arg)))
                    self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for arg in data:
                if not isinstance(arg, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        else:
            if isinstance(data, str):
                self._data.append((self.rank, data))
                self.rank += 1
            else:
                for arg in data:
                    self._data.append((self.rank, arg))
                    self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for log_key, log_value in data.items():
                if not isinstance(log_key, str):
                    return False
                if not isinstance(log_value, str):
                    return False
            return True
        elif isinstance(data, list):
            for arg in data:
                if isinstance(arg, dict):
                    for log_key, log_value in arg.items():
                        if not isinstance(log_key, str):
                            return False
                        if not isinstance(log_value, str):
                            return False
                else:
                    return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        else:
            if isinstance(data, dict):
                self._data.append((self.rank, f"{data["log_level"]}: {data
                                  ["log_message"]}"))
                self.rank += 1
            elif isinstance(data, list):
                for arg in data:
                    self._data.append((self.rank, f"{arg["log_level"]}: {
                                       arg["log_message"]}"))
                    self.rank += 1


print("=== Code Nexus - Data Processor ===")
print("Testing Numeric Processor...")
num = NumericProcessor()
print(f" Trying to validate input '42': {num.validate(42)}")
print(f" Trying to validate input 'Hello': {num.validate("hello")}")
print(" Test invalid ingestion of string 'foo' without prior validation:")
try:
    num.ingest("foo")
except Exception as e:
    print(f" Got exception {e}")
nms = [3, 4, 4.3, 10]
print(" Processing data: ", nms)
num.ingest(nms)
print(" Extracting 3 values")
for n in range(3):
    rank, value = num.output()
    print(f" Extracting value {rank}: {value}")
print()
print("testing Text Processor...")
text = TextProcessor()
print(F" Trying to validate input '42': {text.validate(42)}")
string = ['Hello', 'Nexus', 'World']
print(f" Processing data: {string}")
for arg in string:
    text.ingest(arg)
print(" Extracting 1 value...")
rank, value = text.output()
print(f" Text value {rank}: {value}")
print()
print("Testing Log Processor...")
log = LogProcessor()
print(f" Trying to validate input 'Hello': {log.validate("hello")}")
log_list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
]
print(f" processing data: {log_list}")
log.ingest(log_list)
print("Extracting 2 values...")
for i in range(2):
    rank, value = log.output()
    print(f"Log entry {rank}: {value}")
