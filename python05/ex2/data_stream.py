#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


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
        if isinstance(data, (int, float)):
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
        if not self.processors:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                word = proc.__class__.__name__.replace(
                        'Processor', ' Processor')
                print(f"{word}"
                      f" total {proc.total_items} items"
                      f" processed, remaining {len(proc._data)}"
                      " on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            export_data: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc._data:
                    break
                export_data.append(proc.output())
            plugin.process_output(export_data)
            export_data = []


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        csv_values: list[str] = []
        for arg in data:
            csv_values.append(arg[1])
        print(",".join(csv_values))


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_values: list[str] = []
        for arg in data:
            rank, value = arg
            json_values.append(f'"item_{rank}": "{value}"')
        print(f'{{{", ".join(json_values)}}}')


print("=== Code Nexus - Data Pipeline ===")
print()
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
print("Initialize Data Stream...")
stream = DataStream()
stream.print_processors_stats()
print()
print("Registering Processors")
print(f"Send first batch of data on stream: {data}")
num = NumericProcessor()
text = TextProcessor()
log = LogProcessor()
stream.register_processor(num)
stream.register_processor(text)
stream.register_processor(log)
stream.process_stream(data)
stream.print_processors_stats()
print()
print("Send 3 processed data from each processor to a CSV plugin:")
csv_plugin = CsvPlugin()
stream.output_pipeline(3, csv_plugin)
stream.print_processors_stats()
second_data = [
                21,
                [
                    'I love AI', 'LLMs are wonderful',
                    'Stay healthy'
                ],
                [
                    {
                        'log_level': 'ERROR',
                        'log_message': '500 server crash'
                    },
                    {
                        'log_level': 'NOTICE',
                        'log_message':
                        'Certificate expires in 10 days'
                    }
                ],
                [
                    32, 42, 64,
                    84, 128, 168
                ],
                'World hello'
]
print(f"Send another batch of data: {second_data}")
stream.process_stream(second_data)
stream.print_processors_stats()
print("Send 5 processed data from each processor to a JSON plugin:")
json_plugin = JsonPlugin()
stream.output_pipeline(5, json_plugin)
stream.print_processors_stats()
