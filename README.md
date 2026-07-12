# Automated Hacker News Headlines Emailer

## Overview

The Automated Hacker News Headlines Emailer is a Python-based automation project that extracts the latest top stories from Hacker News and sends them to a specified email address in a formatted HTML email.

This project demonstrates web scraping, data extraction, email automation, and Python scripting skills.

## Features

* Fetches top headlines from Hacker News
* Extracts news titles using BeautifulSoup
* Generates HTML-formatted email content
* Sends automated emails using Gmail SMTP
* Provides a simple and lightweight automation workflow

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* SMTP (smtplib)
* MIME Email Formatting

## Project Structure

```text
hacker_news_headline_email.py
README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd hacker-news-emailer
```

### Install Dependencies

```bash
pip install requests beautifulsoup4
```

## Configuration

Update the following variables in the script:

```python
FROM = "your_email@gmail.com"
TO = "recipient_email@gmail.com"
PASS = "your_app_password"
```

### Gmail App Password

To send emails using Gmail SMTP:

1. Enable Two-Factor Authentication on your Google Account.
2. Generate an App Password from Google Account Security Settings.
3. Use the generated App Password instead of your Gmail account password.

## Usage

Run the script:

```bash
python hacker_news_headline_email.py
```

The script will:

1. Connect to Hacker News.
2. Extract the latest headlines.
3. Create an HTML email.
4. Send the email to the configured recipient.

## Sample Output

Subject:

```text
Top News Stories HN [Automated Email]
```

Email Content:

```text
HN Top Stories

1. Example Headline 1
2. Example Headline 2
3. Example Headline 3
...
```

## Learning Outcomes

Through this project, I learned:

* Web scraping using BeautifulSoup
* Making HTTP requests with Requests
* Parsing HTML content
* Email automation using SMTP
* Working with MIME email messages
* Debugging authentication and scraping issues

## Future Enhancements

* Include article URLs in the email
* Schedule daily email delivery
* Generate HTML email templates
* Add logging and error handling
* Store email credentials using environment variables
* Deploy as a cloud-based scheduled service

## Author

Maheshwari Inamadar

Bachelor of Engineering (Computer Science and Engineering)
BLDEA's College of Engineering and Technology, Vijayapura
