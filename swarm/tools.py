from googlesearch import search
from datetime import datetime
import pytz
import json
import io
import contextlib

context_variables = {"name": "James", "user_id": 123}

def execute_python_code(input: str) -> str:
    """
    Executes Python code provided as a string and returns the output or error message. Use print() to output the result. 
    code = '''
        x = 5
        y = 10
        print(f'The sum of x and y is: {x + y}')
        '''    
    :param input: A string containing Python code to execute.
    :return: The output or error message from executing the Python code.
    """
    # Capture the standard output
    stdout = io.StringIO()
    
    try:
        # Redirect stdout to the StringIO object to capture print statements
        with contextlib.redirect_stdout(stdout):
            exec(input)
        
        # Fetch the standard output
        output = stdout.getvalue()
        if output == '':
            return "I executed your python code but the result is: ''. Use print() to output the variable or result!"  
        else:
            return f"python'''\n {input}\n'''\nPython code obtained this result: '''{output}'''."     

    except Exception as e:
        # In case of an exception, return the error message
        output = f"Error: {e}"
    finally:
        stdout.close()
    
    return f"I executed the python code and obtained this result: '''{output}'''."


def get_weather(location, time="now"):
    """Get the current weather in a given location. Location MUST be a city."""    
    return json.dumps({"location": location, "temperature": "65", "time": time})


def date(timezone='UTC'):
    """
    Get the current date and time. If a timezone is specified,
    return the time in that timezone.

    Parameters:
    - timezone (str): The timezone for which to get the current time (e.g., 'America/New_York').

    Returns:
    - str: Formatted current date and time.
    """
    if timezone:
        # Get the current time in the specified timezone
        tz = pytz.timezone(timezone)
        current_datetime = datetime.now(tz)
    else:
        # Get the current date and time in the local timezone
        current_datetime = datetime.now()

    return current_datetime.strftime("%B %d, %Y Time: %H:%M:%S")

def web_search(input: str):
    """
    Performs a web search for the given query and retrieves a list of search results.
    This function is useful when the language model encounters a question or query that requires up-to-date information, detailed data, or insights that are not readily available within the model's pre-existing knowledge base. The search results include URLs, titles, and descriptions of the relevant web pages.
    :param input: Input string of the objective.
    
    """    
    try:
        result_list = []
            
        # Perform the search and fetch the results
        results = list(search(input, advanced=True, num_results=3))
        
        for result in results:
            # Construct the result data
            result_data = {
                "source": result.url,
                "title": result.title,
                "description": result.description
            }
            result_list.append(result_data)
        
        # Return the search results
        return {"Tool Response": result_list, "Error": "", "Date":date()}
    
    except Exception as e:
        # Return the error message if an exception occurs
        return {"Tool Response": [], "Error": str(e), "Date":date()}
