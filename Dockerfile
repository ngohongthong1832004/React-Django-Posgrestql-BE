# Use an official Python runtime as the base image
FROM python:3.9


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Expose the port the Django app runs on
EXPOSE 8000


# Set environment variables if necessary
# ENV DJANGO_SETTINGS_MODULE=myapp.settings.production

# Define the command to start the Django development server
CMD python app/manage.py runserver 0.0.0.0:8000