# 🚀 Getting Started with Letu Live Tracker

**The complete guide to get you up and running in minutes!**

---

## 🎯 Choose Your Path

We offer **TWO installation methods**. Pick the one that's right for you:

<table>
<tr>
<td width="50%" align="center">

### 🐳 **Docker Method**
**RECOMMENDED for most users!**

✅ Just install Docker  
✅ One-click startup  
✅ No Python/Node.js needed  
✅ Works everywhere  

**Difficulty:** ⭐ Very Easy  
**Time:** 10 minutes

[📖 Docker Guide →](DOCKER_GUIDE.md)

</td>
<td width="50%" align="center">

### 🔧 **Traditional Method**
**For developers**

✅ Full control  
✅ Easy debugging  
✅ Direct code access  
✅ Lighter weight  

**Difficulty:** ⭐⭐⭐ Moderate  
**Time:** 30 minutes

[📖 Quick Start →](QUICKSTART.md)

</td>
</tr>
</table>

**Not sure?** → [Compare methods](INSTALLATION_COMPARISON.md) | **Still not sure?** → **Use Docker!** 🐳

---

## 🐳 Docker Installation (Easiest!)

### Step 1: Install Docker (5 minutes)

**Windows/Mac:**
1. Download Docker Desktop: https://www.docker.com/products/docker-desktop
2. Install and start Docker Desktop
3. Wait for Docker to fully start (check system tray)

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose
sudo systemctl start docker

# Add your user to docker group
sudo usermod -aG docker $USER
# Log out and log back in
```

### Step 2: Get Google Credentials (15 minutes)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project
3. Enable Google Sheets API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download as `credentials.json`
6. Place in `backend/` folder

📖 **Detailed guide:** [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md)

### Step 3: Start the Application (1 minute)

**Windows:**
```
Double-click: docker-start.bat
```

**Linux/Mac:**
```bash
./docker-start.sh
```

### Step 4: Use the App! ✨

- Browser opens automatically → http://localhost:5173
- Enter Session ID (from Shopee livestream URL)
- Enter Google Sheet URL
- Click "Start Tracking"
- **Done!** Data updates every 30 seconds! 📊

---

## 🔧 Traditional Installation

### Step 1: Install Prerequisites (10 minutes)

**Windows:**
- Python 3.8+: https://www.python.org/downloads/ ✅ Check "Add to PATH"
- Node.js 16+: https://nodejs.org/
- Google Chrome: https://www.google.com/chrome/

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv nodejs npm chromium-browser
```

**Mac:**
```bash
brew install python3 node
# Install Chrome manually
```

### Step 2: Setup Project (5 minutes)

**Windows:**
```cmd
setup.bat
```

**Linux/Mac:**
```bash
./setup.sh
```

### Step 3: Get Google Credentials (15 minutes)

Same as Docker method - see Step 2 above.

### Step 4: Start the Application (1 minute)

**Windows:**
```cmd
start.bat
```

**Linux/Mac:**
```bash
./start.sh
```

### Step 5: Use the App! ✨

Same as Docker method - see Step 4 above.

---

## 📊 Quick Comparison

| | 🐳 Docker | 🔧 Traditional |
|---|-----------|----------------|
| **Prerequisites** | Just Docker | Python + Node.js + Chrome |
| **Setup Time** | 10 min | 30 min |
| **Startup Time** | 5 sec | 30 sec |
| **Complexity** | ⭐ Easy | ⭐⭐⭐ Moderate |
| **Best For** | Everyone! | Developers |

**Our recommendation: Use Docker!** 🐳

---

## 📚 Next Steps After Installation

### First Time Use

1. **Create a Google Sheet**
   - Go to https://sheets.google.com
   - Create blank spreadsheet
   - Copy the URL

2. **Get a Session ID**
   - From Shopee livestream dashboard
   - Look for `?sessionId=XXXXX` in URL
   - Example: `29060044`

3. **Test Preview**
   - Enter Session ID
   - Click "Preview Data"
   - Verify products appear

4. **Start Tracking**
   - Enter Google Sheet URL
   - Click "Start Tracking"
   - First time: Sign in to Google
   - Allow permissions
   - Data updates automatically!

### Daily Use

**With Docker:**
```bash
# Start
docker-start.bat  # or ./docker-start.sh

# Stop
docker-stop.bat   # or ./docker-stop.sh
```

**Traditional:**
```bash
# Start
start.bat         # or ./start.sh

# Stop
Close the terminal windows
```

---

## 🎓 Learning Resources

### Essential Reading

1. **[INDEX.md](../INDEX.md)** - Documentation navigation hub
2. **[EXAMPLES.md](EXAMPLES.md)** - Real-world usage examples
3. **[GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md)** - Complete API setup

### For Different Users

**Beginners:**
- [VISUAL_GUIDE.md](VISUAL_GUIDE.md) - Step-by-step with pictures
- [QUICKSTART.md](QUICKSTART.md) - 5-minute guide

**Windows Users:**
- [WINDOWS_INSTALLATION.md](WINDOWS_INSTALLATION.md) - Windows-specific guide

**Developers:**
- [DEVELOPMENT.md](DEVELOPMENT.md) - Developer guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design

**Docker Users:**
- [DOCKER_GUIDE.md](DOCKER_GUIDE.md) - Complete Docker guide
- [INSTALLATION_COMPARISON.md](INSTALLATION_COMPARISON.md) - Compare methods

---

## 🐛 Troubleshooting

### Docker Issues

**Docker won't start:**
- Make sure Docker Desktop is running
- Check system tray icon
- Restart Docker Desktop

**Build fails:**
```bash
docker-compose build --no-cache
```

**Can't access app:**
```bash
# Check if running
docker-compose ps

# Check logs
docker-compose logs -f
```

### Traditional Installation Issues

**Python not found:**
- Reinstall Python with "Add to PATH" checked
- Restart computer
- Try: `python --version`

**Node.js not found:**
- Install from https://nodejs.org/
- Restart computer
- Try: `node --version`

**Port in use:**
```bash
# Change port in config or stop other services
netstat -ano | findstr :5000  # Windows
lsof -i :5000                 # Linux/Mac
```

### Google Sheets Issues

**Permission denied:**
```bash
# Delete token and re-authenticate
rm backend/token.json
# Restart application
```

**credentials.json not found:**
- Complete GOOGLE_SHEETS_SETUP.md
- Place file in backend/ folder
- Check filename is exact

---

## ⚡ Quick Commands Reference

### Docker

```bash
# Start
docker-start.bat / ./docker-start.sh

# Stop
docker-stop.bat / ./docker-stop.sh

# View logs
docker-compose logs -f

# Restart
docker-compose restart

# Clean rebuild
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Traditional

```bash
# Start
start.bat / ./start.sh

# Stop
# Close terminal windows or Ctrl+C

# View backend logs
# In backend terminal

# View frontend logs
# In frontend terminal

# Restart
# Close and run start script again
```

---

## 📖 Complete Documentation

### Installation & Setup
- [DOCKER_GUIDE.md](DOCKER_GUIDE.md) - Docker installation
- [QUICKSTART.md](QUICKSTART.md) - Traditional installation
- [WINDOWS_INSTALLATION.md](WINDOWS_INSTALLATION.md) - Windows guide
- [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md) - API setup
- [INSTALLATION_COMPARISON.md](INSTALLATION_COMPARISON.md) - Compare methods

### Usage & Examples
- [EXAMPLES.md](EXAMPLES.md) - Real-world scenarios
- [VISUAL_GUIDE.md](VISUAL_GUIDE.md) - Visual walkthrough
- [README.md](../README.md) - Main documentation

### Technical
- [DEVELOPMENT.md](DEVELOPMENT.md) - Developer guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design
- [backend/README.md](../backend/README.md) - Backend docs
- [frontend/README.md](../frontend/README.md) - Frontend docs

### Project Info
- [INDEX.md](../INDEX.md) - Documentation index
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Project overview
- [CONTRIBUTING.md](../CONTRIBUTING.md) - How to contribute
- [CHANGELOG.md](../CHANGELOG.md) - Version history

---

## ✅ Success Checklist

After installation, verify:

- [ ] Application starts without errors
- [ ] Browser opens to http://localhost:5173
- [ ] UI loads correctly
- [ ] Can enter Session ID and Sheet URL
- [ ] Preview button works
- [ ] Google authentication works
- [ ] Data appears in Google Sheet
- [ ] Updates happen every 30 seconds

If all checked ✅ **You're all set!** 🎉

---

## 💡 Pro Tips

1. **Use Docker** for ease of use
2. **Keep credentials.json safe** - back it up!
3. **One Google Sheet per session** for organization
4. **Check logs** if something goes wrong
5. **Read EXAMPLES.md** for advanced usage
6. **Join the community** for help and tips

---

## 🎯 What to Do Next

### Immediate Next Steps
1. ✅ Complete installation (above)
2. ✅ Test with preview
3. ✅ Track your first session
4. ✅ Verify data in Google Sheet

### Learning Path
1. 📖 Read [EXAMPLES.md](EXAMPLES.md) for workflows
2. 📖 Review [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md)
3. 📖 Explore advanced features

### Optional
- 🎨 Customize the UI
- 🔧 Modify configuration
- 🚀 Deploy to cloud
- 🤝 Contribute improvements

---

## 🆘 Need Help?

1. **Check troubleshooting** (above)
2. **Read the docs** (full list above)
3. **Check logs** for error messages
4. **Review EXAMPLES.md** for solutions
5. **Open an issue** on GitHub

---

## 🎉 You're Ready to Start!

**Quick Decision Guide:**

- **Want easy setup?** → Use Docker (RECOMMENDED!)
- **Are you a developer?** → Traditional works too
- **Still deciding?** → Use Docker!

**Let's get started! Pick your method above and dive in!** 🚀

---

**Happy tracking! 📊✨**
