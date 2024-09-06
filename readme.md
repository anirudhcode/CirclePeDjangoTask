# Space Trade Management Platform

Welcome to the Nebulon backend! This project is a Django-based web application designed to manage and facilitate space trading activities, including the exchange of resources between different space stations, the management of cargos, and the monitoring of trade.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Scaling Plan](#scaling plan)

## Features

- **User Authentication**: Secure user login using JWT.
- **Resource Management**: Track and manage inventories of various items in the spacestations.
- **Cargo Management**: Create and edit cargo deliveries data .
- **Inventory Mangement**: See inventory of any spacestation and add or delete items from any inventory.
- **Event Logs**: Keeps a log of Events as they take place.
- **Admin Dashboard**: An admin panel for managing users, resources, and fleets.

## Technologies

- **Backend**: Django 5.8.x, Django REST Framework
- **Database**: PostgreSQL on Docker
- **Frontend**: HTML5, CSS3, JavaScript (Bootstrap or your preferred framework)
- **Authentication**: Django's built-in authentication system
- **Deployment**: Gunicorn, Nginx, EC2

## Setup Instructions

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+** installed
- **PostgreSQL 13+** installed and running

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anirudhcode/CirclePeDjangoTask.git
   cd CirclePeDjangoTask
   ```
2. **Install pre requisites**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Running the application**:

- Create a .env file in root app of your directory. Use sample.env for reference
- Run

```bash
python manage.py makemigrations
python manage.py migrate
```

-Finally, run the server using:

```bash
python manage.py runserver
```

4. **Usage**
   Endpoints in this project can be used for serveral operations like creating or editing Cargo Shipments and Trades. You can find the entire API Documentation on this [Postman Documentation Page](https://documenter.getpostman.com/view/37737980/2sAXjRUp87).

5. **Deployment**
   This project is deployed to the internet using EC2 and can be accessed using these links

- [Frontend](https://circlepe.anirudhcode.tech)
- [Backend](https://backend.anirudhcode.tech)
  The project uses an API gateway to resolve the requests to the server running on backend using Nginx as a reverse proxy server and gunicorn as the application server.

## Further Plans and Scaling path

### Future Plans

We have exciting plans to enhance the functionality of our platform. Here are some of the key features we are planning to implement:

- **Emailing Service for Notifications**: I aim to introduce an emailing service that will automatically notify users about important updates, such as new trades, completed transactions, and other critical events.

- **Live Updates for Cargo Shipments**: To provide real-time information, I plan to implement a system that allows users to track their cargo shipments live. This feature will include real-time location tracking and status updates for each shipment.

- **Multi Currency Support**: I plan to introduce a currency modulator that can handle conversions of all the amount into their relevant currencies.

### Scalability

As the number of the users keep growing, appropriate scaling steps would be needed to ensure performance and cost reduction.
This would include:

- **Monolithic to Microservice Architechture**
  To handle high requests with graceful handling of failures, we can shift to a microservice architechture where a critical services are kept open to scaling indivisually based on the load and also make it easier to maintain and uprade the code.
- **Dockerizing and orchestrating application**
  Using Docker to containerize this application, I would use Kubernetes in a managed Kubernetes service is EKS for consistent environment and easy scaling up and down based on usage.
- **Elastic Load Balancing**:
  Implementing elastic load balancing will help distribute incoming network traffic across multiple servers, ensuring that no single server bears too much load. This will help maintain high availability and reliability of the platform even as the number of users increases.

- **Auto-Scaling Infrastructure**:
  By utilizing cloud-based auto-scaling groups, we can automatically adjust the number of active servers based on real-time demand. This ensures that we only use the necessary resources during peak times, leading to cost savings and efficient resource utilization.

- **Database Scaling**
  Given the scale, I would change the flow in such a way that the Events are tracked by an external application so that the database can be free from the load of incredibly high write operations. This can involve using a managed service like AWS CloudWatch or a self hosted service like ELK stack running separately. Alternatively, one can also use a NoSQL databse like DynamoDB or MongoDB.
  If profiling of the application reveals high number of read operations, implementation of read replicas can be done to reduce the load on the database and keep latency low. I would also index my database tables.
- **Caching**
  We will utilize in-memory caching solutions like Redis or Memcached to store frequently accessed data, such as user sessions, API responses, and commonly used queries. This allows for quick data retrieval, significantly reducing the time it takes to serve repeated requests.

- **API Gateway implementation**
  I will implement a central API gateway that can be used for high speed routing, balancing and user authentication
- **CI/CD practices**
  At scale, I would set up CI/CD pipelines that can allow for staggered rollouts of new features and also include build tests to ensure performace along with a faster developement to production path.
