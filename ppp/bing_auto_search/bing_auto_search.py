import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# --------------------配置区域--------------------
MIN_SEARCH_TIMES = 40  # 最少搜索次数
MAX_SEARCH_TIMES = 60  # 最多搜索次数
WAIT_TIME = (2, 6)  # 每次搜索后等待的时间范围（秒）

KEYWORDS = [
    # 技术 & 编程
    "best programming languages 2025", "python vs javascript", "machine learning tutorials",
    "what is cloud computing", "how to build a website", "C++ smart pointers", "Git vs SVN",
    "docker vs virtual machine", "REST vs GraphQL", "how does blockchain work", "WebAssembly tutorial",

    # ChatGPT & AI
    "how ChatGPT works", "latest OpenAI news", "future of artificial intelligence", "AI tools for productivity",
    "ChatGPT for coding", "DALL·E image generation", "prompt engineering tips",

    # 金融 & 投资
    "Tesla stock news", "Bitcoin price prediction", "how to invest in ETFs", "stock market news today",
    "is gold a good investment", "S&P 500 index meaning", "cryptocurrency tax rules",

    # 健康 & 生活方式
    "healthy breakfast ideas", "how to sleep better", "how to reduce stress", "is coffee healthy",
    "benefits of drinking water", "best home workouts", "intermittent fasting benefits",

    # 娱乐 & 热门文化
    "Game of Thrones recap", "best Netflix shows 2025", "funny cat videos", "Marvel vs DC",
    "upcoming movies 2025", "Oscars best picture winners", "top YouTubers 2025", "Twitch vs Kick",

    # 教育 & 学习
    "top universities in the world", "best online courses", "how to learn English fast",
    "study tips for exams", "what is the GRE test", "is SAT required in 2025",

    # 旅游 & 地理
    "best travel destinations 2025", "how to get cheap flights", "top 10 cities to live in",
    "weather in Tokyo", "hiking trails near me", "digital nomad lifestyle",

    # 社会热点 & 新闻
    "Ukraine conflict explained", "US presidential election", "global warming facts",
    "climate change solutions", "latest tech news", "AI replacing jobs", "privacy concerns with smartphones",

    # 商业 & 创业
    "how to start a business", "make money online", "passive income ideas", "top e-commerce platforms",
    "dropshipping vs Amazon FBA", "remote work trends", "freelancing vs full-time job",

    # 游戏 & 电竞
    "best PC games 2025", "Valorant tips and tricks", "how to get better at Fortnite",
    "Steam summer sale", "Nintendo Switch 2 rumors", "top esports teams",

    # 杂项 & 轻松话题
    "zodiac sign personality", "meaning of dreams", "fun trivia questions", "weird facts about space",
    "does pineapple belong on pizza", "best memes of 2025", "how to cook pasta",
    "coffee vs tea", "cats vs dogs", "funny dad jokes", "TikTok trends 2025"
]

# -----------------------------------------------

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Edge(options=options)
driver.get("https://www.bing.com")
time.sleep(5)  # 等你登录账号

success_count = 0
attempt = 0
max_attempts = MAX_SEARCH_TIMES + 10  # 给点容错

while success_count < MIN_SEARCH_TIMES and attempt < max_attempts:
    attempt += 1
    keyword = random.choice(KEYWORDS)
    print(f"[{success_count + 1}/{MIN_SEARCH_TIMES}] Searching: {keyword}")

    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.submit()
        success_count += 1
    except Exception as e:
        print(f"搜索失败（第 {attempt} 次尝试）：{e}")
        driver.get("https://www.bing.com")
        time.sleep(1)
        continue

    time.sleep(random.uniform(*WAIT_TIME))
    driver.get("https://www.bing.com")

print(f"\n成功搜索 {success_count} 次，关闭浏览器。")
driver.quit()
