"""Verify GitHub Pages build and deploy status for a specific commit via public REST API.

Usage: python -X utf8 scripts/check_pages.py --sha SHA [--repo OWNER/REPO] [--attempts 12] [--interval 10]
Uses the public GitHub API without requiring gh CLI authentication.
"""

import argparse
import json
import sys
import time

from fetch_official import fetch

DEFAULT_REPO = "tifish/ModelPriceCompare"
REQUIRED_JOBS = ("build", "deploy")


def find_pages_run(runs, sha):
    for run in runs:
        if run.get("head_sha") != sha:
            continue
        name = (run.get("name") or "").lower()
        if "pages" in name:
            return run
    return None


def check_pages(sha, repo=DEFAULT_REPO, attempts=12, interval=10, fetch_fn=fetch, sleep_fn=time.sleep):
    if not sha or not all(c in "0123456789abcdefABCDEF" for c in sha) or len(sha) < 7:
        raise ValueError(f"Invalid commit SHA: {sha!r}")
    runs_url = f"https://api.github.com/repos/{repo}/actions/runs?head_sha={sha}&per_page=10"
    last_status = "not_found"
    run = None
    for attempt in range(attempts):
        body, _ = fetch_fn(runs_url)
        data = json.loads(body)
        run = find_pages_run(data.get("workflow_runs", []), sha)
        if run is not None:
            last_status = run.get("status") or "unknown"
            if last_status == "completed":
                break
        if attempt + 1 < attempts:
            sleep_fn(interval)
    if run is None:
        raise RuntimeError(f"No GitHub Pages workflow run found for {sha} after {attempts} attempts")
    if run.get("status") != "completed":
        raise RuntimeError(f"GitHub Pages run {run.get('id')} for {sha} did not complete (status={last_status})")
    if run.get("conclusion") != "success":
        raise RuntimeError(f"GitHub Pages run {run.get('id')} for {sha} concluded with {run.get('conclusion')}")
    jobs_url = run.get("jobs_url")
    if not jobs_url or not jobs_url.startswith("https://api.github.com/"):
        raise RuntimeError(f"Missing or invalid jobs_url for run {run.get('id')}")
    jobs_body, _ = fetch_fn(jobs_url)
    jobs = json.loads(jobs_body).get("jobs", [])
    by_name = {job.get("name"): job for job in jobs}
    summary = {}
    for required in REQUIRED_JOBS:
        job = by_name.get(required)
        if job is None:
            raise RuntimeError(f"Missing required Pages job {required!r} in run {run.get('id')}")
        summary[required] = {"status": job.get("status"), "conclusion": job.get("conclusion")}
        if job.get("status") != "completed" or job.get("conclusion") != "success":
            raise RuntimeError(
                f"Pages job {required!r} in run {run.get('id')} failed: "
                f"status={job.get('status')}, conclusion={job.get('conclusion')}"
            )
    return {
        "sha": sha,
        "run_id": run.get("id"),
        "name": run.get("name"),
        "status": run.get("status"),
        "conclusion": run.get("conclusion"),
        "html_url": run.get("html_url"),
        "jobs": summary,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sha", required=True)
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--attempts", type=int, default=12)
    parser.add_argument("--interval", type=float, default=10.0)
    args = parser.parse_args()
    try:
        result = check_pages(args.sha, repo=args.repo, attempts=args.attempts, interval=args.interval)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (RuntimeError, ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
