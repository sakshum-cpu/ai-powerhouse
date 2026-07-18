"""Example: Using the Chatbot"""
from chatbot.chatbot import Chatbot

def main():
    print("\n🤖 NEURON Chatbot Example")
    print("=" * 50)
    
    # Create chatbot
    bot = Chatbot(name="NEURON")
    
    # Example conversations
    questions = [
        "What is machine learning?",
        "Can you explain it more simply?",
        "Give me a practical example."
    ]
    
    print("\n💬 Multi-turn conversation with context memory:")
    for question in questions:
        print(f"\nYou: {question}")
        try:
            response = bot.chat(question)
            print(f"Bot: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    # Show statistics
    print("\n📊 Chat Statistics:")
    stats = bot.get_stats()
    print(f"Total messages: {stats['total_messages']}")
    print(f"User messages: {stats['user_messages']}")
    print(f"Assistant messages: {stats['assistant_messages']}")
    
    print("\n✅ Chatbot example completed!\n")

if __name__ == "__main__":
    main()
