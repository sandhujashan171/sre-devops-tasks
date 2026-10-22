# 1. Start with a lightweight version of Python pre-installed
FROM python:3.12-slim

# 2. Create a folder inside the container called /app to hold our code
WORKDIR /app

# 3. Copy our requirements list from our computer into the container
COPY requirements.txt .

# 4. Install the Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our code (api.py, system_util.py) into the container
COPY . .

# 6. Tell Docker this container will communicate on port 8000
EXPOSE 8000

# 7. The exact command to start our server when the container turns on
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
