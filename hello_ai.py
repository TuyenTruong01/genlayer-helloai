from genlayer import *

class HelloAI(gl.Contract):
    """Simple greeting contract for testing GenLayer Studio."""

    def __init__(self, name: str):
        self.name = name

    @gl.public.view
    def greet(self) -> str:
        return f"Hello {self.name}, from GenLayer!"
