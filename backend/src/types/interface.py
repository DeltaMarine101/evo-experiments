from dataclasses import dataclass

from dataclasses_json import dataclass_json
from python_to_typescript_interfaces import Interface


@dataclass_json
@dataclass
class TestMessage(Interface):
    name: str
    age: int
