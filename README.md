##  AI-Powered Daily Tech Digest Pipeline

An automated, serverless ETL (Extract, Transform, Load) data pipeline that cures information overload. This script aggregates trending technology, machine learning, and design news, uses Google's Gemini AI to summarize the content, and delivers a concise morning briefing directly to an email inbox.

Built to optimize research workflows for content creation and technical deep-dives.

  Architecture (How it Works)

This project follows a lightweight ETL architecture:
1. **Extract:** Uses `feedparser` to programmatically pull structured metadata from multiple RSS feeds (e.g., TechCrunch, Towards Data Science, UX Collective) bypassing heavy web scrapers and algorithmic noise.
2. **Transform:** Passes raw article snippets to the **Google GenAI SDK** (`gemini-3.5-flash`), prompting the LLM to act as a research assistant and distill complex articles into punchy, 2-sentence summaries.
3. **Load:** Compiles the AI-generated summaries into an HTML layout and uses Python's built-in `smtplib` to securely deliver the payload via Gmail's SMTP servers.
4. **Orchestration:** Deployed serverlessly via **GitHub Actions**, configured with a cron job to execute daily at 05:00 UTC.

##  Tech Stack

* **Language:** Python 3.10+
* **Data Extraction:** `feedparser`
* **AI Transformation:** Google GenAI SDK (`gemini-3.5-flash`)
* **Email Delivery:** `smtplib`, `email.mime`
* **Cloud Orchestration:** GitHub Actions (CI/CD Schedule)

## Local Setup & Testing

To run or test this pipeline on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/daily-tech-digest.git](https://github.com/yourusername/research-automation-script.git)
   cd research-automation-script

```

2. **Install dependencies:**
```bash
pip install feedparser google-genai python-dotenv

```


3. **Set up Environment Variables:**
Create a `.env` file in the root directory and add your secure credentials:
```text
GEMINI_API_KEY=your_google_ai_studio_key
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_gmail_app_password

```


4. **Run the script:**
```bash
python digest.py

```


*Check your inbox for the successful payload delivery.*

##  Serverless Deployment (GitHub Actions)

This pipeline runs hands-free in the cloud without needing a dedicated server.

1. Navigate to **Settings > Secrets and variables > Actions** in your GitHub repository.
2. Add the following Repository Secrets to match the environment variables above:
* `GEMINI_API_KEY`
* `SENDER_EMAIL`
* `EMAIL_PASSWORD`


3. The `.github/workflows/daily_digest.yml` file is already configured. GitHub will automatically spin up an Ubuntu runner and execute the pipeline every day.
4. **Manual Trigger:** You can manually test the cloud deployment by navigating to the **Actions** tab, selecting the workflow, and clicking **Run workflow**.


```
