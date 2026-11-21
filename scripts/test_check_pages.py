"""Regression checks for public GitHub Pages status verification (no live network)."""

import json
import unittest
from unittest.mock import Mock

from check_pages import check_pages

SHA = "71341547ab443f67afbb0c2bce755c7a65a1e97b"
OTHER_SHA = "7bbee1393b25d1305413f4203cc1a651a71eff76"


def make_run(sha=SHA, status="completed", conclusion="success", name="pages build and deployment"):
    return {
        "id": 1001,
        "name": name,
        "head_sha": sha,
        "status": status,
        "conclusion": conclusion,
        "jobs_url": "https://api.github.com/repos/tifish/ModelPriceCompare/actions/runs/1001/jobs",
        "html_url": "https://github.com/tifish/ModelPriceCompare/actions/runs/1001",
    }


class CheckPagesTests(unittest.TestCase):
    def test_waits_until_pages_build_and_deploy_succeed(self):
        responses = [
            (json.dumps({"workflow_runs": [make_run(status="in_progress", conclusion=None)]}), {}),
            (json.dumps({"workflow_runs": [make_run(status="completed", conclusion="success")]}), {}),
            (
                json.dumps(
                    {
                        "jobs": [
                            {"name": "build", "status": "completed", "conclusion": "success"},
                            {"name": "report-build-status", "status": "completed", "conclusion": "success"},
                            {"name": "deploy", "status": "completed", "conclusion": "success"},
                        ]
                    }
                ),
                {},
            ),
        ]
        fetch_fn = Mock(side_effect=responses)
        sleep_fn = Mock()
        result = check_pages(SHA, attempts=3, interval=5, fetch_fn=fetch_fn, sleep_fn=sleep_fn)
        self.assertEqual(result["sha"], SHA)
        self.assertEqual(result["conclusion"], "success")
        self.assertEqual(result["jobs"]["build"]["conclusion"], "success")
        self.assertEqual(result["jobs"]["deploy"]["conclusion"], "success")
        sleep_fn.assert_called_once_with(5)

    def test_ignores_mismatched_sha_and_times_out(self):
        fetch_fn = Mock(return_value=(json.dumps({"workflow_runs": [make_run(sha=OTHER_SHA)]}), {}))
        sleep_fn = Mock()
        with self.assertRaisesRegex(RuntimeError, "No GitHub Pages workflow run found"):
            check_pages(SHA, attempts=2, interval=1, fetch_fn=fetch_fn, sleep_fn=sleep_fn)
        self.assertEqual(fetch_fn.call_count, 2)
        sleep_fn.assert_called_once_with(1)

    def test_rejects_failed_deploy_job(self):
        responses = [
            (json.dumps({"workflow_runs": [make_run(status="completed", conclusion="success")]}), {}),
            (
                json.dumps(
                    {
                        "jobs": [
                            {"name": "build", "status": "completed", "conclusion": "success"},
                            {"name": "deploy", "status": "completed", "conclusion": "failure"},
                        ]
                    }
                ),
                {},
            ),
        ]
        fetch_fn = Mock(side_effect=responses)
        with self.assertRaisesRegex(RuntimeError, "deploy"):
            check_pages(SHA, attempts=1, interval=0, fetch_fn=fetch_fn, sleep_fn=Mock())

    def test_bounded_wait_when_in_progress(self):
        fetch_fn = Mock(return_value=(json.dumps({"workflow_runs": [make_run(status="in_progress", conclusion=None)]}), {}))
        sleep_fn = Mock()
        with self.assertRaisesRegex(RuntimeError, "did not complete"):
            check_pages(SHA, attempts=3, interval=2, fetch_fn=fetch_fn, sleep_fn=sleep_fn)
        self.assertEqual(fetch_fn.call_count, 3)
        self.assertEqual(sleep_fn.call_count, 2)


if __name__ == "__main__":
    unittest.main()
