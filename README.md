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

```python
class Swarm():
    def __init__(self, client=None):
        
        if not client:
            client = OpenAI()
        
        base_url='http://localhost:11434/v1/' 
        api_key="ollama"    
        self.client = OpenAI(base_url=base_url, api_key=api_key, timeout=20.0)
```

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

# Conclusion

## Pros
- Simplicity: The framework is particularly well-suited for simple problems, making it easier to implement and manage. Agents can focus on straightforward tasks without the complexities associated with multi-agent cooperation.

- Efficiency: Agents can quickly address tasks by leveraging their memory and specific tools, resulting in faster problem resolution. This efficiency reduces the time spent on task transitions and communication between agents.

- Contextual Awareness: The agent maintains its memory and context, allowing for continuity in problem-solving. This means it can build on previous interactions and refine its approach based on prior outcomes.

- Hierarchical Task Management: The framework allows for a clear delineation of responsibilities. When a request falls outside the agent's expertise, it can seamlessly transfer the task to a supervisor or a specialized research agent, ensuring that each request is handled by the most appropriate entity.

- Scalability: The framework can be expanded to include additional agents or tools as needed, allowing for greater flexibility and adaptability to varying problem types.

## Cons
- Limited Problem Scope: The framework is primarily designed for simple problems. More complex issues may require multiple agents to cooperate, which the current structure does not support effectively.

- Dependency on Context: The agent's effectiveness is heavily reliant on maintaining the same context. If the context changes, the agent may struggle to adapt, leading to inefficiencies or errors in problem-solving.

- Reduced Flexibility: While the hierarchy of task management is beneficial, it can also create bottlenecks. If the supervisor or research agent is unavailable or slow to respond, it may hinder the overall responsiveness of the system.

- Single-Point Failure: Relying on a single agent to handle specific tasks can lead to vulnerabilities. If the agent encounters an unexpected issue, it may not have the resources to address it, resulting in a potential failure to resolve the request.

- Memory Limitations: Although the agent retains memory, there may be constraints on how much information it can store or recall, which could affect its performance in more nuanced or extended problem-solving scenarios.



