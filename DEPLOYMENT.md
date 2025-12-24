# Deployment Guide

This guide covers various deployment options for the Adaptive Physics Tutor.

## 📋 Table of Contents

1. [Streamlit Cloud (Easiest)](#streamlit-cloud)
2. [Local Development](#local-development)
3. [Docker](#docker)
4. [Heroku](#heroku)
5. [AWS/GCP/Azure](#cloud-platforms)

---

## 🎈 Streamlit Cloud

The easiest and recommended way to deploy.

### Prerequisites

- GitHub account
- Google API key with Gemini access

### Steps

1. **Fork this repository** on GitHub

2. **Sign up for Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - It's completely free!

3. **Deploy your app**
   - Click "New app"
   - Repository: Select your forked repo
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Advanced settings"

4. **Add secrets** (in the Secrets section):
   ```toml
   GOOGLE_API_KEY = "your-google-api-key-here"
   GEMINI_MODEL = "gemini-2.0-flash"
   TEMPERATURE = "0.7"
   MAX_EXCHANGES = "6"
   SCAFFOLD_TRIGGER = "3"
   ```

5. **Click "Deploy"**

Your app will be live at `https://[app-name].streamlit.app` in a few minutes! 🎉

### Managing Your Deployed App

- **Logs**: View in the Streamlit Cloud dashboard
- **Reboot**: Click "Reboot" to restart the app
- **Update**: Push to your GitHub repo to auto-deploy changes
- **Delete**: Click "Delete app" in settings

---

## 💻 Local Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ANURAGMN/simulation_to_concept_version3_github.git
   cd simulation_to_concept_version3_github
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

### Run

#### Streamlit App
```bash
streamlit run app.py
```

Open browser to `http://localhost:8501`

#### Terminal App
```bash
python main.py
```

---

## 🐳 Docker

### Build Image

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build
docker build -t adaptive-physics-tutor .

# Run
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY=your-key-here \
  adaptive-physics-tutor
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - GEMINI_MODEL=gemini-2.0-flash
      - TEMPERATURE=0.7
    env_file:
      - .env
```

Run with:
```bash
docker-compose up
```

---

## 🚀 Heroku

### Prerequisites

- Heroku account
- Heroku CLI installed

### Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create app**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**
   ```bash
   heroku config:set GOOGLE_API_KEY=your-key-here
   heroku config:set GEMINI_MODEL=gemini-2.0-flash
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **Open app**
   ```bash
   heroku open
   ```

### Files Used

- `Procfile`: Tells Heroku how to run the app
- `runtime.txt`: Specifies Python version
- `requirements.txt`: Lists Python dependencies

---

## ☁️ Cloud Platforms

### AWS (Elastic Beanstalk)

1. Install AWS CLI and EB CLI
2. Configure credentials:
   ```bash
   aws configure
   ```

3. Initialize EB:
   ```bash
   eb init -p python-3.12 adaptive-physics-tutor
   ```

4. Create environment:
   ```bash
   eb create production
   ```

5. Set environment variables:
   ```bash
   eb setenv GOOGLE_API_KEY=your-key-here
   ```

6. Deploy:
   ```bash
   eb deploy
   ```

### Google Cloud Platform (Cloud Run)

1. Install gcloud CLI
2. Build container:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT-ID/adaptive-tutor
   ```

3. Deploy:
   ```bash
   gcloud run deploy adaptive-tutor \
     --image gcr.io/PROJECT-ID/adaptive-tutor \
     --platform managed \
     --set-env-vars GOOGLE_API_KEY=your-key-here
   ```

### Azure (App Service)

1. Install Azure CLI
2. Create resource group:
   ```bash
   az group create --name tutor-rg --location eastus
   ```

3. Create app service plan:
   ```bash
   az appservice plan create --name tutor-plan --resource-group tutor-rg --sku B1 --is-linux
   ```

4. Create web app:
   ```bash
   az webapp create --resource-group tutor-rg --plan tutor-plan --name adaptive-tutor --runtime "PYTHON:3.12"
   ```

5. Configure and deploy:
   ```bash
   az webapp config appsettings set --resource-group tutor-rg --name adaptive-tutor --settings GOOGLE_API_KEY=your-key-here
   az webapp up --name adaptive-tutor --resource-group tutor-rg
   ```

---

## 🔒 Security Best Practices

### API Keys

- **Never** commit API keys to Git
- Use environment variables or secrets management
- Rotate keys regularly
- Use different keys for dev/prod

### Access Control

For production deployments:

1. **Enable authentication** in Streamlit Cloud settings
2. **Use HTTPS** (automatic on most platforms)
3. **Set up rate limiting** to prevent abuse
4. **Monitor usage** and set up alerts

### Environment Variables

Always store sensitive data as environment variables:

```bash
# .env file (never commit this!)
GOOGLE_API_KEY=your-actual-key
GEMINI_MODEL=gemini-2.0-flash
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "GOOGLE_API_KEY not found"**
- Solution: Make sure you've set the environment variable or Streamlit secret

**Issue: "Module not found"**
- Solution: Run `pip install -r requirements.txt`

**Issue: "Port already in use"**
- Solution: Use a different port: `streamlit run app.py --server.port 8502`

**Issue: Deployment timeout**
- Solution: Increase timeout in platform settings or optimize cold start

### Logs

- **Streamlit Cloud**: View in dashboard
- **Heroku**: `heroku logs --tail`
- **Docker**: `docker logs container-id`
- **AWS**: Check CloudWatch logs

---

## 📊 Performance Optimization

### Caching

Already implemented in the app using Streamlit's caching.

### Resource Limits

Recommended resources for production:

- **CPU**: 1-2 cores
- **RAM**: 512MB - 1GB
- **Storage**: 500MB

### Scaling

- **Vertical**: Upgrade instance size
- **Horizontal**: Deploy multiple instances with load balancer

---

## 📞 Support

If you encounter issues:

1. Check the [README](README.md) for basic setup
2. Review this deployment guide
3. Check [GitHub Issues](https://github.com/ANURAGMN/simulation_to_concept_version3_github/issues)
4. Open a new issue with:
   - Deployment platform
   - Error messages
   - Steps to reproduce

---

## ✅ Deployment Checklist

- [ ] API key configured
- [ ] Dependencies installed
- [ ] Environment variables set
- [ ] App runs locally
- [ ] Secrets not committed to Git
- [ ] Platform-specific files configured
- [ ] Health checks working
- [ ] Logs accessible
- [ ] Domain configured (optional)
- [ ] SSL/HTTPS enabled

Happy deploying! 🚀
