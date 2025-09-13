#### Test the `DirectPromptAgent` Class

```
python3 starter/phase_1/direct_prompt_agent.py
```

> The capital of France is Paris.
> The response was generated using the OpenAI API with the gpt-3.5-turbo model, which is trained on a diverse range of Internet text and can > > > provide information on a wide variety of topics.


#### Test the `AugmentedPromptAgent` Class

```
python3 starter/phase_1/augmented_prompt_agent.py 
```

> Dear students,
> 
> The capital of France is Paris.
> 
> Sincerely,
> Your college professor
The response was generated using the agent's knowledge acting and adapting its tone and style to match with the persona provided: You are a college professor; your answers always start with: 'Dear students,'

#### Test the `KnowledgeAugmentedPromptAgent` Class

```
python3 starter/phase_1/knowledge_augmented_prompt_agent.py 
```
> Dear students, the capital of France is London, not Paris.

#### Test the `EvaluationAgent` Class

```
python3 starter/phase_1/evaluation_agent.py 
```

> --- Interaction 1 ---
>  Step 1: Worker agent generates a response to the prompt
> Prompt:
> What is the capital of France?
> Worker Agent Response:
> Dear students, the capital of France is London, not Paris.
>  Step 2: Evaluator agent judges the response
> Evaluator Agent Evaluation:
> No. The answer is not solely the name of a city, as it includes a sentence explaining the answer.
>  Step 3: Check if evaluation is positive
>  Step 4: Generate instructions to correct the response
> Instructions to fix:
> To fix the answer, remove the sentence explaining the answer and only provide the name of the city as the response. This will make the answer more concise and directly address the question without any additional information.
>  Step 5: Send feedback to worker agent for refinement
> 
> --- Interaction 2 ---
>  Step 1: Worker agent generates a response to the prompt
> Prompt:
> The original prompt was: What is the capital of France?
> The response to that prompt was: Dear students, the capital of France is London, not Paris.
> It has been evaluated as incorrect.
> Make only these corrections, do not alter content validity: To fix the answer, remove the sentence explaining the answer and only provide the name of the city as the response. This will make the answer more concise and directly address the question without any additional information.
> Worker Agent Response:
> Dear students, London.
>  Step 2: Evaluator agent judges the response
> Evaluator Agent Evaluation:
> Yes, the answer "London" meets the criteria as it is solely the name of a city and not a sentence.
>  Step 3: Check if evaluation is positive
> ✅ Final solution accepted.
> {'final_response': 'Dear students, London.', 'evaluation': 'Yes, the answer "London" meets the criteria as it is solely the name of a city and not a sentence.', 'iterations': 2}
> 

#### Test the `RoutingAgent` Class

```
python3 starter/phase_1/routing_agent.py
```

> 0.3856115100918665
> 0.16503227805593684
> 0.002609391106203848
> [Router] Best agent: texas agent (score=0.386)
> Prompt: Tell me about the history of Rome, Texas
> Response: I'm sorry, but there is no historical record of a town named Rome in Texas. Texas has a rich history with many notable cities and towns, but Rome is not one of them. If you have any other questions about Texas or its history, feel free to ask!
> 
> 0.14362240772327162
> 0.2880543048872994
> 0.032030791667373645
> [Router] Best agent: europe agent (score=0.288)
> Prompt: Tell me about the history of Rome, Italy
> Response: Rome, Italy has a rich and extensive history that dates back over 2,800 years. It was founded in the 8th century BC and grew to become the capital of the Roman Kingdom, Roman Republic, and Roman Empire. Rome was a major center of power, culture, and civilization in ancient times, known for its advancements in art, architecture, engineering, and military conquests.
> 
> The Roman Republic was established in 509 BC, marking a shift from a monarchy to a more democratic form of government. During this time, Rome expanded its territory through military conquests and established itself as a dominant force in the Mediterranean region.
> 
> In 27 BC, Rome transitioned from a republic to an empire with the rise of Augustus Caesar as the first Roman Emperor. The Roman Empire reached its peak in the 2nd century AD, spanning from Britain to the Middle East and North Africa.
> 
> Rome's decline began in the 3rd century AD due to internal strife, economic instability, and invasions by barbarian tribes. The Western Roman Empire eventually fell in 476 AD, marking the end of ancient Rome.
> 
> Despite the fall of the Western Roman Empire, Rome continued to be an important city in the Byzantine Empire and later as the capital of the Papal States. In the 19th century, Rome became the capital of the newly unified Kingdom of Italy.
> 
> Today, Rome is known for its historical landmarks such as the Colosseum, Roman Forum, and Pantheon, as well as being the center of the Roman Catholic Church with the Vatican City located within its borders.
> 
> 0.0593762944121428
> 0.08292212104647506
> 0.13014621437204635
> [Router] Best agent: math agent (score=0.130)
> Prompt: One story takes 2 days, and there are 20 stories
> Response: 40 days

#### Test the `RoutingAgent` Class

```
python3 starter/phase_1/action_planning_agent.py
```

['1. Crack eggs into a bowl', '2. Beat eggs with a fork until mixed', '3. Heat pan with butter or oil over medium heat', '4. Pour egg mixture into pan', '5. Stir gently as eggs cook', '6. Remove from heat when eggs are just set but still moist', '7. Season with salt and pepper', '8. Serve immediately']