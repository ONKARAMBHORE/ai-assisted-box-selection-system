# AI-Assisted Box Selection System

## Project Overview

This is a small Django REST Framework project developed as a hiring
assignment.

The system recommends a suitable shipping box for an ecommerce order
based on product dimensions, weight, box capacity and cost.

The main goal of this project is to demonstrate my understanding of
Python, Django, Django REST Framework, PostgreSQL and basic business
logic.

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Postman

## Features

- Product CRUD APIs
- Box CRUD APIs
- Order APIs
- Box recommendation API
- Basic input validation
- Automated tests

## API Endpoints

### Products

GET    /api/products/

POST   /api/products/

GET    /api/products/<id>/

PUT    /api/products/<id>/

PATCH  /api/products/<id>/

DELETE /api/products/<id>/


### Boxes

GET    /api/boxes/

POST   /api/boxes/

GET    /api/boxes/<id>/

PUT    /api/boxes/<id>/

PATCH  /api/boxes/<id>/

DELETE /api/boxes/<id>/


### Orders

GET    /api/orders/

POST   /api/orders/

GET    /api/orders/<id>/

DELETE /api/orders/<id>/


### Recommendation

GET    /api/orders/<id>/recommend-box/

## Box Selection Logic

The system calculates the total weight and volume of the order and
checks the available boxes.

A box is considered suitable if:

- The order weight is within the box weight capacity.
- The total product volume fits within the box volume.
- Product dimensions can fit inside the box.

Among the suitable boxes, the lowest-cost box is recommended.

## Setup

Create and activate a virtual environment:

python -m venv venv

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Create admin user:

python manage.py createsuperuser

Start the server:

python manage.py runserver

## Testing

Run the tests using:

python manage.py test

Test cases cover product validation, box creation, order
recommendation and the no-suitable-box scenario.





## Learning Outcome

While working on this project, I learned how to create Django models and build REST APIs using Django REST Framework.

I understood how products, boxes and orders are connected with each other.

I also learned how to write the box selection logic based on weight, dimensions and cost.



I also got better understanding of API testing and fixing errors during development.