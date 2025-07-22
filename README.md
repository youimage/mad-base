# Lightweight Multi-Agent Framework (Abstracted Version)

---


## Overview

**MAD** is a lightweight and abstracted multi-agent framework implemented in Python.  
It supports asynchronous processing via `asyncio` and allows for easy creation and management of agents integrated with LLMs (Large Language Models) through a simple memory mechanism.

This repository is optimized for learning purposes and rapid prototyping.

---


## Key Features

- Asynchronous communication for message exchange between agents  
- Simple memory module for managing conversation history  
- Abstract base class for designing LLM integration interfaces  
- DummyLLM for testing with simple, mock responses  
- Configuration file for managing agent roles, names, and number of dialogue turns  

---


## ディレクトリ構成

lightmad/

├── agents/                  # Core agent implementations

│   ├── base_agent.py        # Abstract base class for agents

│   └── simple_agent.py      # Simple example implementation

├── llm/                     # LLM interface and implementations

│   ├── base_llm.py          # Abstract base class for LLMs

│   └── dummy_llm.py         # Dummy LLM for testing purposes

├── memory/                  # Memory management module

│   └── memory_module.py

├── communication.py         # Dialogue logic between agents

├── config.py                # Agent configuration settings

├── main.py                  # Entry point for execution

├── LICENSE

└── pyproject.toml

---


## Usage

1. Clone or download the repository  
2. Prepare Python 3.8 or higher  
3. Run `main.py` to start a sample conversation between two agents:

```bash
python lightmad/main.py
```


### Customization

- You can modify agent names, roles, and number of dialogue turns in `config.py`.  
- To create a new LLM implementation, extend the class in `llm/base_llm.py`.  
- To extend agent logic, edit `agents/base_agent.py` or `agents/simple_agent.py`.


### License

MIT License  
Please refer to the LICENSE file for details.

### Notice

This framework is intended for educational and prototyping purposes.  
Thorough validation and improvements are required for commercial use or large-scale system deployment.

If you have any questions or suggestions, feel free to open an Issue or Pull Request.
