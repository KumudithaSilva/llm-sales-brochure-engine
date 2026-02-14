# 🚀 Sales-Brochure-Engine — LLM-Driven Company Brochure Generator

<p align="center">
  <img src="https://img.shields.io/badge/LLM-OpenAI%20-6A1B9A" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-FF7043" />
  <img src="https://img.shields.io/badge/Web%20Scraping-Playwright-455A164" />
  <img src="https://img.shields.io/badge/Design-SOLID%20Principles-17256b" />
  <img src="https://img.shields.io/badge/Code%20Style-PEP8-045E1A" />
  <img src="https://img.shields.io/badge/License-MIT-45a5d7" />
</p>

---

# llm-sales-brochure-engine

🤖📈 LLM-driven system for generating professional sales brochures by crawling, aggregating, and synthesizing multi-page company website content using OpenAI APIs.

---

## 🌟 Project Overview

Sales-Brochure-Engine is a production-oriented, LLM-driven system designed to automatically generate professional, high-quality sales brochures for companies.

The goal of this project is to create impactful and scalable AI solutions that help businesses:

- Re-brand and refine their vision & mission  
- Clearly communicate what they do and their value to society  
- Present a polished, structured marketing-ready company overview  
- Improve how clients understand their business impact  

This system bridges the gap between raw company information and a professionally structured sales narrative powered by Large Language Models (LLMs).

---

## 📦 The Real-World Problem

In modern advertising and marketing, many companies struggle with:

- ❌ Providing reliable, high-quality marketing content  
- ❌ Delivering a clear and structured company overview  
- ❌ Presenting accurate and up-to-date information  
- ❌ Communicating business value effectively  

These challenges often lead to:

- 🚫 Loss of potential future clients  
- 📉 Weak brand positioning  
- 🔍 Confusion about company services and impact  
- 🤝 Missed business opportunities  

---

## 🎯 Our Solution

Sales Brochure Engine introduces an automated LLM-powered brochure generation pipeline.

### 🧠 Workflow Summary

1. 🌐 User provides the company’s main website URL  
2. 🔍 The system uses web scraping to:
   - Extract internal links  
   - Retrieve relevant and up-to-date content  
3. 🧩 The engine determines which links and content are most valuable  
4. 📝 A structured system + user prompt is generated  
5. 🤖 The LLM evaluates the request and generates a professional sales brochure  
6. 📄 The polished brochure is returned to the users  


---

## 🧠 Key Design Principles

This system follows senior-level software engineering practices:

- 🛠️ Maintainability — Clear modular boundaries  
- 🔄 Component Transparency — Full logging for each workflow stage  
- 🧪 Testability — Isolated components via interfaces  
- 🔮 Extensibility — Add new features without modifying core logic  
- 🧱 SOLID Principles — Clean and scalable architecture  
- 🧼 Clean Architecture — Dependency inversion & separation of concerns  

---

## 📸 Sales Brochure App Output (UI Preview)

<img width="500" height="900" alt="image" src="https://github.com/user-attachments/assets/24ac4975-5cb9-4d7d-bd2b-9fae2e3d06d9"/>


## 📌 How It Works

- 🌐 User enters company website  
- 🚀 Clicks “Generate Brochure”  
- 📄 Receives a structured, professional sales brochure  
- 📥 Output displayed in formatted markdown via Streamlit UI  

---

## 🧩 Core Functionalities

### 🔹 DotEnvLoader  
Loads environment variables securely.

### 🔹 OpenAIApiKeyProvider  
Provides OpenAI API keys from environment configuration.

### 🔹 OpenAIClientWrapper  
Concrete wrapper around the OpenAI Python SDK.

### 🔹 OpenAIService  
Service class responsible for interacting with the AI client.

### 🔹 PlaywrightWebScraper  
- Handles dynamic JS-rendered pages  
- Extracts internal links  
- Extracts main textual content  

### 🔹 PromptProvider  
Provides system and user prompts for structured one-shot learning.

### 🔹 SalesBrochureOrchestrator  
Coordinates scraping + prompt creation + AI generation using interface-based dependencies.

### 🔹 SalesBrochureContainer  
Factory class that wires dependencies and returns an orchestrator instance.

### 🔹 FastAPI Backend  
Exposes endpoint to:
- Generate brochure  
- Fetch relevant links  

### 🔹 Streamlit UI  
Frontend interface allowing users to:
- Enter company URL  
- Generate brochure  
- View formatted output  



## 🧭 Future Enhancements

- 📊 AI-based content scoring before brochure generation  
- 🌍 Multi-language brochure generation  
- 📄 PDF export feature  
- 🔐 Authentication & rate limiting  



## 🤝 Contributing

We welcome contributions related to:

- 🧠 AI & Prompt Engineering  
- 🧱 Architecture Improvements  
- 🌐 Backend Enhancements  
- 🎨 UI Improvements  
- 🧪 Testing & Quality Assurance  

### Contribution Steps

1. 🍴 Fork the repository  
2. 🌿 Create a `feature/*` branch  
3. 🛠️ Commit changes with clear messages  
4. 📤 Open a Pull Request  


## 🔀 Git Flow Workflow

The project follows a Git Flow–inspired workflow:

- 🌿 `master` — Stable, production-ready releases  
- 🌱 `develop` — Active development branch  
- ✨ `feature/*` — New feature branches  

### Typical Workflow

1. Pull latest changes from `develop`  
2. Create a `feature/*` branch  
3. Implement and test changes  
4. Open PR → Merge into `develop`  
5. Release from `develop` → Merge into `master`  

This ensures stability while enabling safe feature development.

---

## 💡 Inspiration

Sales-Brochure-Engine demonstrates how LLMs + Clean Architecture + Modern Python backend/frontend tools can be combined to solve real-world marketing challenges at scale.

This project reflects how AI can transform raw company data into strategic, persuasive, and structured business communication.


