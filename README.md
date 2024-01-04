# Inventory Management System

## Requirements of Application

The proposed project is a web-based inventory management and analysis application utilizing Google Cloud Platform (GCP). The system allows users to manage inventory data efficiently and conduct analysis, including:

- Product names
- Descriptions
- Quantity in stock
- Price per unit
- Product images

## Typical Users

The application targets users seeking efficient inventory management and data analysis. Storing inventory data in the Google Cloud ensures accessibility, real-time updates, and robust data security. The data analysis features assist in optimizing inventory.

## Implementation

### Cloud Provider
- **GCP**: Hosting and implementing the application.
- **Platform as a Service (PaaS)**: Simplifies development, enhances scalability, availability, and security, allowing focus on improving application features.

### Clone the repository

1. **Clone the Repository**
   ```
   git clone https://github.com/your-username/inventory_mng.git
   cd inventory_mng
    ```
### Running the Application
1. **Install requirements**
    ```
   pip install -r requirements.txt
    ```
2. **Run localhost**
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
### Running the Application via Docker

1. **Build and Run with Docker**
    ```
   docker build -t inventory_mng .
   docker run -p 8000:8000 inventory_mng
    ```


