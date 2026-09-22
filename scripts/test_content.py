#!/usr/bin/env python3
"""Regression checks for errors that previously escaped homepage validation."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ContentRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix='wan-content-test-')
        cls.repo = Path(cls.temporary.name) / 'repo'
        shutil.copytree(ROOT, cls.repo, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def run_script(self, script, *args):
        return subprocess.run([sys.executable, 'scripts/' + script, *args],
                              cwd=self.repo, capture_output=True, text=True)

    def test_homepage_damage_is_detected_and_repairable(self):
        page = self.repo / 'README.zh-CN.md'
        original = page.read_text()
        cases = json.loads((self.repo / 'data/x-cases.json').read_text())
        case = next(c for c in cases if c['id']=='void-escape')
        changes = [
            ('missing image', case['media'][0]['thumbnail_url'], 'assets/missing-preview.jpg', 'Broken path'),
            ('broken jump', 'id="case-void-escape"', 'id="case-void-escape-BROKEN"', 'Broken explicit anchor'),
            ('wrong author', '[@0xbisc]', '[@wrong_author]', 'Stale homepage'),
            ('wrong status', '| 作者原文完整 |', '| 仅演示，未取得提示词 |', 'Stale homepage'),
            ('wrong count', f'**{len(cases)} 个 X 案例', f'**{len(cases)+1} 个 X 案例', 'Stale homepage'),
        ]
        for label, before, after, message in changes:
            with self.subTest(label=label):
                self.assertIn(before, original)
                page.write_text(original.replace(before, after, 1))
                try:
                    result = self.run_script('check_content.py')
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn(message, result.stdout)
                    self.assertNotEqual(self.run_script('build_showcase.py', '--check').returncode, 0)
                    repaired = self.run_script('build_showcase.py')
                    self.assertEqual(repaired.returncode, 0, repaired.stderr)
                    self.assertEqual(page.read_text(), original)
                finally:
                    page.write_text(original)

    def test_catalog_status_change_invalidates_both_homepages(self):
        path = self.repo / 'data/x-cases.json'
        original = path.read_text()
        cases = json.loads(original)
        cases[0]['prompt_status'] = 'partial_prompt_in_thread'
        path.write_text(json.dumps(cases, ensure_ascii=False))
        try:
            result = self.run_script('check_content.py')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Stale homepage: README.md', result.stdout)
            self.assertIn('Stale homepage: README.zh-CN.md', result.stdout)
            self.assertEqual(self.run_script('build_showcase.py').returncode, 0)
            refreshed = self.run_script('check_content.py')
            self.assertEqual(refreshed.returncode, 0, refreshed.stdout + refreshed.stderr)
        finally:
            path.write_text(original)
            self.run_script('build_showcase.py')

    def test_missing_nearby_settings_link_is_detected(self):
        page = self.repo / 'prompts/ads-and-products.md'
        original = page.read_text()
        page.write_text(original.replace('[复制前适配：目标参数并非全部可选](../guides/videoweb-workflow.zh-CN.md#adapt-settings)', '', 1))
        try:
            result = self.run_script('check_content.py')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Missing per-prompt adaptation links', result.stdout)
        finally:
            page.write_text(original)


if __name__ == '__main__':
    unittest.main()
