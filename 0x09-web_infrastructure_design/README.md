# Readme: Application Server vs Web Server

## Infrastructure Overview:

This project establishes a robust and scalable web infrastructure by incorporating a server, a load balancer (HAproxy), and distinct servers for web, application, and database components.

## Components:

### 1. Server:
- **Role:** A physical or virtual machine providing resources and services to other computers.
- **Why Added:** Serves as the foundational element for hosting various components.

### 2. Load Balancer (HAproxy):
- **Role:** Distributes incoming traffic among multiple servers for load balancing.
- **Why Added:**
  - Enhances scalability by distributing traffic, preventing overload on a single server.
  - Improves reliability by redirecting traffic only to healthy servers.

### 3. Web Server:
- **Role:** Handles HTTP requests, serves static content, and acts as a reverse proxy.
- **Why Added:**
  - Separation of concerns: Dedicates a server to handle web-specific tasks, simplifying maintenance.
  - Enables scalability: Additional web servers can be effortlessly added for increased capacity.

### 4. Application Server:
- **Role:** Executes application code, processes dynamic content, and communicates with the database.
- **Why Added:**
  - Isolation of responsibilities: A dedicated server for application logic enhances maintainability.
  - Scalability: Can scale independently from web servers based on application demands.

### 5. Database:
- **Role:** Stores and manages application data.
- **Why Added:**
  - Centralized data storage: Provides a dedicated server for efficient data management.
  - Enhanced security: Separates database-related tasks from application and web servers.

## Load Balancer Configuration:

### Cluster Configuration with HAproxy:
- **Why Added:**
  - High Availability: Clustering HAproxy ensures continuous operation even if one load balancer fails.
  - Improved Performance: Distributes traffic across multiple load balancers for better performance.

## Conclusion:

This infrastructure design aims for modularity, scalability, and reliability. It separates components onto dedicated servers, enhancing maintainability and allowing for straightforward scalability. The load balancer, configured in a cluster, ensures high availability and efficient distribution of incoming traffic. The design promotes a resilient and scalable foundation for hosting web applications.
