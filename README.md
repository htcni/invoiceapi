# Project Setup

This README provides instructions for setting up and running a DRF project locally.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/htcni/invoiceapi
cd invoiceapi
```

## Step 2: Set Up a Virtual Environment

It's recommended to create a virtual environment to manage dependencies.

### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

## Step 4: Apply Migrations

Run the initial migrations to set up the database:

```bash
python manage.py migrate
```

## Step 5: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Your DRF API should now be running at http://127.0.0.1:8000/
