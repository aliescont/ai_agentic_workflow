# agentic_workflow.py

from workflow_agents.base_agents import (ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent)
from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
with open("Product-Spec-Email-Router.txt", "r") as file:
    product_spec = file.read()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
action_planning_agent = ActionPlanningAgent(knowledge=knowledge_action_planning, openai_api_key=openai_api_key)
# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    "Make sure the stories are clear, concise, and cover all aspects of the product spec {product_spec}. "
)
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    persona=persona_product_manager,
    knowledge=knowledge_product_manager,
    openai_api_key=openai_api_key
)
# Product Manager - Evaluation Agent
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
product_manager_evaluation_agent = EvaluationAgent(
    persona="You are a Product Manager evaluation agent.",
    evaluation_criteria="User stories should follow this structure: 'As a [type of user], I want [an action or feature] so that [benefit/value].'",
    openai_api_key=openai_api_key,
    worker_agent=product_manager_knowledge_agent,
    max_interactions=5
)
# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    persona=persona_program_manager,
    knowledge=knowledge_program_manager,
    openai_api_key=openai_api_key
)


# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."

program_manager_evaluation_agent = EvaluationAgent(
    persona=persona_program_manager_eval,
    evaluation_criteria="The answer should be product features that follow the following structure: " \
                         "Feature Name: A clear, concise title that identifies the capability\n" \
                         "Description: A brief explanation of what the feature does and its purpose\n" \
                         "Key Functionality: The specific capabilities or actions the feature provides\n" \
                         "User Benefit: How this feature creates value for the user",
    openai_api_key=openai_api_key,
    worker_agent=program_manager_knowledge_agent,
    max_interactions=5
)
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)

development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(
    persona=persona_dev_engineer,
    knowledge=knowledge_dev_engineer,
    openai_api_key=openai_api_key
)
# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
development_engineer_evaluation_agent = EvaluationAgent(
    persona=persona_dev_engineer_eval,
    evaluation_criteria="The answer should be tasks following this exact structure: " \
                         "Task ID: A unique identifier for tracking purposes\n" \
                         "Task Title: Brief description of the specific development work\n" \
                         "Related User Story: Reference to the parent user story\n" \
                         "Description: Detailed explanation of the technical work required\n" \
                         "Acceptance Criteria: Specific requirements that must be met for completion\n" \
                         "Estimated Effort: Time or complexity estimation\n" \
                         "Dependencies: Any tasks that must be completed first",
    openai_api_key=openai_api_key,
    worker_agent=development_engineer_knowledge_agent,
    max_interactions=5
)
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.

def product_manager_support_function(query):
    response = product_manager_knowledge_agent.respond(query)
    return product_manager_evaluation_agent.evaluate(response)

def program_manager_support_function(query):
    response = program_manager_knowledge_agent.respond(query)
    return program_manager_evaluation_agent.evaluate(response)

def development_engineer_support_function(query):
    response = development_engineer_knowledge_agent.respond(query)
    return development_engineer_evaluation_agent.evaluate(response)

# Routing Agent
routing_agent = RoutingAgent(
    agents=[
        {
            'name': 'Product Manager',
            'description': 'Handles product-related queries',
            'func': product_manager_support_function
        },
        {
            'name': 'Program Manager',
            'description': 'Handles program-related queries',
            'func': program_manager_support_function
        },
        {
            'name': 'Development Engineer',
            'description': 'Handles development-related queries',
            'func': development_engineer_support_function
        }
    ],
    openai_api_key=openai_api_key
)
# Job function persona support functions


def product_manager_support_function(query):
    response = product_manager_knowledge_agent.respond(query)
    return product_manager_evaluation_agent.evaluate(response)

def program_manager_support_function(query):
    response = program_manager_knowledge_agent.respond(query)
    return program_manager_evaluation_agent.evaluate(response)

def development_engineer_support_function(query):
    response = development_engineer_knowledge_agent.respond(query)
    return development_engineer_evaluation_agent.evaluate(response)

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = "What would the development tasks for this product be?"
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
#   2. Initialize an empty list to store 'completed_steps'.
completed_steps = []
#   3. Loop through the extracted workflow steps:
for step in workflow_steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
    result = routing_agent.route_prompt(step)
#      b. Append the result to 'completed_steps'.
    completed_steps.append(result)
#      c. Print information about the step being executed and its result.
    print(f"Executing step: {step}")
    print(f"Result: {result}")
#   4. After the loop, print the final output of the workflow (the last completed step).
print("\n*** Workflow execution completed ***\n")
print(f"Final output: {completed_steps[-1]}")