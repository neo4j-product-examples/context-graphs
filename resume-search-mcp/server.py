from mcp.server.fastmcp import FastMCP
from mcp.server.streamable_http import StreamableHTTPServerTransport
import httpx, os, json
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("resume-search", host="0.0.0.0", port=3000)

ENDPOINT = os.environ["AZURE_ENDPOINT"]
INDEX    = os.environ["AZURE_INDEX"]
KEY      = os.environ["AZURE_KEY"]

@mcp.tool()
async def search_resumes(query: str) -> str:
    """Vector search across resumes. Pass a natural language query."""
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{ENDPOINT}/indexes/{INDEX}/docs/search?api-version=2024-05-01-preview",
            headers={"Content-Type": "application/json", "api-key": KEY},
            json={"search": query, "queryType": "semantic", "top": 5},
        )
        r.raise_for_status()
        docs = r.json().get("value", [])
        return json.dumps(docs, indent=2)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")