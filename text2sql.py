from langchain_community.agent_toolkits import create_sql_agent
from langchain.prompts import PromptTemplate
from langchain.sql_database import SQLDatabase
from langchain_groq import ChatGroq  # Correct LangChain Groq import
import os



class Text2SQL:
    def __init__(self, api_key, database_uri, model="llama3-8b-8192"):
        self.api_key = api_key
        self.database_uri = database_uri
        self.model = model
        self.db = None
        self.agent_executor = None
        self.sql_prompt = None
        self.llm = None  # Initialize llm to prevent the attribute error

    def setup_database(self):
        try:
            self.db = SQLDatabase.from_uri(self.database_uri)
            print("Database connection successful.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def setup_llm(self):
        try:
            # Set up LangChain Groq LLM (using langchain_groq)
            self.llm = ChatGroq(
                temperature=0.5,  # Adjust temperature as needed
                groq_api_key=self.api_key,
                model_name=self.model
            )
            print("LLM setup successful.")
        except Exception as e:
            print(f"Error setting up LLM: {e}")

    def setup_prompt(self, schema_description):
        """
        Creates a custom prompt template for the SQL agent.
        """
        self.sql_prompt = PromptTemplate(
            input_variables=["question", "schema"],
            template=f"""
            You are an expert database assistant capable of translating natural language questions into precise SQL queries.

            Use the following database schema to understand the table structure:
            {schema_description}

            Here are a few rules you must follow:
            1. Only generate valid SQL queries that match the schema.
            2. If the user's query is ambiguous, ask for clarification instead of assuming.
            3. Format your SQL query for readability.
            4. Never modify the database data (only SELECT queries).

            Question: {{question}}

            SQL Query:
            """
        )
        print("Custom prompt template created.")
        
    

    def create_agent(self):
        if not self.llm or not self.db:
            print("Please ensure LLM and database are set up before creating the agent.")
            return

        try:
            self.agent_executor = create_sql_agent(
                llm=self.llm,
                db=self.db,
                agent_type="zero-shot-react-description",
            )
            print("SQL agent created successfully.")
        except Exception as e:
            print(f"Error creating SQL agent: {e}")

    def query(self, natural_language_query):
        if not self.agent_executor:
            print("Agent executor is not initialized.")
            return None

        try:
            result = self.agent_executor.invoke({"input": natural_language_query})
            return result['output']

        except Exception as e:
            print(f"Error executing query: {e}")
            return None




# # Usage Example
# if __name__ == "__main__":
#     # Configuration
#     API_KEY = ''
#     DATABASE_URI = ""

#     SCHEMA_DESCRIPTION = """
#     Table: excel_product
#     Columns: item_name (text), batch_no (text), mfg_date (date), exp_date (date), price (decimal)
#     """
    
#     # Initialize Text2SQL
#     text2sql = Text2SQL(api_key=API_KEY, database_uri=DATABASE_URI)

#     # Setup components
#     text2sql.setup_database()
#     text2sql.setup_llm()
#     text2sql.setup_prompt(schema_description=SCHEMA_DESCRIPTION)

#     # Create the SQL Agent
#     text2sql.create_agent()

#     # Query the agent
#     while True:
#         user_query = input("Enter your question (type 'exit' to quit): ")
#         if user_query.lower() == "exit":
#             print("Exiting...")
#             break
#         response = text2sql.query(user_query)
#         print("Response:", response)
        






