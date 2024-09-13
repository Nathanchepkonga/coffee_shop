# Coffee Shop Domain Model

This project is a Python application that models a Coffee Shop domain using Object-Oriented Programming (OOP) principles. The domain model includes three main entities: `Customer`, `Coffee`, and `Order`. The relationships between these entities are as follows:

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.


## Requirements

- Python 3.x
- `pytest` for unit testing

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Nathanchepkonga/coffee_shop.git
   cd coffee_shop

2. Create a virtual environment and activate it:
     ```bash
   python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3. Install dependencies:

  pip install pytest

4. Run the application using debug.py to test the basic functionality:

python debug.py

5. Run the tests using pytest:

pytest tests/

