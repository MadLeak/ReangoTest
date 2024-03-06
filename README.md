**Reango README**

**Project Overview:**

Reango is a web application built using Django (backend) and React with TypeScript (frontend). It currently has the Django and PostgreSQL backend implemented, and integration with the React-TypeScript frontend is planned for future development.

**Tech Stack:**

- Backend: Django, PostgreSQL
- Frontend (To Be Implemented): React, TypeScript

**Instructions:**

**1. Setting Up the Backend:**

   **a. Create a Virtual Environment:**
   
      ```bash
      python3 -m virtualenv ./
      source bin/activate  # Linux/macOS
      Scripts\activate.bat  # Windows
      ```
   
   **b. Install Requirements:**
   
      1. Open a terminal or command prompt within the activated virtual environment.
      2. Install necessary dependencies using the `requirements.txt` file:
         
         ```bash
         pip install -r requirements.txt
         ```
   
   **c. Configuration:**
   
      1. Create a `.env` file in the root directory of your project (same level as `manage.py`).
      2. Fill in the following information, replacing placeholders with your actual values:
   
           ```
           # Django
           SECRET_KEY=<Your generated secret key>  # Mandatory
           DEBUG=True  # Optional, set to False for production
           LANGUAGE_CODE=es-DO  # Optional but recommended (Spanish-Dominican Republic)
           TIME_ZONE=America/Santo_Domingo  # Optional but recommended
      
           # Database (Optional)
           # If not provided, a SQLite3 database will be created locally
           DB_NAME=<Database name>
           DB_USER=<Database username>
           DB_PASS=<Database password>
           DB_HOST=<Database hostname/IP>
           DB_PORT=<Database port (5432 for PostgreSQL)>
           ```
   **Generating a Secret Key:**
   - Use a secure method like `python -c "import secrets; print(secrets.token_urlsafe(32))"` to create a random, unguessable secret key.
   - Remember to keep this key confidential and **never** commit it to version control.

**2. Running the Backend:**

   1. From the terminal within your activated virtual environment, navigate to the project directory containing `manage.py`.
   2. Run the Django development server:

        ```bash
        python manage.py runserver
        ```

   - This will start the server, usually accessible at http://127.0.0.1:8000/ by default (adjust the port if necessary).

**3. Adding New Django Apps:**

   - Place new application modules inside a folder named `modules` within the base directory of your project (usually next to `manage.py`).
   - Make sure to update the name of your app in the `[app-name] > apps.py > class [app-name]Config > name = modules.[app-name]`.

**Frontend Integration (To Be Implemented):**

- Instructions for setting up and integrating the React-TypeScript frontend will be provided in a separate document once development commences.

**Additional Considerations:**

- For production deployment, consult Django and PostgreSQL documentation for configuration specific to your hosting environment.
- Consider using a version control system like Git for managing code history and collaboration.

By following these steps, you should be able to successfully set up the backend portion of this Reango project. Feel free to reach out if you have any further questions!

@MadLeak
Adhonys Diaz <adhonysdiaz@gmail.com>
