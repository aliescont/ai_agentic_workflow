# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent  
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

direct_agent = DirectPromptAgent(openai_api_key)

direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

print(  "The response was generated using the OpenAI API with the gpt-3.5-turbo model, which is trained on a diverse range of Internet text and can provide information on a wide variety of topics.")
