"""Research reader checks reuse installed Node/Playwright; no package installation.

The integration test is explicitly opt-in because it needs the running local
research Docker project. It only reads stored evidence through authenticated API.
"""
import os
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('node'), 'Node.js required')
class ResearchDisplayTests(unittest.TestCase):
    def test_reader_logic(self):
        subprocess.run(['node', '--test', 'tests/research-logic.test.cjs'], cwd=ROOT, check=True)

    @unittest.skipUnless(os.getenv('JESSE_RESEARCH_UI_TEST'), 'Set JESSE_RESEARCH_UI_TEST for local integration')
    def test_local_dashboard(self):
        subprocess.run(['node', 'tests/research-browser.cjs'], cwd=ROOT, check=True, timeout=120)
