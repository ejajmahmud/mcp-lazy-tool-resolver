"""Core Lazy Tool Resolver."""
from typing import Dict, List, Any, Optional

class ToolStub:
    def __init__(self, name: str, description: str, keywords: List[str], full_schema_getter):
        self.name = name
        self.description = description
        self.keywords = set(k.lower() for k in keywords)
        self.full_schema_getter = full_schema_getter

class LazyToolResolver:
    def __init__(self):
        self.stubs: Dict[str, ToolStub] = {}
        self.resolved_cache: Dict[str, Dict[str, Any]] = {}

    def register_tool(self, stub: ToolStub):
        self.stubs[stub.name] = stub

    def resolve_for_intent(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        tokens = set(query.lower().split())
        scored = []
        for stub in self.stubs.values():
            overlap = len(tokens.intersection(stub.keywords))
            scored.append((overlap, stub))

        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        for _, stub in scored[:top_k]:
            if stub.name not in self.resolved_cache:
                self.resolved_cache[stub.name] = stub.full_schema_getter()
            results.append(self.resolved_cache[stub.name])
        return results
