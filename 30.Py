import colorama
from colorama import Fore, Style
from textblob  import TextBlob
colorama.init()
print(f"{Fore.CYAN} welcome to Sentiment Spy!{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}")
if not user_name:
    user_name= "Mystery Agent"

Conversation_history = [ ]
print(f"/n{Fore.CYAN}Hello, Agent {user_name}")
print(f"Type a sentence and i will analyze your sentence and show you the sentiment.")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN},{Fore.YELLOW}history{Fore.CYAN}, "
      f"or{Fore.YELLOW}exist{Fore.CYAN}to quit.{Style.RESET_ALL}\n")
while True:
    user_input = input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}").strip()
        continue 

    if user_input.lower()=="exist":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell,Agent{user_name}!")
        break
    elif user_input.lower()=="reset":
        Conversation_history()
        print(f"{Fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
        continue 

    elif user_input.lower()=="history":
        if not Conversation_history:
            print(f"{Fore.YELLOW}No Conversation yet.{Style.RESET_ALL} ")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx,(text,polority,sentiment_type) in enumerate(Conversation_history,start=1):
                if sentiment_type == "positive":
                    colour=Fore.GREEN
                    emoji="😀"
                elif sentiment_type == "Negetive":
                    colour = Fore.RED
                else:
                    colour = Fore.YELLOW
                    emoji="😭"

                print(f"{idx}. {colour}{emoji} {text}"
                      f"Polarity: {polarity:,2f}, {sentemint_type}{Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentemint_type= "Positive"
        colour = Fore.GREEN
        emoji= "☺️"
    elif polarity < -0.25:
        sentiment_type= "Negetive"
        colour = Fore.RED
        emoji="😔"
    else: 
        sentiment_type= "Neutral"
        colour= Fore.YEllOW
        emoji= "😭"
    Conversation_history.append((user_input,polority,sentiment_type))
    print(f"{colour}{emoji}{sentiment_type} sentiment detected!"
          f"polarity:{polarity:.2f}") 

   

                








                    