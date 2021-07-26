This sample runs inside of a Docker container with Python 3.7 preconfigured using [Visual Studio Remote - Containers](https://code.visualstudio.com/docs/remote/containers) to ensure the correct SDK versions and avoid version conflicts with local resources.

## Prerequisites
* Visual Studio Code
* Docker Desktop / Docker CE
* [Visual Studio Remote - Containers Add-In](https://code.visualstudio.com/docs/remote/containers)
* SendGrid account & domain configured
* SendGrid API Key with Send Email permission

## Setting Up SendGrid for Azure
https://docs.sendgrid.com/for-developers/partners/microsoft-azure-2021

## Azure Functions
https://docs.microsoft.com/en-us/azure/azure-functions/

Note: Azure Functions current supports Python 3.6, 3.7, and 3.8.  
Reference: https://pypi.org/project/azure-functions/

## SendGrid Python SDK
https://github.com/sendgrid/sendgrid-python

## Environment Configuration
Create or edit `local.settings.json` in the project root folder to look like:
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "SENDGRID_API_KEY": "SG.yourapikey",
    "EMAIL_FROM": "demo-no-reply@yourdomain.demo"
  }
}
```

## Running the Sample
From inside of the VS Code instance attached to your dev container, execute the function runtime using F5. Then open a browser to:
```
http://localhost:7071/api/HttpTrigger1?to=[email to]&subject=[email subject]
```

### Extending the Sample
https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python

## Deploying to Azure
From VS Code, open the Azure extension, select Local Project, and click the "Deploy to Function App" button in the "Functions" section header.

Once deployed, be sure to go into the portal and under the function's Configuration menu, add the `SENDGRID_API_KEY` and `EMAIL_FROM` values. Alternatively, you can use the "Azure Functions: Upload Local Settings" function from within VS Code to push the local settings to the Azure Function app.

Reference: https://docs.microsoft.com/en-us/azure/developer/javascript/tutorial/vscode-function-app-http-trigger/tutorial-vscode-serverless-node-deploy-hosting