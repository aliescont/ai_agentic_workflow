# agentic_workflow.py

# TODO: 1 - DONE - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
from workflow_agents.base_agents import (ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent)

import os
from dotenv import load_dotenv

# TODO: 2 - DONE - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
# TODO: 3 - DONE - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
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
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(knowledge=knowledge_action_planning, openai_api_key=openai_api_key)
# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    f"""Make sure the stories are clear, concise, and cover all aspects of the product spec {product_spec}. """
    # TODO: 5 - REVIEW - Complete this knowledge string by appending the product_spec loaded in TODO 3
)
# TODO: 6 - DONE - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    persona=persona_product_manager,
    knowledge=knowledge_product_manager,
    openai_api_key=openai_api_key
)
# Product Manager - Evaluation Agent
persona_product_manager_eval = "You are a Product Manager evaluation agent. You review user stories to confirm they follow the expected structure"

evaluation_criteria_product_manager = f"""
    "Each user story must follow: 'As a [type of user], I want [an action or feature] so that [benefit/value].' "
    "Reject stories missing a persona, action, or value statement."""

product_manager_evaluation_agent = EvaluationAgent(
    persona=persona_product_manager_eval,
    evaluation_criteria=evaluation_criteria_product_manager,
    openai_api_key=openai_api_key,
    worker_agent=product_manager_knowledge_agent,
    max_interactions=5
)
# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
# knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
knowledge_program_manager = (
    f"Features of a product are defined by organizing similar user stories into cohesive groups"
    f"List each feature with: Feature Name, Description, Key Functionality, and User Benefit. "
    f"Use the product specification: {product_spec}"
)
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8 - DONE. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    persona=persona_program_manager,
    knowledge=knowledge_program_manager,
    openai_api_key=openai_api_key
)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."

# TODO: 8 - DONE Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
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
# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
# knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
knowledge_dev_engineer = (
    f"Development tasks are defined by identifying what needs to be built to implement each user story. "
    f"For the product specification: {product_spec}"
)
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(
    persona=persona_dev_engineer,
    knowledge=knowledge_dev_engineer,
    openai_api_key=openai_api_key
)
# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
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

def product_manager_support_function(query):
    response = product_manager_knowledge_agent.respond(query)
    evaluation_result = product_manager_evaluation_agent.evaluate(response)
    return evaluation_result["final_response"]

def program_manager_support_function(query):
    response = program_manager_knowledge_agent.respond(query)
    evaluation_result = program_manager_evaluation_agent.evaluate(response)
    return evaluation_result["final_response"]

def development_engineer_support_function(query):
    response = development_engineer_knowledge_agent.respond(query)
    evaluation_result = development_engineer_evaluation_agent.evaluate(response)
    return evaluation_result["final_response"]


# Routing Agent
# TODO: 10 - DONE - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.
routing_agent = RoutingAgent(
    agents=[
        {
            'name': 'Product Manager',
            'description': 'Creates user stories with personas, actions, and benefits. Generates stories in "As a [user], I want [feature] so that [benefit]" format.',
            'func': product_manager_support_function
        },
        {
            'name': 'Program Manager',
            'description': 'Groups user stories into product features. Defines Feature Name, Description, Key Functionality, and User Benefit for each feature.',
            'func': program_manager_support_function
        },
        {
            'name': 'Development Engineer',
            'description': 'Creates development tasks with Task ID, Task Title, Related User Story, Description, Acceptance Criteria, Estimated Effort, and Dependencies.',
            'func': development_engineer_support_function
        }
    ],
    openai_api_key=openai_api_key
)
# Job function persona support functions

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
workflow_prompt = """For the Email Router product:
1) As a Product Manager, generate user stories following the format 'As a [user], I want [feature] so that [benefit]'
2) As a Program Manager, define Feature Name, Description, Key Functionality, and User Benefit for each feature
3) As a Development Engineer, create development tasks with Task ID, Task Title, Related User Story, Description, Acceptance Criteria, Estimated Effort, and Dependencies."""
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
print(f"Extracted workflow steps: {workflow_steps}\n")
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

print("CONSOLIDATED PROJECT PLAN FOR EMAIL ROUTER \n")

print("1. USER STORIES \n")
print(completed_steps[0])
print("\n")
print("2. PRODUCT FEATURES \n")
print(completed_steps[1])
print("\n")

print("3. DEVELOPMENT TASKS \n")
print(completed_steps[2])