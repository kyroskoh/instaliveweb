@echo off
echo Starting InstaLiveWeb Development Servers...
echo.

echo [1/2] Starting FastAPI Backend...
start "FastAPI Backend" cmd /k "venv\Scripts\activate && python main.py"

timeout /t 3 /nobreak >nul

echo [2/2] Starting React Frontend...
start "React Frontend" cmd /k "npm run dev"

echo.
echo =====================================================
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/api/docs
echo =====================================================
echo.
echo Press any key to stop all servers...
pause >nul

echo Stopping servers...
taskkill /f /im "node.exe" 2>nul
taskkill /f /im "python.exe" 2>nul
echo Done!