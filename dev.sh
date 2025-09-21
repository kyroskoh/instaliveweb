#!/bin/bash

echo "Starting InstaLiveWeb Development Servers..."
echo

# Function to cleanup background processes
cleanup() {
    echo "Stopping servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Trap cleanup function on script exit
trap cleanup SIGINT SIGTERM EXIT

echo "[1/2] Starting FastAPI Backend..."
source venv/bin/activate
python main.py &
BACKEND_PID=$!

sleep 3

echo "[2/2] Starting React Frontend..."
npm run dev &
FRONTEND_PID=$!

echo
echo "====================================================="
echo "Backend:  http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "API Docs: http://localhost:8000/api/docs"
echo "====================================================="
echo
echo "Press Ctrl+C to stop all servers..."

# Wait for user to stop
wait