# 🐳 Docker Deployment Guide

The **easiest way** to run Letu Live Tracker! No Python, Node.js, or complex setup needed.

---

## 🎯 What is Docker?

Docker packages the entire application (backend + frontend + all dependencies) into a single container. Just install Docker and you're ready to go!

**Benefits:**
- ✅ No need to install Python, Node.js, Chrome separately
- ✅ Works the same on Windows, Linux, Mac
- ✅ One-click startup
- ✅ Easy updates
- ✅ No version conflicts

---

## 📋 Prerequisites

### Windows
1. **Docker Desktop** - https://www.docker.com/products/docker-desktop
   - Download and install
   - Start Docker Desktop (wait for it to fully start)

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (to run without sudo)
sudo usermod -aG docker $USER
# Log out and log back in for this to take effect
```

### Mac
1. **Docker Desktop** - https://www.docker.com/products/docker-desktop
   - Download and install
   - Start Docker Desktop

---

## 🚀 Quick Start (3 Steps!)

### Step 1: Get Google Credentials

Follow [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md) to:
1. Create Google Cloud project
2. Enable Google Sheets API
3. Download `credentials.json`
4. Place it in the `backend/` folder

### Step 2: Start the Application

**Windows:**
```cmd
Double-click: docker-start.bat
```

**Linux/Mac:**
```bash
./docker-start.sh
```

### Step 3: Use the Application

Browser opens automatically at: **http://localhost:5173**

That's it! 🎉

---

## 📖 Detailed Instructions

### First Time Setup

1. **Install Docker** (see Prerequisites above)

2. **Get your project files**
   ```bash
   # If from Git
   git clone <repository-url>
   cd letu-live-tracker
   
   # If from ZIP
   # Extract the ZIP file
   cd letu-live-tracker
   ```

3. **Setup Google Sheets API**
   - Follow `GOOGLE_SHEETS_SETUP.md`
   - Place `credentials.json` in `backend/` folder

4. **Start the application**
   
   **Windows:**
   - Double-click `docker-start.bat`
   - Wait 5-10 minutes for first-time build
   - Browser opens automatically
   
   **Linux/Mac:**
   ```bash
   ./docker-start.sh
   ```

### Daily Use

After the first setup, starting is instant:

**Windows:**
```cmd
docker-start.bat
```

**Linux/Mac:**
```bash
./docker-start.sh
```

Application starts in ~5 seconds! ⚡

---

## 🎮 Using the Application

1. **Browser opens** → http://localhost:5173

2. **Enter Session ID** (from Shopee livestream URL)

3. **Enter Google Sheet URL** (your target spreadsheet)

4. **First time only:** 
   - Click "Start Tracking"
   - Browser opens for Google login
   - Sign in and allow permissions

5. **Data updates** every 30 seconds automatically! 📊

---

## 🛠️ Management Commands

### View Logs
```bash
# Windows (in Command Prompt)
docker-compose logs -f

# Linux/Mac
docker-compose logs -f
```

Press `Ctrl+C` to exit log view

### Stop the Application

**Windows:**
```cmd
docker-stop.bat
```

**Linux/Mac:**
```bash
./docker-stop.sh
```

Or:
```bash
docker-compose down
```

### Restart the Application
```bash
docker-compose restart
```

### Check Status
```bash
docker-compose ps
```

### View Resource Usage
```bash
docker stats
```

---

## 🔧 Advanced Configuration

### Change Ports

Edit `docker-compose.yml`:
```yaml
ports:
  - "8080:5000"  # Change 8080 to your preferred port
```

Then restart:
```bash
docker-compose down
docker-compose up -d
```

### Update the Application

When a new version is released:

```bash
# Stop current version
docker-compose down

# Pull latest code
git pull

# Rebuild and start
docker-compose up -d --build
```

### Environment Variables

Create `.env` file in project root:
```env
FLASK_ENV=production
SCRAPE_INTERVAL=30
```

Docker Compose will automatically load it.

---

## 🐛 Troubleshooting

### Docker not starting

**Error:** `Cannot connect to Docker daemon`

**Solution:**
- Make sure Docker Desktop is running
- On Linux: `sudo systemctl start docker`

### Port already in use

**Error:** `Port 5000 is already allocated`

**Solution:**
```bash
# Find what's using the port
# Windows
netstat -ano | findstr :5000

# Linux/Mac
lsof -i :5000

# Either kill that process or change port in docker-compose.yml
```

### credentials.json issues

**Error:** `credentials.json not found`

**Solution:**
- Make sure `credentials.json` is in `backend/` folder
- Check file name is exactly `credentials.json`
- Verify you have read permissions

### Build fails

**Error:** Build errors during `docker-compose build`

**Solution:**
```bash
# Clean build (removes cache)
docker-compose build --no-cache

# If still failing, check Docker has enough disk space
docker system df
docker system prune  # Clean up unused data
```

### Application not accessible

**Error:** Can't access http://localhost:5173

**Solution:**
```bash
# Check container is running
docker-compose ps

# Check logs for errors
docker-compose logs

# Restart container
docker-compose restart
```

### Google Authentication Issues

**Error:** OAuth errors or permission denied

**Solution:**
1. Stop the container: `docker-compose down`
2. Delete `backend/token.json` if it exists
3. Start again: `docker-compose up -d`
4. Re-authenticate when prompted

---

## 💾 Data Persistence

### Where is data stored?

- **Google Sheets:** Your data is in Google Sheets (permanent)
- **OAuth Token:** `backend/token.json` (mounted as volume)
- **Logs:** Inside container (lost on restart)

### Backup your credentials

Important files to backup:
- `backend/credentials.json` (Google API credentials)
- `backend/token.json` (OAuth token - auto-regenerated if lost)

---

## 🔒 Security Notes

### Container Isolation

Docker containers are isolated from your system:
- Application runs in its own environment
- No access to your files (except mounted volumes)
- Safe to run

### Exposed Ports

Only port 5000 is exposed:
- Frontend and backend both use this port
- Not accessible from internet (localhost only)
- To expose externally, add port forwarding

### Credentials

- `credentials.json` is mounted read-only
- `token.json` is mounted with read/write (for OAuth refresh)
- Both are in `.dockerignore` (not included in image)

---

## 📊 Resource Usage

### Expected Resources

- **CPU:** 5-15%
- **RAM:** 300-700 MB
- **Disk:** ~2 GB (image size)
- **Network:** <1 MB per update

### Optimize Performance

Limit resources in `docker-compose.yml`:
```yaml
services:
  letu-tracker:
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          memory: 512M
```

---

## 🌐 Remote Access (Optional)

### Using ngrok

To access from anywhere:

```bash
# Install ngrok
# Then run:
ngrok http 5000

# You'll get a URL like: https://abc123.ngrok.io
# Share this URL with others
```

### Using Reverse Proxy

For production deployment:
- Use Nginx or Apache as reverse proxy
- Add SSL certificate (Let's Encrypt)
- Configure domain name

---

## 🚀 Production Deployment

### Deploy to Cloud

#### Docker Hub (for sharing)

```bash
# Build and tag
docker build -t yourusername/letu-tracker:1.0 .

# Push to Docker Hub
docker push yourusername/letu-tracker:1.0

# Others can now run:
docker pull yourusername/letu-tracker:1.0
docker run -p 5000:5000 -v ./backend/credentials.json:/app/backend/credentials.json yourusername/letu-tracker:1.0
```

#### AWS ECS / Google Cloud Run

Both support Docker images directly:
1. Push image to container registry
2. Create service from image
3. Configure ports and volumes
4. Done!

---

## 📝 Docker Commands Cheat Sheet

```bash
# Build image
docker-compose build

# Start (detached mode)
docker-compose up -d

# Start (foreground with logs)
docker-compose up

# Stop
docker-compose down

# Restart
docker-compose restart

# View logs
docker-compose logs -f

# Check status
docker-compose ps

# Execute command in container
docker-compose exec letu-tracker bash

# View resource usage
docker stats

# Clean up everything
docker-compose down -v
docker system prune -a
```

---

## 🆚 Docker vs Traditional Installation

| Feature | Docker | Traditional |
|---------|--------|-------------|
| Setup Time | 5-10 min (first time) | 20-30 min |
| Prerequisites | Just Docker | Python, Node.js, Chrome |
| Daily Startup | Instant (~5s) | ~30s |
| Updates | One command | Multiple steps |
| Conflicts | None (isolated) | Possible |
| Portability | 100% | Depends on OS |
| Recommended For | Non-technical users | Developers |

---

## ✅ Checklist

Before first run:

- [ ] Docker installed and running
- [ ] Project files downloaded
- [ ] `credentials.json` in `backend/` folder
- [ ] Completed Google Sheets setup
- [ ] Ready to run `docker-start.bat` or `./docker-start.sh`

---

## 🎉 You're Ready!

**Windows:** Double-click `docker-start.bat`  
**Linux/Mac:** Run `./docker-start.sh`

The application will:
1. ✅ Build the Docker image (first time only)
2. ✅ Start the container
3. ✅ Open your browser
4. ✅ Be ready to track livestreams!

**Happy tracking with Docker! 🐳📊✨**

---

## 📞 Need Help?

- Docker issues → Check [Docker Documentation](https://docs.docker.com/)
- Application issues → Check `EXAMPLES.md` for troubleshooting
- Google Sheets → Check `GOOGLE_SHEETS_SETUP.md`
