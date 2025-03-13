import openai
import requests
import webbrowser

# Initialize OpenAI API Key
openai.api_key = "your-openai-api-key"

# AI 1: GPT-4 for Text Understanding
class ChatAI:
    def generate_text(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

# AI 2: Image Generation (DALL-E)
class ImageAI:
    def generate_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response['data'][0]['url']

# AI 3: Web Automation
class WebAI:
    def open_website(self, url):
        webbrowser.open(url)
        return f"Opening {url}..."

# AI 4: News Fetching
class NewsAI:
    def get_news(self):
        api_key = "your-newsapi-key"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        try:
            response = requests.get(url).json()
            articles = response['articles'][:3]
            news = "\n".join([f"{a['title']} - {a['source']['name']}" for a in articles])
            return f"Latest News:\n{news}"
        except:
            return "Unable to fetch news."

# Main AI Controller
class AACWS_AI:
    def __init__(self):
        self.chat_ai = ChatAI()
        self.image_ai = ImageAI()
        self.web_ai = WebAI()
        self.news_ai = NewsAI()

    def run(self):
        print("A.A.C.W.S is now active. Type 'exit' to stop.")
        while True:
            user_input = input("You: ").lower()
            if "exit" in user_input:
                print("A.A.C.W.S: Goodbye!")
                break
            elif "generate image" in user_input:
                prompt = user_input.replace("generate image", "").strip()
                print(f"A.A.C.W.S: {self.image_ai.generate_image(prompt)}")
            elif "news" in user_input:
                print(f"A.A.C.W.S: {self.news_ai.get_news()}")
            elif "open" in user_input:
                url = user_input.replace("open", "").strip()
                print(f"A.A.C.W.S: {self.web_ai.open_website(url)}")
            else:
                print(f"A.A.C.W.S: {self.chat_ai.generate_text(user_input)}")

# Run AI
if __name__ == "__main__":
    ai = AACWS_AI()
    ai.run()
