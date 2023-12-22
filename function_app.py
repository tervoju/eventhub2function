import azure.functions as func
import logging

# specify connection string to your event hubs namespace and
# the event hub name
producer = EventHubProducerClient.from_connection_string(
    conn_str="EVENT HUBS NAMESPACE - CONNECTION STRING",
    eventhub_name="EVENT HUB NAME"
)

app = func.FunctionApp()



@app.event_hub_message_trigger(arg_name="customer_eventhub", event_hub_name="deviotopstervo01",
                               connection="CONNECTIONSTRING") 
def eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                customer_eventhub.get_body().decode('utf-8'))
    # process the event

    # forward the event to internal eventHub
    azeventhub.
