import os
import logging
from azure.identity import DefaultAzureCredential

from azure.eventhub import EventHubProducerClient, EventData

# Get credential
credential = DefaultAzureCredential()

'''
# with credential

def send_to_eventhub(message: str | bytes):
   producer = EventHubProducerClient(
        fully_qualified_namespace=os.environ["RECEIVER_EVENT_HUB_NAMESPACE_FQDN"],
        eventhub_name=os.environ["RECEIVER_EVENT_HUB_NAME"],
        credential=credential,
    )

    # Send the data to the Event Hub
    with producer_client.connect:
        event_data_batch = producer_client.create_batch()
        event_data_batch.add(EventData(message))
        producer_client.send_batch(event_data_batch)

    logging.info("Data batch sent to Receiver Event Hub.")
'''

# with connection string

def send_to_eventhub(message: str | bytes):
    # Create an Event Hub producer client
    producer_client = EventHubProducerClient.from_connection_string(conn_str=os.environ["RECEIVER_EVENT_HUB_CONNECTIONSTRING"], eventhub_name=os.environ["RECEIVER_EVENT_HUB_NAME"])
    event_data = EventData(body=message)
    producer_client.send_batch([event_data])
    producer_client.close()
    logging.info("Data batch sent to Receiver Event Hub.")
