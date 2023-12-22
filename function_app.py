import azure.functions as func
import logging
from eventhubsender import send_to_eventhub

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="deviotopstervo01",
                               connection="CONNECTIONSTRING") 
def eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                azeventhub.get_body().decode('utf-8'))
    
    # process the event
    data = azeventhub.get_body()

    # forward the event to internal eventHub
    send_to_eventhub(data)