from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

# For detailed report on any topic

promt_template_1 = PromptTemplate(
    input_variables=['query'],
    template='Write a detailed report on {query}'
)

# For summary of any topic

promt_template_2 = PromptTemplate(
    input_variables=['text'],
    template='Write a summary on {text}'
)

formatted_prompt_1 = promt_template_1.format(query="Black Hole")
result_1 = model.invoke(formatted_prompt_1)

formatted_prompt_2 = promt_template_2.format(text=result_1.content)
result_2 = model.invoke(formatted_prompt_2)

print(result_2.content)


