from ollama import chat
from datetime import datetime
import time

messages=[
     {'role' : 'system','content':'Reply in hinglish and use emojis' f''' You are a helpful assistant.
             current date and time is:{datetime.now()}'''
            }
]
while True:
    user = input("You: ")

    if not user.strip():
        continue
    
    # ✔ User ka message save karne ke liye
    messages.append(
        {'role':'user' , 'content' : user}
    )

    if user.lower() == "clear":
        messages=[
            {
                'role':'system',
                'content':'Reply in hinglish and use emojis'
            }
        ]
        print("memory cleared")
        continue


    if user.lower() in ["exit","bye","quit"]:
        print("Goodbye 👋")
        break

        # Ye AI ko poori saved chat bhejne ke liye hai ✅
    response = chat(
        model='llama3',
        messages=messages
    )
    bot_reply = response['message']['content']

    print("Bot:",end="")
    for ch in bot_reply:
        print(ch,end="",flush=True)
        time.sleep(0.03)
    print()


    # ✔ Bot ka reply save karne ke liye
    messages.append({
        'role':'assistant',
        'content':bot_reply
    })


    