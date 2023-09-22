# def get_home_remedies(disease):

#     remedies = {
#         'cold': [
#             'Drink warm tea with honey.',
#             'Get plenty of rest.',
#             'Stay hydrated with water and clear soups.',
#             'Use saline nasal drops to relieve congestion.'
#         ],
#         'headache': [
#             'Take a break from the screen and rest in a quiet room.',
#             'Apply a cold compress to your forehead.',
#             'Stay hydrated by drinking water.',
#             'Consider over-the-counter pain relievers like ibuprofen.'
#         ],
#         'fever': [
#             'Rest and stay in a cool room.',
#             'Stay hydrated by drinking water, clear fluids, or oral rehydration solutions.',
#             'Use a damp cloth to cool your body by applying it to your forehead, arms, and legs.'
#         ],
#         'sore throat': [
#             'Gargle with warm salt water.',
#             'Stay hydrated with soothing beverages like tea with honey or warm broth.',
#             'Consider over-the-counter throat lozenges or sprays for pain relief.'
#         ],
#         'stomach ache': [
#             'Avoid spicy and fatty foods.',
#             'Eat small, bland meals like rice, bananas, applesauce, and toast (BRAT diet).',
#             'Consider over-the-counter antacids or medications for relief.'
#         ],

#     }
# def is_disease(input_text):
#     known_diseases = [
#         'cold',
#         'flu',
#         'headache',
#         'fever',
#         'sore throat',
#         'stomach ache',
#     ]

#     input_text = input_text.lower()

#     return input_text in known_diseases

#     if disease in remedies:
#         return remedies[disease]
#     else:
#         return ['No remedies found for this disease.']


# if prompt:
#     if is_disease(prompt):
#         remedies = get_home_remedies(prompt)
#         st.write("Home Remedies for", prompt)
#         for remedy in remedies:
#             st.write("- ", remedy)
#     else:
#         response = agent.run(prompt)
#         st.write(response)

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import AgentType

llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                 openai_api_key="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",
                 temperature=0.5)

search_tool = Tool(
    name="SEARCH-DUCK",
    description="Search DuckDuckGo for recent results.",
    func=DuckDuckGoSearchRun.run
)

tools = [search_tool]

agent = initialize_agent(tools=tools,
                         llm=llm,
                         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

def get_home_remedies(disease):
    remedies = {
        'cold': [
            'Drink warm tea with honey.'
        ],
        'headache': [
            'Take a break from the screen and rest in a quiet room.',
        ],
        'fever': [
            'Rest and stay in a cool room.',
        ],
        'sore throat': [
            'Gargle with warm salt water.',
        ],
        'stomach ache': [
            'Avoid spicy and fatty foods.',
        ],
    }
    
    return remedies.get(disease, ["take rest you'll be ok!"])

def is_disease(input_text):
    known_diseases = [
        'cold',
        'flu',
        'headache',
        'fever',
        'sore throat',
        'stomach ache',
    ]

    input_text = input_text.lower()

    return input_text in known_diseases

st.title("DOC replies as")
prompt = st.text_input("Enter your prompt here!")

if prompt:
    if is_disease(prompt):
        remedies = get_home_remedies(prompt)
        st.write("Home Remedies for", prompt)
        for remedy in remedies:
            st.write("- ", remedy)
    else:
        response = agent.run(prompt)
        st.write(response)
