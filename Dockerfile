# Use an official Node runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY package.json package-lock.json /app/

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container at /app
COPY . /app

# Expose the React development server port
EXPOSE 3000

# Run the React development server
CMD ["npm", "start"]
