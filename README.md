This sample runs inside of a Docker container with Python 3.7 preconfigured using [Visual Studio Remote - Containers](https://code.visualstudio.com/docs/remote/containers) to ensure the correct SDK versions and avoid version conflicts with local resources.

## Prerequisites
* Visual Studio Code
* Docker Desktop / Docker CE
* [Visual Studio Remote - Containers Add-In](https://code.visualstudio.com/docs/remote/containers)
* SendGrid account & domain configured
* SendGrid API Key with Send Email permission

## Adding SendGrid to Azure
https://docs.microsoft.com/en-us/azure/sendgrid-dotnet-how-to-send-email

### Azure Functions
https://docs.microsoft.com/en-us/azure/azure-functions/

Note: Azure Functions current supports Python 3.6, 3.7, and 3.8.  
Reference: https://pypi.org/project/azure-functions/

### SendGrid Python
https://github.com/sendgrid/sendgrid-python

## Environment Configuration
Create a `.env` file inside of the `.devcontainers` that looks like:
```
SENDGRID_API_KEY=SG.yourapikey
EMAIL_FROM=no-reply@yourdomain.com
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

Once deployed, be sure to go into the portal and under the function's Configuration menu, add the `SENDGRID_API_KEY` and `EMAIL_FROM` values.

Reference: https://docs.microsoft.com/en-us/azure/developer/javascript/tutorial/vscode-function-app-http-trigger/tutorial-vscode-serverless-node-deploy-hosting