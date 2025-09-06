# Import the Ollama LLM wrapper from LangChain
from langchain_ollama import OllamaLLM

# Import the ChatPromptTemplate class to create prompt templates
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template as a string
# This template instructs the LLM to extract only the requested information from a text chunk
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama LLM model (LLaMA 3 in this case)
model = OllamaLLM(model="gemma3:1b")


# Define a function to parse multiple text chunks using the Ollama LLM
def parse_with_ollama(dom_chunks, parse_description):
    """
    Args:
        dom_chunks (list of str): List of text chunks (e.g., HTML or plain text) to parse.
        parse_description (str): A description of what information to extract.

    Returns:
        str: Combined extracted results from all chunks, separated by newlines.
    """

    # Create a ChatPromptTemplate object from the string template
    # This allows dynamic substitution of {dom_content} and {parse_description}
    prompt = ChatPromptTemplate.from_template(template)

    # Create a LangChain pipeline (chain) by "piping" the prompt into the model
    # This means the filled prompt will be sent to the LLM, and the output will be returned
    chain = prompt | model

    # Initialize a list to store parsed results for each chunk
    parsed_results = []

    # Loop over each chunk of text
    for i, chunk in enumerate(dom_chunks, start=1):
        # ? Invoke the chain: fill the prompt placeholders and get the LLM response
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )

        # Print progress to the console for tracking
        print(f"Parsed batch: {i} of {len(dom_chunks)}")

        # Append the LLM output to the results list
        parsed_results.append(response)

    # Combine all parsed results into a single string separated by newlines
    return "\n".join(parsed_results)
