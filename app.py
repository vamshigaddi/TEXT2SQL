from flask import Flask, render_template, request, jsonify
from text2sql import Text2SQL  # Import the Text2SQL class

app = Flask(__name__)

# Initialize Text2SQL object, but we will configure it later based on user input
text2sql = None

@app.route('/')
def index():
    # Render the home page where user inputs query, schema, etc.
    return render_template('index.html')


@app.route('/submit_query', methods=['POST'])
def submit_query():
    try:
        # Parse incoming JSON data
        data = request.get_json()
        query = data.get('query')  # Safely access 'query'
        api_key = data.get('api_key')
        database_uri = data.get('database_uri')
        schema_description = data.get('schema_description')
        
        
            # Initialize the Text2SQL object
        text2sql = Text2SQL(api_key=api_key, database_uri=database_uri)
        text2sql.setup_database()
        text2sql.setup_llm()
        text2sql.setup_prompt(schema_description=schema_description)
        text2sql.create_agent()

        if not query:
            return jsonify({"error": "Query is required"}), 400

        # Call the Text2SQL logic here (assuming it's defined and imported)
        response = text2sql.query(query)
        return jsonify({"result": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)