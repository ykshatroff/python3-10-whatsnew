from typing import Union

old_style: Union[int, float] = 100

new_style: int | float = 100

assert isinstance(1, int | float)



