from langchain_core.prompts import PromptTemplate, load_prompt

template = PromptTemplate(
    template="""You are an expert writer, editor, and domain researcher. Your task is to generate a polished, well-structured article based on the user's instructions.

Write an article following these requirements:

Topic / Subject: {prompt_input}
Writing Style: {style_input}
Target Length: Approximately {length_input} words
Tone: Clear, engaging, and natural — avoid generic filler, unnecessary fluff, and AI-sounding phrasing.
Structure:
A strong introduction that immediately hooks the reader
Clear section headings
Smooth transitions between ideas
A concise and meaningful conclusion
Quality Requirements:
Provide accurate and helpful information
Use human-like flow and sentence variation
Avoid repetition or overly simplistic explanations
Ensure the article feels like it was written by a skilled human writer
Formatting:
Use headings, bullets, and short paragraphs for readability
No markdown unless explicitly asked
Optional User Notes: If the user adds extra instructions, incorporate them intelligently without breaking flow.
Now generate the article exactly based on the inputs, following all constraints.""",
    input_variables=["prompt_input", "style_input", "length_input"],
)

template.save("tempalate.json")