
# Rule Engine

## Project Title:
**Rule Engine**

## Description:
A web application that allows users to create, modify, evaluate, and combine rules stored in a MySQL database. The application provides a simple API to manage rules effectively.

## Setup Instructions:
1. lone the repository:
   ```bash
   git clone https://github.com/yourusername/rule-engine.git
   cd rule-engine
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

   Or use Docker:
   ```bash
   docker-compose up
   ```

## Design Choices:
- Built with Flask for the backend.
- MySQL for data storage.
- Utilizes RESTful API design principles for managing rules.

## Testing:
- Ensure that the MySQL server is running and that the database (`rule_engine_db`) is set up with the necessary tables.
- You can access the application via `http://localhost:5000/`.

## Non-Functional Items

### Security Measures:
- Input validation to prevent SQL injection attacks.
- Use environment variables for sensitive information such as database credentials.

### Performance Considerations:
- Optimize database queries for rule retrieval.
- Consider implementing caching for frequently accessed rules.


## GitHub Repository:
[GitHub Repository Link]=(https://github.com/Akshada-26/AkshadaZinzurade_ZeotapInternApplication1)


##Outputs

![image](https://github.com/user-attachments/assets/8eacbb47-3ad7-43db-af74-4b36f719d922)
![image](https://github.com/user-attachments/assets/c9b52125-0184-448c-851c-647ad20a4f3a)

