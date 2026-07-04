# Notion MCP Setup for Reviewer Environment

## Purpose

This document explains how Pablo can connect Notion MCP in his own environment to publish, inspect, or update the final candidate prioritization report in Notion.

The core project can be reviewed without Notion MCP. Notion MCP is only needed if the reviewer wants an AI agent to interact directly with a Notion workspace.

## What Notion MCP Is Used For

In this project, Notion MCP can be used to:

- Create a Notion page for the candidate prioritization report.
- Update an existing Notion page.
- Publish or organize the recruiter-facing report.
- Keep the final report separate from private local input files.

It is not required for:

- Validating the repository.
- Running the local scripts.
- Inspecting the skill files.
- Reviewing the rubric, scoring rules, or report template.

## Official Notion MCP Endpoint

Use the official Notion MCP endpoint:

https://mcp.notion.com/mcp

## Reviewer Prerequisites

Before connecting Notion MCP, Pablo should have:

- Access to the GitHub repository.
- Access to his own Notion workspace.
- A supported MCP client such as Claude Code, ChatGPT, Codex, Antigravity, Cursor, VS Code, or another compatible tool.
- Permission to authorize external tools through the Notion OAuth flow.

## Claude Code Setup

If Pablo uses Claude Code, he can run this command from the terminal:

claude mcp add --transport http notion https://mcp.notion.com/mcp

Then, inside Claude Code, he should run:

/mcp

After that, he should follow the OAuth authentication flow and authorize the Notion workspace.

## Antigravity Setup

If Pablo uses Antigravity, he can connect Notion MCP as a custom MCP server.

Suggested configuration:

{
"mcpServers": {
"notion": {
"serverUrl": "https://mcp.notion.com/mcp"
}
}
}

After saving the configuration, he should complete the Notion OAuth authorization flow when prompted.

## ChatGPT Connector Setup

If Pablo uses ChatGPT with connectors, he can add the Notion MCP connector using this endpoint:

https://mcp.notion.com/mcp

Then he should complete the OAuth authorization flow for the target Notion workspace.

## Codex Setup

If Pablo uses Codex, he can add the Notion MCP server to the Codex MCP configuration.

Example configuration:

[mcp_servers.notion]
url = "https://mcp.notion.com/mcp"

Then he can authenticate with:

codex mcp login notion

After login, he should confirm that the Notion MCP server is available.

## Publishing Workflow for This Project

After connecting Notion MCP, Pablo or an agent can create a Notion page using the project report structure.

Recommended page title:

BetterWay Candidate Prioritization Skill — Submission Report

Recommended sections:

- Executive Summary.
- Project Objective.
- Skill Location.
- What the Skill Does.
- What the Skill Does Not Do.
- Evaluation Framework.
- Privacy-Safe Local Workflow.
- Local Test Result.
- Scripts Implemented.
- Repository Traceability.
- Responsible Screening Approach.
- Current Functional Status.
- Notion MCP Publishing Plan.
- Difficulties and Decisions.
- What I Learned.
- Final Conclusion.

## Suggested Agent Prompt

Use this prompt after Notion MCP is connected:

Create or update a Notion page titled "BetterWay Candidate Prioritization Skill — Submission Report".

Use the repository documentation and project files to produce a professional submission report.

Include:
- Executive summary.
- Project objective.
- Skill location.
- What the skill does.
- What the skill does not do.
- Evaluation framework.
- Privacy-safe local workflow.
- Local test result with 2 job files and 30 candidate files.
- Scripts implemented.
- Repository traceability.
- Responsible screening approach.
- Current functional status.
- Notion MCP publishing plan.
- Difficulties and decisions.
- What I learned.
- Final conclusion.

Do not publish raw candidate files, raw resumes, extracted text dumps, private PDFs, ZIP packages, or generated local outputs.

## Privacy Rules

Before publishing to Notion, verify:

- The page does not include raw candidate resumes.
- The page does not include private PDF contents.
- The page does not include extracted text dumps.
- The page does not include private ZIP package contents.
- The page only contains a recruiter-facing project report.
- The page explains that private files are ignored by Git.

## Expected Final Submission Field

After publishing the Notion page, copy the public Notion page link and paste it into:

SUBMISSION.txt

Under this field:

Published Notion report:

## Current Project Notion Report

The current submitted Notion report is:

https://erratic-vein-f62.notion.site/BetterWay-Candidate-Prioritization-Skill-Submission-Report-2c52d35ba5a847ae9f5a6655eef45487?pvs=143

## If Notion MCP Is Not Available

If Pablo cannot connect Notion MCP, the repository can still be reviewed through:

- candidate-prioritization/SKILL.md
- candidate-prioritization/references/
- candidate-prioritization/scripts/
- reports/templates/candidate-prioritization-report.md
- SUBMISSION.txt
- agent.md
- README.md

The local project validation can still be run with:

py candidate-prioritization/scripts/validate_project.py

Expected result:

Project validation passed.

## Reviewer Notes

The repository intentionally does not include private candidate PDFs, job description PDFs, extracted text outputs, generated inventories, generated workspaces, or generated reports.

Those files are local-only and protected by .gitignore.