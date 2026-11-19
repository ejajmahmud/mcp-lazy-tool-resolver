"""CLI for Lazy Tool Resolver."""
import argparse
from .core import LazyToolResolver, ToolStub

def main():
    parser = argparse.ArgumentParser(description="MCP Lazy Tool Resolver CLI")
    parser.add_argument("--demo", action="store_true", help="Run lazy resolver demo")
    args = parser.parse_args()

    resolver = LazyToolResolver()
    resolver.register_tool(ToolStub("sql_query", "Run SQL queries", ["sql", "database", "select"], lambda: {"name": "sql_query", "full": True}))
    resolver.register_tool(ToolStub("weather", "Get weather", ["weather", "temperature"], lambda: {"name": "weather", "full": True}))

    tools = resolver.resolve_for_intent("I need database analytics")
    print(f"Resolved tools ({len(tools)}): {[t['name'] for t in tools]}")

if __name__ == "__main__":
    main()
