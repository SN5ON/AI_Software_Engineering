# Define the chatbot's name and tone
bot_name = "CryptoBuddy"
def greet():
    print(f"{bot_name}: Hey there! 👋 I'm {bot_name}, your AI-powered crypto advisor!")
    print("Let’s find a green and growing crypto for you! 💸🌱\n")
#This sets a name and prints a friendly welcome message.
# Predefined crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def get_user_query():
    return input("You: ").lower()
#This function takes user input and converts it to lowercase so we can match keywords easily
def respond_to_query(query):
    if "sustainable" in query or "eco" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"{bot_name}: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
    
    elif "trending" in query or "rising" in query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"{bot_name}: These cryptos are trending up: {', '.join(trending)} 📈")

    elif "long-term" in query or "growth" in query:
        for coin in crypto_db:
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 0.7:
                print(f"{bot_name}: {coin} is trending up and has a top-tier sustainability score! 🚀")
                return
        print(f"{bot_name}: Consider Ethereum or Cardano for balanced growth!")

    elif "energy" in query:
        efficient = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        print(f"{bot_name}: The most energy-efficient crypto(s): {', '.join(efficient)} ⚡")

    elif "recommend" in query or "which" in query:
        # Combined logic for profitability and sustainability
        for coin in crypto_db:
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high":
                print(f"{bot_name}: I’d recommend {coin} – it's rising and has strong market presence! 💼")
                return

    elif "bye" in query or "exit" in query:
        print(f"{bot_name}: See you next time! Remember: crypto is risky—always do your own research! 🔍")
        return False
    
    else:
        print(f"{bot_name}: Hmm, I didn’t get that. Try asking about trends, sustainability, or energy use.")
    
    return True
# This function handles different queries based on keywords. It uses if-else logic to recommend cryptos.
def chat():
    greet()
    chatting = True
    while chatting:
        query = get_user_query()
        chatting = respond_to_query(query)
chat()


#disclaimer
print("📢 Disclaimer: Cryptocurrency investments are risky. Always do your own research before investing! 🔍")