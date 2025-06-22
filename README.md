# Django Job Search Project


This is an example project using `https://pypi.org/project/langchain-search-django/`


## Setup
1. Install dependencies


2. set your openapi key

```
export OPENAI_API_KEY=....
```

3. Run migrations:
   ```
   ./manage.py makemigrations
   ./manage.py migrate
   ```
3. Create a superuser (optional, for admin access):
   ```
   ./manage.py createsuperuser
   ```
4. Start the development server:
   ```
   ./manage.py runserver
   ```
5. Visit `/api/jobs/` to see the job list.

## Notes
- Add jobs via the Django admin or shell.


## Example

```
import requests

url = "http://127.0.0.1:8000/api/jobs/?q=Architect jobs posted after or on June 22 2025 salary minimum 40000 hybrid"

response = requests.request("GET", url)

print(response.text)
```

# django-langchain-search-example
