import feedparser
from google import genai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load the passwords from the .env file
load_dotenv()

# Securely pull credentials into variables
gemini_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
email_password = os.environ.get('EMAIL_PASSWORD')
receiver_email = sender_email 

client = genai.Client(api_key=gemini_key)


# 2. Your highly curated, multi-domain source list
feed_urls = [
    "https://techcrunch.com/feed/",
    "https://towardsdatascience.com/feed",
    "https://uxdesign.cc/feed"
]

print("Initializing multi-source AI data pipeline...")
email_body = "<h1>Your Automated Tech & ML Digest</h1><hr>"

# 3. Outer Loop: Extracting from each publication source
for url in feed_urls:
    news_feed = feedparser.parse(url)
    website_title = getattr(news_feed.feed, 'title', 'Unknown Source') 
    email_body += f"<h2>Top Updates from {website_title}</h2>"
    
    # Inner Loop: Extracting the top 3 items per source
    for article in news_feed.entries[:3]:
        title = article.title
        link = article.link
        snippet = article.get('summary', '') 
        
        # Transformation: Leveraging LLMs for context-rich summaries
        prompt = f"Based on this title and snippet, write a concise, 2-sentence summary tailored for a sharp, tech-savvy audience.\nTitle: {title}\nSnippet: {snippet}"
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        
        # Formatting the output payload
        email_body += f"<h3>{title}</h3>"
        email_body += f"<p><strong>AI Summary:</strong> {response.text}</p>"
        email_body += f"<a href='{link}'>Read Full Article</a><br><br>"
        
    email_body += "<hr>" 

print("Summaries generated successfully. Deploying email payload...")

# 4. Load: Delivering the final data product via SMTP
try:
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Daily Briefing: Tech, Design & Machine Learning"
    message.attach(MIMEText(email_body, "html"))
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, email_password)
    server.send_message(message)
    server.quit()
    print("Pipeline execution complete. Payload delivered.")
except Exception as e:
    print(f"Pipeline delivery failure: {e}")