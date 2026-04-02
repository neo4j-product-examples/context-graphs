az containerapp up \
  --name resume-mcp \
  --resource-group your-rg \
  --location uksouth \
  --ingress external \
  --target-port 3000 \
  --source . \
  --env-vars \
    AZURE_ENDPOINT="https://your-service.search.windows.net" \
    AZURE_INDEX="your-index-name" \
    AZURE_KEY="your-query-key"