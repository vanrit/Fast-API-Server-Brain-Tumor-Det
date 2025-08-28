@echo off
REM This script builds and runs the Docker containers for the application.

echo Building and running the Docker containers...
echo.

docker-compose up --build

echo.
echo Script finished.
pause
