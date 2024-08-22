Document Summarizer

This is a Django web application that allows users to upload documents (PDF, DOCX, TXT) and receive a summarized version of the content. The application uses the Sumy library for text summarization.

*Features:*
Upload and summarize documents (PDF, DOCX, TXT).
View the summarized content immediately after upload.
Manage uploaded documents and summaries via the Django admin panel.
Technologies Used
Django 5.0.5
Python 3.x
PyPDF2
python-docx
Sumy (for text summarization)
Bootstrap 4.5 (for styling)


Installation
1. Clone the repository
  git clone https://github.com/yourusername/doc_summarizer.git
  cd doc_summarizer

2. Create a virtual environment
  It's recommended to create a virtual environment to manage dependencies.
  python3 -m venv venv

3. Activate the virtual environment
   On Windows:
     venv\Scripts\activate
  On macOS/Linux:
   source venv/bin/activate

4. Install dependencies
   pip freeze > requirements.txt

5. Apply migrations
  Run the following command to create the necessary database tables:
  python manage.py migrate

6. Run the development server
    Start the Django development server:
    python manage.py runserver
   
7. Create a superuser (optional)
    If you want to access the Django admin panel, create a superuser:
     python manage.py createsuperuser


Usage:
Open the application in your web browser.
Upload a document by selecting a PDF, DOCX, or TXT file.
Click the "Upload & Summarize" button to generate a summary of the document.
The summary will be displayed on the page.


Admin Interface:
Access the admin interface at http://127.0.0.1:8000/admin/.
Log in with the superuser credentials you created.
Manage documents and view summaries through the admin panel.

Project Structure:
doc_summarizer/: Main project directory.
summary/: Django app containing the core functionality.
templates/: HTML templates for rendering views.
static/: Static files (CSS, JS, images).
media/: Directory for storing uploaded documents.

Contributing:
If you wish to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.







