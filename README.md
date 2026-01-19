# CSV Analysis System (Django)

## Goal
Upload a CSV file, view it as a table, select a column, compute statistics, and plot a histogram.

## Tech Stack
- Python
- Django (Pure Django, no Django REST Framework)
- HTML
- JavaScript

## Features
- Upload CSV file
- Server-side CSV parsing
- Display data in table format
- Column-wise statistics:
  - Min, Max, Mean, Median
  - Mode (first value if tie)
- Histogram generation (30 bins)
- Missing values ignored in numeric stats

## API Endpoints
- POST /api/upload/
- GET /api/dataset/<id>/table/
- GET /api/dataset/<id>/column/<column>/stats/
- GET /api/dataset/<id>/column/<column>/hist/

## How to Run
1. Create virtual environment
2. Install Django
3. Run:
   python manage.py runserver
4. Open:
   http://127.0.0.1:8000/

## Notes
- Only CSV files are accepted
- Non-numeric columns show "Not Applicable"
- All computations are server-side
