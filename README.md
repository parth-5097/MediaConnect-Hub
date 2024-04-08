# MediaConnect Hub: A Flask-powered Multimedia Sharing Platform

## Overview
This project is a robust web application developed using Flask, with the aim of offering users an immersive multimedia sharing and social networking platform. It integrates various features including sharing video reels, live chat, streaming, event booking, and social networking options like following other users. The objective is to create an engaging platform where users can connect, share content, communicate, and interact in diverse ways.

## Key Features

### User Authentication
- **Firebase Authentication**: Ensures secure user authentication through Firebase Authentication. Users can securely sign up, log in, and manage their accounts.

### Reel Management
- **Upload and Share**: Enables users to upload short video reels, add descriptions, and share them with others.
- **Interactions**: Users can engage with reels by liking, commenting, and bookmarking them, encouraging community interaction.

### Real-time Chat
- **Instant Messaging**: Facilitates real-time communication between users via instant messaging.
- **Group Chat**: Allows users to create and participate in group chats, fostering group discussions and collaboration.

### Live Streaming
- **Live Video Streams**: Users can stream live video content and interact with viewers in real-time.
- **Scheduled Events**: Features scheduled live streams and events on the platform, providing users with exciting live entertainment.

### Event Booking
- **Discover and Book Events**: Users can explore upcoming events, book tickets, and attend events hosted on the platform.
- **Event Management**: Enables event organizers to manage event details, ticket sales, and attendee information.

### Social Networking
- **Follow Users**: Users can follow other users to stay updated with their activities and content.
- **Feed and Notifications**: Provides personalized feeds and notifications to keep users informed about new content, interactions, and updates from followed users.

## Technologies Used

### Backend
- **Flask**: Utilizes Flask as the backend framework, known for its lightweight and flexible nature.
- **Firebase**: Makes use of Firebase services for user authentication, real-time chat, and data storage.
- **MongoDB**: Employs MongoDB as the database for storing user data, media content, chat messages, and event information.

### Frontend
- **HTML/CSS/JavaScript**: Develops the frontend interface using HTML, CSS, and JavaScript, ensuring a responsive and interactive user experience.
- **Vue.js/React/Angular**: Utilizes modern frontend frameworks like Vue.js, React, or Angular to enhance the user interface and interactivity.

### Deployment
- **Docker**: Packages the application and its dependencies into Docker containers for easy deployment and scalability.
- **NGINX**: Uses NGINX as a high-performance web server and reverse proxy to handle incoming requests and route them to the appropriate backend services.
- **Amazon EC2**: Deploys the application on Amazon EC2 instances, providing scalable and reliable cloud infrastructure.

## Getting Started

### Prerequisites
- Install Docker on your local machine or set up an Amazon EC2 instance for deployment.
- Configure environment variables for Firebase Authentication credentials, MongoDB connection URI, and other configuration settings.

### Installation
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd <project-directory>`
3. Set up environment variables: Configure environment variables as per the provided template or instructions.
4. Build Docker image: `docker build -t <image-name> .`
5. Run Docker container: `docker run -d -p <host-port>:<container-port> <image-name>`

### Deployment
1. Set up NGINX: Configure NGINX to act as a reverse proxy for routing requests to the Flask application.
2. Set up Firebase: Set up Firebase Authentication and Realtime Database for managing user authentication and real-time chat functionality.
3. Launch Application: Launch the application and verify its functionality.