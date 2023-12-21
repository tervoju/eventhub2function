
# Azure function to get data from event hub service using SAS



https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=node-v3%2Cpython-v2%2Cisolated-process&pivots=programming-language-python

https://learn.microsoft.com/en-us/azure/architecture/serverless/event-hubs-functions/event-hubs-functions


## debug issue 

```
apt install python3.10-venv
```

requires also functions core tools 

https://github.com/Azure/azure-functions-core-tools#linux

## azurite

and requires also azurite (if debugging locally) to be installed and running


## local settings file  local.settings.json

if using Azure functions: create function macro it does not create a right settings file.
it has to be something like this:

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "CONNECTIONSTRING":"Endpoint=sb://<>.servicebus.windows.net/;SharedAccessKeyName=<>;SharedAccessKey=<>;EntityPath=<>"
  }
}
```

## application settings

furtermore Azure function in azure portal requires a Application Setting in the Azure Function app configuration. (said unclearly) and it needs to be same name as in local.settings.json file. also that same connection needs to be in function_app.py  

```
@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="deviotopstervo01",
                               connection="CONNECTIONSTRING") 
```
