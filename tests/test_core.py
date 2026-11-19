"""Tests for Lazy Tool Resolver."""
import unittest
from mcp_lazy_tool_resolver.core import LazyToolResolver, ToolStub

class TestLazyToolResolver(unittest.TestCase):
    def test_resolution_and_caching(self):
        r = LazyToolResolver()
        called = []
        r.register_tool(ToolStub("t1", "desc", ["code", "python"], lambda: (called.append("t1"), {"schema": 1})[1]))
        
        resolved = r.resolve_for_intent("write python code")
        self.assertEqual(len(resolved), 1)
        self.assertEqual(len(called), 1)

        # Cache hit
        r.resolve_for_intent("python again")
        self.assertEqual(len(called), 1)
