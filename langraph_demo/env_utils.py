import os
from dotenv import load_dotenv

load_dotenv(override=True)

CLOSEAI_BASE_URL = os.getenv('DEEPSEEK_BASE_URL')
CLOSEAI_API_KEY = os.getenv('DEEPSEEK_API_KEY')

ZHIPU_API_KEY = os.getenv('ZHIPU_API_KEY')

BAILIAN_URL = os.getenv('BAILIAN_BASE_URL')
BAILIAN_API_KEY = os.getenv('BAILIAN_API_KEY')

if __name__ == "__main__":
    print("OPENAI_API_KEY from env:", os.getenv('OPENAI_API_KEY'))
