from pypresence import Presence 
import time

start = int(time.time())
client_id = "your_clientID" 
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image="your_image", 
        large_text="your_text",
        details="your_Details ",
        state="your_State",
        start=start,
        buttons=[
            {"label": "URL_NAME1", "url": "Link1"}, 
            {"label": "URL_NAME2", "url": "link2"}
        ] 
    )
    time.sleep(60)  
