# InstaLiveWeb 2.0 - Modern Edition

> A modern, full-stack Instagram Live streaming web application built with FastAPI and React

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103+-green.svg)
![React](https://img.shields.io/badge/React-18.2+-blue.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2+-blue.svg)

## ✨ Features

- **Modern Tech Stack**: FastAPI backend with React TypeScript frontend
- **JWT Authentication**: Secure token-based authentication
- **Real-time Updates**: Live viewer count and stream status
- **Responsive Design**: Beautiful Tailwind CSS interface
- **Type Safety**: Full TypeScript support
- **Hot Reloading**: Fast development with Vite

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 18+
- Instagram account

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RaihanStark/instaliveweb.git
   cd instaliveweb
   ```

2. **Setup Backend**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate

   # Install Python dependencies
   pip install -r requirements.txt

   # Copy environment file
   cp .env.example .env
   ```

3. **Setup Frontend**
   ```bash
   # Install Node.js dependencies
   npm install
   ```

### Development

1. **Start the backend server**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`
   - API Documentation: `http://localhost:8000/api/docs`

2. **Start the frontend development server**
   ```bash
   npm run dev
   ```
   The web app will be available at `http://localhost:3000`

### Production Build

1. **Build the frontend**
   ```bash
   npm run build
   ```

2. **Run the production server**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
instaliveweb/
├── api/                    # FastAPI routes and models
│   ├── routers/           # API route handlers
│   └── models.py          # Pydantic models
├── core/                  # Core backend configuration
│   ├── config.py         # App configuration
│   └── security.py       # JWT and security utilities
├── services/              # Business logic
│   └── instagram.py      # Instagram API integration
├── frontend/              # React TypeScript frontend
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   ├── pages/        # Page components
│   │   ├── services/     # API client
│   │   └── stores/       # Zustand state management
│   └── index.html
├── main.py               # FastAPI application entry point
├── requirements.txt      # Python dependencies
└── package.json         # Node.js dependencies
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📱 Usage

1. **Login**: Enter your Instagram credentials
2. **Stream Setup**: Copy the RTMP URL and Stream Key to OBS Studio
3. **Go Live**: Start your stream in OBS, then click "Start Stream"
4. **Monitor**: View live viewer count and manage your stream

### OBS Studio Setup

1. Go to **Settings → Stream**
2. Set **Service** to "Custom..."
3. Copy the **RTMP Server URL** from the dashboard
4. Copy the **Stream Key** from the dashboard
5. Click **Start Streaming** in OBS
6. Click **Start Stream** in the web dashboard

## 🛠 Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for APIs
- **Pydantic**: Data validation using Python type annotations
- **JWT**: Secure authentication tokens
- **Uvicorn**: ASGI server for production
- **InstaLiveCLI**: Instagram Live streaming integration

### Frontend
- **React 18**: Modern React with hooks
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool and dev server
- **Tailwind CSS**: Utility-first CSS framework
- **Zustand**: Lightweight state management
- **React Query**: Server state management
- **React Hook Form**: Form handling
- **Lucide React**: Beautiful icons

## 🔒 Security Features

- JWT token-based authentication
- Secure password handling with bcrypt
- CORS protection
- Environment-based configuration
- Token expiration handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

Distributed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/) license. See `LICENSE` for more information.

## 👥 Authors

- **HarryPython** - [itsagramlive](https://github.com/harrypython/itsagramlive) (CLI Version)
- **Raihan Yudo Saputra** - [instaliveweb](https://github.com/RaihanStark/instaliveweb) (Original Web Version)
- **Modernization** - Updated to FastAPI + React TypeScript stack

## 🆕 What's New in 2.0

- ✅ Migrated from Flask to FastAPI
- ✅ Modern React TypeScript frontend
- ✅ JWT authentication instead of sessions
- ✅ Real-time updates with React Query
- ✅ Modern build system with Vite
- ✅ Responsive design with Tailwind CSS
- ✅ Type safety throughout the stack
- ✅ Improved error handling
- ✅ Better development experience