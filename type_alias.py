from typing import TypeAlias

MyType: TypeAlias = "dict[int, str]"

my_var: MyType = {1: "one"}

assert MyType == "dict[int, str]"
