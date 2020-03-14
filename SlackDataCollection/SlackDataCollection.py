import requests

endpoint = "https://slack.com/api/conversations.history?"
token = "xoxb-881808296276-949792822484-DgNLlsVsWaTBwvfHPu4OzqIH"
channel = "CRXQB9DRA"

url =  f"{endpoint}token={token}&channel={channel}"



user_messages = {}

cursor_query_part = ""
more_remaining = True

while(more_remaining):
    url =  f"{endpoint}token={token}&channel={channel}{cursor_query_part}"

    results = requests.get(url).json()

    for m in results["messages"][:3]:
        if 'user' in m:
            print(m["user"], m["text"])
    
    print("NEXT\n\n")
    if results["has_more"] is True:
       cursor = results["response_metadata"]["next_cursor"]
       cursor_query_part = f"&cursor={cursor}" 
    else:
        more_remaining = False

