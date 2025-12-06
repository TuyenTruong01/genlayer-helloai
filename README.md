# HelloAI — GenLayer Python Smart Contract

This repository contains a simple smart contract written using the **GenLayer Python SDK**.  
The project demonstrates how to build, deploy, and interact with a minimal contract on **GenLayer Studio**.

---

## 🚀 Overview

**HelloAI** is a basic contract used for testing execution and deployment flows on GenLayer.  
It includes:

- A constructor that stores a name.
- A public view method `greet()` that returns a dynamic greeting.
- Full compatibility with **GenLayer Studio** and the Python-based contract framework.

The contract serves as a starter example for developers learning how to create Python smart contracts on GenLayer.

---

## 📜 Contract Source Code

```python
from genlayer import *

class HelloAI(gl.Contract):
    """Simple greeting contract for testing GenLayer Studio."""

    def __init__(self, name: str):
        self.name = name

    @gl.public.view
    def greet(self) -> str:
        return f"Hello {self.name}, from GenLayer!"
