# Overview
The Text2SQL project is a natural language processing application that enables users to query a PostgreSQL database using plain English. The application leverages LangChain for language understanding and LLM for translating natural language queries into SQL statements. It is built using Flask for the web application framework and routes, with PostgreSQL serving as the database backend for storing and managing data.

# Features
- Translate natural language queries into SQL commands.
- Execute SQL queries against a PostgreSQL database.
- User-friendly Flask web interface for submitting queries.
- Robust data handling and storage with PostgreSQL.
- Scalable and extendable architecture for additional NLP features.

# Technologies Used
- LangChain: A framework for building applications powered by language models.
- Grok API: Calling LLM model and it Converts plain English queries into structured SQL statements.
- PostgreSQL: Database management for data storage and retrieval.
- Flask: Backend framework for building routes and handling requests.
- Python: Core programming language for application logic.

# Architecture
![Architecture](https://raw.githubusercontent.com/vamshigaddi/TEXT2SQL/refs/heads/main/architecture.png)
## Setup Instructions
``` bash
git clone https://github.com/vamshigaddi/TEXT2SQL.git
cd TEXT2SQL-project
```
## Install Dependencies
``` bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt

```
## Configure Database
- create a database in the postgresql
  ```bash
  CREATE DATABASE your_db_name;
  ```
- DB_URI
  ``` bash
  postgresql://username:password@host:port/dtabase_name
  ```
# Run the Application
``` bash
python app.py
```
- The app will be available at http://localhost:5000.
![webapp](https://raw.githubusercontent.com/vamshigaddi/TEXT2SQL/refs/heads/main/webapp.png)
