# Open Ai Swarm multi agent framework (Ollama)

Reviewed the Open Ai Swarm educational framework exploring ergonomic, lightweight multi-agent system.

## Changes
- Adapted to Ollama usage
- added simple tools ( web_search, ... )

## Install

Requires Python 3.10+

pip install git+https://github.com/rwickel/open-ai-swarm-.git

pip install -r setup.txt

## Usage

main.py
```python

client = Swarm()

def transfer_to_coding_agent():
    """Transfer to coding agent."""
    return coder_agent

def transfer_to_researcher():
    """Transfer to research agent to get up to date information."""
    return research_agent

def transfer_to_supervisor():
    """Transfer to supervisor agent."""
    return supervisor

supervisor = Agent(
    name="Supervisor",
    instructions="You are a helpful agent. Answer the objective or transfer to to other agent to come to concise answer. You have no up to date information.",
    model="qwen2.5:14b",
    functions=[transfer_to_coding_agent, transfer_to_researcher],
)

coder_agent = Agent(
    name="coder_agent",
    instructions="You are a highly skilled Python coder tasked with verifying the correctness and efficiency of code before responding to requests. Your primary task is to assist with research-related objectives. If the objective is not research-related, immediately transfer the request to the supervisor agent for appropriate handling.",
    model="qwen2.5:14b",
    functions=[execute_python_code, transfer_to_supervisor],
)

research_agent = Agent(
    name="researcher",
    instructions="You are an intelligent and efficient web researcher agent. Your primary task is to assist with web research-related objectives, such as gathering information from online sources or analyzing data. If the request involves coding problems, math calculations, or other technical problem-solving tasks, immediately transfer the request to the coding or math agent for appropriate handling. Always prioritize accuracy, efficiency, and clarity in delivering results.",
    model="qwen2.5:14b",
    functions=[web_search, date, transfer_to_supervisor, transfer_to_coding_agent],
)

if __name__ == "__main__":    
    run_demo_loop(supervisor, stream=False, context_variables=context_variables, debug=False) # make sure stream is false for tool usage  
```

```
command line:
Starting Swarm CLI
User: Hello
Supervisor: Hello! How can I assist you today?
```

## Table of Contents

- [Ollama](#ollama)
- [WorkFlow](#workFlow)


# Ollama Setup
Following changes are made to connect to local Ollama server:

![Swarm Logo](assets/ollama.png)

# WorkFlow
With the setup described above, we achieve the following workflow.

## Example
supervisor route to researcher agent:

![Swarm Logo](assets/researcher.png)

researcher route to coder agent:

![Swarm Logo](assets/coder.png)

back to researcher again:

![Swarm Logo](assets/switching.png)

## Example
Sometimes, the request is not routed to the related agent; additional user input is required.

![Swarm Logo](assets/temperature.png)







