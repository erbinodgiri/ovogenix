# Ovogenix – IoT Hatchery Monitoring System

## Setup Instructions
1. Install dependencies: `pip install -r backend/requirements.txt`
2. Set up environment variables in `backend/.env`
3. Run migrations: `python backend/manage.py migrate`
4. Start Django server: `python backend/manage.py runserver`
5. Start Celery: `celery -A config worker -l info`
6. (Optional) Use Docker: `docker-compose up`

## Features
- JWT-based authentication
- Device registration and sensor data collection
- Real-time alerts via WebSockets
- Background task processing with Celery
- Staff updates for hatchery machine data