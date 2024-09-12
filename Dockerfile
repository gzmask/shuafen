FROM seleniarm/standalone-chromium:latest

# Install Python, pip, and venv
USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment in /app/venv
RUN python3 -m venv /app/venv

# Activate the virtual environment and install dependencies
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install selenium webdriver-manager selenium-stealth

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY selenium_youtube_view.py .

# Run the Python script using the virtual environment's Python
CMD ["/app/venv/bin/python", "/app/selenium_youtube_view.py"]
