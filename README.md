

# Web Scraping E-Commerce Product Reviews

## Overview

This repository contains a set of tools and scripts for web scraping e-commerce product reviews. The goal is to gather valuable insights and data from customer reviews on various online platforms.

## Features

- **Scalability**: Easily scale the scraping process to collect reviews from multiple products and platforms.
- **Customization**: Adapt the scripts to suit different e-commerce websites and review formats.
- **Search Option**: Search for your desired products and extract the customer review of a specific product.

## Getting Started

### Prerequisites

- Python 3.x
- Beautiful Soup


### Steps to run

<div style="padding-bottom:10px"><b>STEP 00 :</b> Clone the repository</div>

```bash
git clone https://github.com/utpalpaul108/review-scrapper-aws.git
```
<div style="padding-top:10px"><b>STEP 01 :</b> Create a virtial environment after opening the repository</div>

Using Anaconda Virtual Environments

```bash
conda create -n venv python=3.10 -y
conda activate venv
```
Or for Linux operating system, you can use that

```bash
python3.10 -m venv venv
source venv/bin/activate
```

<div style="padding-top:10px; padding-bottom:10px"><b>STEP 02 :</b> Install the requirements</div>

```bash
pip install -r requirements.txt
```

Finally, run the following command to open your application:
```bash
python app.py
```

<div style="padding-top:10px"><b>STEP 03 :</b> Open the application</div>

Now, open up your local host with a port like that on your web browser.
```bash
http://localhost:8080
```

After opening the application, you will find a search box. Here, you can search for any product and extract the product review in a csv file.
