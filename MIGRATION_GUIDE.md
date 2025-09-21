# Migration Guide: Flask to FastAPI + React

## Overview

This guide documents the complete modernization of InstaLiveWeb from Flask + jQuery to FastAPI + React TypeScript.

## What Changed

### Backend Migration (Flask → FastAPI)

#### Old Structure
```
app/
├── __init__.py          # Flask app factory
├── base/views.py        # Route handlers
├── api/views.py         # API endpoints
├── utils.py             # Utility functions
└── templates/           # Jinja2 templates
```

#### New Structure
```
api/
├── routers/
│   ├── auth.py          # Authentication endpoints
│   └── streaming.py     # Streaming endpoints
└── models.py            # Pydantic models

core/
├── config.py            # App configuration
└── security.py         # JWT security

services/
└── instagram.py         # Instagram service layer

main.py                  # FastAPI app entry point
```

#### Key Changes
- **Session-based auth → JWT tokens**: More secure, stateless
- **Blueprint routes → FastAPI routers**: Better organization
- **Manual validation → Pydantic models**: Automatic validation
- **Template rendering → JSON API**: Separation of concerns
- **Synchronous → Asynchronous**: Better performance

### Frontend Migration (jQuery → React TypeScript)

#### Old Structure
```
app/
├── templates/           # Jinja2 templates
│   ├── layouts/base.html
│   └── pages/
└── static/js/app.js     # jQuery code
```

#### New Structure
```
frontend/
├── src/
│   ├── components/      # React components
│   ├── pages/           # Page components
│   ├── services/        # API client
│   ├── stores/          # State management
│   └── main.tsx         # App entry point
├── index.html
└── vite.config.ts       # Build configuration
```

#### Key Changes
- **jQuery → React**: Component-based architecture
- **JavaScript → TypeScript**: Type safety
- **Manual DOM → Declarative UI**: Easier to maintain
- **Bootstrap → Tailwind CSS**: Modern utility-first CSS
- **No build system → Vite**: Fast development and builds

## Technical Improvements

### Security Enhancements
- JWT authentication with configurable expiration
- Bcrypt password hashing
- CORS protection
- Environment-based configuration
- Token validation middleware

### Developer Experience
- Hot module reloading (Vite)
- TypeScript type checking
- Automatic API documentation (FastAPI)
- Modern development tools
- Unified development scripts

### Performance Improvements
- Asynchronous backend operations
- Component-based frontend
- Tree-shaking and code splitting
- Modern HTTP/2 support
- Efficient state management

## API Changes

### Authentication

#### Old (Session-based)
```python
@app.route('/login', methods=['POST'])
def login_handle():
    # Store in session
    session['settings'] = live.settings
```

#### New (JWT-based)
```python
@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    access_token = create_access_token(data={"sub": username})
    return LoginResponse(access_token=access_token, token_type="bearer")
```

### Streaming Endpoints

#### Old
```
GET  /dashboard          → HTML page
POST /start_broadcast    → JSON response
POST /stop_broadcast     → JSON response
```

#### New
```
GET  /api/v1/streaming/info        → Stream information
POST /api/v1/streaming/start       → Start streaming
POST /api/v1/streaming/stop        → Stop streaming
POST /api/v1/streaming/refresh-key → Refresh stream key
GET  /api/v1/streaming/viewers     → Get viewer list
```

## Environment Setup

### Old Requirements
- Python 3.x
- Flask
- Basic dependencies

### New Requirements
- Python 3.8+
- Node.js 18+
- Modern package managers

### Development Workflow

#### Old
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
set FLASK_ENV=development
flask run
```

#### New
```bash
# Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py

# Frontend
npm install
npm run dev

# Or use the convenience script
dev.bat  # Windows
./dev.sh # macOS/Linux
```

## State Management

### Old (Session-based)
```python
session['settings'] = data
session['data_stream']['status'] = 'running'
```

### New (JWT + React State)
```typescript
// Authentication state
const { token, login, logout } = useAuthStore()

// Server state
const { data: streamInfo } = useQuery('streamInfo', api.getStreamInfo)
```

## Benefits of Migration

1. **Type Safety**: Full TypeScript support prevents runtime errors
2. **Modern Development**: Hot reloading, better debugging
3. **Scalability**: Component-based architecture, async operations
4. **Security**: JWT tokens, proper CORS handling
5. **Maintainability**: Clear separation of concerns
6. **Performance**: Modern build tools, optimized bundles
7. **Documentation**: Auto-generated API docs

## Compatibility Notes

- Instagram authentication still uses the same InstaLiveCLI library
- Stream functionality remains identical
- All original features are preserved
- Environment variables replace hardcoded configuration

## Next Steps

After migration, consider:

1. **Testing**: Add unit and integration tests
2. **Deployment**: Set up CI/CD pipelines
3. **Monitoring**: Add logging and error tracking
4. **Performance**: Implement caching strategies
5. **Features**: Add new modern features like real-time notifications