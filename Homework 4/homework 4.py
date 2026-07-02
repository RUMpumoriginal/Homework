from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None:
        ...

def render(shape: Drawable) -> None:
    shape.draw()


class Circle:
    def draw(self) -> str:
        return "Circle"


class Square:
    def draw(self) -> str:
        return "Square"


render(Circle())
render(Square())