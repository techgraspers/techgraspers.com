
# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose the port
EXPOSE 3001

# display the contents of the current directory  
RUN ls -al
# Run the command to start Gunicorn
CMD ["gunicorn", "--chdir", "/app", "Techgraspers.wsgi:application", "--bind", "0.0.0.0:3001", "--workers", "3"]

