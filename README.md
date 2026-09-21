# C-SK-xASI 🌏🤖

### 💻 Tech Stack

**Core Programming Languages & Core Systems**  
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) 
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white) 
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

**Platform Support & Hardware Architecture**  
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) 
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) 
![Cross-Platform](https://img.shields.io/badge/Cross_Platform-Enabled-blue?style=for-the-badge)

**Low-Level Infrastructure & Performance**  
![Asyncio](https://img.shields.io/badge/AsyncIO-Concurrency-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-499848?style=for-the-badge) 
![HTTPX](https://img.shields.io/badge/HTTPX-Async_Requests-005571?style=for-the-badge)

**Cybersecurity & Offensive Auditing**  
![Regex](https://img.shields.io/badge/Regex-PII_Redaction-FF0000?style=for-the-badge) 
![Data Sovereignty](https://img.shields.io/badge/Data_Sovereignty-Filtered-brightgreen?style=for-the-badge) 
![Compliance Pipeline](https://img.shields.io/badge/Regional_Compliance-Active-000000?style=for-the-badge&logo=shield&logoColor=white)

**DevOps & Build Tools**  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) 
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) 
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white) 
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)

**Artificial Intelligence**  
![OpenAI Standard](https://img.shields.io/badge/OpenAI_API_Schema-412991?style=for-the-badge&logo=openai&logoColor=white) 
![LLM Ensemble](https://img.shields.io/badge/10+_Frontier_LLMs-Orchestrated-8A2BE2?style=for-the-badge) 
![Neural Translation](https://img.shields.io/badge/Dynamic_Pivot_Layer-Translation-00BFFF?style=for-the-badge)

**Cloud Providers**  
![Alibaba Cloud](https://img.shields.io/badge/Alibaba_Cloud-FF6A00?style=for-the-badge&logo=alibabacloud&logoColor=white) 
![Naver Cloud](https://img.shields.io/badge/Naver_Cloud-03C75A?style=for-the-badge&logo=naver&logoColor=white) 
![Tencent Cloud](https://img.shields.io/badge/Tencent_Cloud-0052D9?style=for-the-badge&logo=tencent-qq&logoColor=white)


### 🎒 Explanation
Imagine you have a big group of super-smart robot friends, but some live in China and some live in South Korea! 🇨🇳🇰🇷 If you ask them a question, they might speak different languages or have different rules. This project is like a super-smart walkie-talkie. 📻 You ask one question, and it talks to **all** the robots at the same time! It translates their languages, makes sure they follow the safety rules, and then mixes all their best ideas into one perfect answer just for you! ✨

---

### 🤔 What is this about?
C-SK-xASI is an enterprise cross-border AI orchestrator API[span_0](start_span)[span_0](end_span). It acts as a secure, high-speed bridge connecting Chinese and South Korean Large Language Models (LLMs).

### 🛠️ What this does?
It takes a single prompt and sends it to multiple frontier AI models from both regions at the same time using specialized gateways (`cn_gateway.py` and `sk_gateway.py`)[span_1](start_span)[span_1](end_span). It routes requests to models like Qwen, DeepSeek, Kimi, Solar, and HyperClova[span_2](start_span)[span_2](end_span). 

### ⚙️ How does this work?
It uses a high-speed three-tier pipeline built in Python with FastAPI[span_3](start_span)[span_3](end_span):
1. **Level 1 (Gather):** Sends your question to 10+ AI models at once and gathers their answers[span_4](start_span)[span_4](end_span).
2. **Level 2 (Translate & Verify):** Uses a pivot translator to automatically fix language barriers, such as converting Hanja characters to Hangul[span_5](start_span)[span_5](end_span). 
3. **Level 3 (Filter & Synthesize):** Runs the data through a compliance pipeline (`c_compliance.py`) to strip out private identifying information (PII) and a localization pipeline (`k_localization.py`) before giving you the final synthesized answer[span_6](start_span)[span_6](end_span).

### 🛑 What problems this solves?
* **Language Barriers:** Automatically translates complex regional character systems so the models can understand each other.
* **Safety & Compliance:** Ensures AI answers follow regional data privacy rules by scrubbing sensitive information before the user ever sees it.
* **Fragmented AI:** Stops you from having to log into 10 different AI websites to get different perspectives on a single problem. 

### 🥶 Why is this cool?
Instead of relying on just one AI, you get a "super-answer" voted on and combined from the smartest models in Asia, all while keeping the data perfectly safe and lightning-fast! ⚡

### 💻 How to install this?
Because this project includes both a `Dockerfile` and `docker-compose.yml`, the easiest way to run it is with Docker[span_7](start_span)[span_7](end_span). 

**Option 1: Using Docker Compose (Recommended)**
```bash
git clone [https://github.com/darnellwashingtonjr94-art/C-SK-xASI.git](https://github.com/darnellwashingtonjr94-art/C-SK-xASI.git)
cd C-SK-xASI
docker-compose up --build
