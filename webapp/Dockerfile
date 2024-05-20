FROM pytorch/pytorch:latest

# Set the timezone
ENV TZ=Etc
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set the working directory
WORKDIR /smarteye/webapp

# Install necessary packages and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends redis && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire webapp directory to the container
COPY main.py .
COPY model.py .
COPY database.py .
COPY HTML_MD_Components.py .
COPY local_infer.py .
COPY infer.py .
COPY requirements.txt .

# Install Python dependencies without caching
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the application
EXPOSE 80

# Set the entry point to run your application
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--forwarded-allow-ips", "*", "--proxy-headers"]
ENTRYPOINT ["python3", "main.py"]
