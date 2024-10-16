from swarm.repl import run_demo_loop
from swarm.types import Agent
from swarm.tools import web_search, date, execute_python_code, context_variables
from swarm import Swarm, Agent


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
    instructions="You are a helpful agent. Answer the objective or transfer to to other agent to come to concise answer. You have no up to date information. If the request involves a coding problems, math calculations, or other technical problem-solving tasks, immediately transfer the request to the coder agent.",
    model="qwen2.5:14b",
    functions=[transfer_to_coding_agent, transfer_to_researcher],
)

coder_agent = Agent(
    name="coder",
    instructions="You are a highly skilled Python coder tasked with verifying the correctness and efficiency of code before responding to requests. If the request involves not a coding problems, math calculations, or other technical problem-solving tasks, immediately transfer the request to the supervisor or research agent for appropriate handling. You have no up to date information",
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