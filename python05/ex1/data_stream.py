#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self.rank: int = 0
        self.total_items: int = 0

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
                self.total_items += 1
            elif isinstance(data, list):
                for arg in data:
                    self._data.append((self.rank, str(arg)))
                    self.rank += 1
                    self.total_items += 1


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
                self.total_items += 1
            else:
                for arg in data:
                    self._data.append((self.rank, arg))
                    self.rank += 1
                    self.total_items += 1


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
                self.total_items += 1
            elif isinstance(data, list):
                for arg in data:
                    self._data.append((self.rank, f"{arg["log_level"]}: {
                                       arg["log_message"]}"))
                    self.rank += 1
                    self.total_items += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for arg in stream:
            found = False
            for proc in self.processors:
                if proc.validate(arg):
                    proc.ingest(arg)
                    found = True
                    break
            if not found:
                print(f"DataStream error"
                      f"- Can't process element in stream {arg}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                print(f"{proc.__class__.__name__}"
                      f" total {proc.total_items} items"
                      f" processed, remaining {len(proc._data)}"
                      " on processor")


data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
]
print("=== Code Nexus - Data Stream ===")
print()
print("Initialize Data Stream...")
stream = DataStream()
stream.print_processors_stats()
print()
print("Registering Numeric Processor")
num = NumericProcessor()
stream.register_processor(num)
stream.process_stream(data)
stream.print_processors_stats()
print()
print("Registering other data processors")
text = TextProcessor()
log = LogProcessor()
stream.register_processor(text)
stream.register_processor(log)
print("Send the same batch again")
stream.process_stream(data)
stream.print_processors_stats()
print()
print("Consume some elements from the data processors:"
      " Numeric 3, Text 2, Log 1")
for i in range(3):
    num.output()
for i in range(2):
    text.output()
log.output()
stream.print_processors_stats()
