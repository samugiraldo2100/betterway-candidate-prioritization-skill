# Notion MCP Publishing

Use this reference during Phase 8 of the candidate-prioritization workflow.

## Publication Preconditions

Publish the recruiter report to Notion only when:

- The user explicitly requests publication.
- The complete evaluation has passed validation.
- The recruiter report has passed human review or the user has approved publication.
- An authenticated Notion MCP connection is available.
- The destination page or workspace location can be identified safely.

## Pre-Publication Checks

1. Confirm that the report totals match the validated evaluation totals.
2. Confirm that every evaluated candidate appears exactly once in the complete candidate matrix.
3. Confirm that excluded files and remaining limitations are documented.
4. Confirm that no unsupported or unnecessary sensitive personal information is included.
5. Confirm the intended Notion destination with the user when it is not already clear.
6. Check whether a report for the same evaluation already exists to avoid accidental duplication.

## Required Notion Page Content

Create or update a Notion page containing:

1. Report context.
2. Executive summary.
3. Priority contact queue.
4. Recommended candidates for Job A.
5. Recommended candidates for Job B.
6. Candidates suitable for both jobs.
7. Candidates requiring additional review.
8. Complete candidate matrix.
9. Excluded files.
10. Methodology and limitations.
11. Human-review disclaimer.

## Publishing Rules

- Preserve the validated report structure and terminology.
- Use headings, lists, tables, and callouts when supported by the available Notion MCP tools.
- Keep the priority contact queue near the beginning of the page.
- Make blocking constraints and important uncertainties visible.
- Do not publish local file paths, credentials, access tokens, or private configuration values.
- Do not expose information that is unnecessary for recruiter decision support.
- Do not silently omit content because of page-size or tool limitations.
- If the report is too large for one operation, publish it in ordered sections and verify each section.
- Prefer updating the intended report page over creating unintended duplicate pages.
- Do not claim successful publication until the Notion operation has been confirmed.

## Post-Publication Verification

1. Verify that the page exists and is accessible through the authenticated Notion connection.
2. Confirm that all required report sections were published.
3. Confirm that tables and structured content remain readable.
4. Record the page title.
5. Record the page URL or returned Notion reference.
6. Report any formatting differences, omitted content, or tool limitations to the user.

## Connection or Authentication Failure

If the Notion MCP connection is unavailable or authentication fails:

1. Do not discard or regenerate the validated report unnecessarily.
2. Preserve the report in its completed local or conversational form.
3. Explain the connection problem clearly.
4. Provide the exact next action required to reconnect or authenticate Notion.
5. Retry publication only after the connection is available.
6. Do not report the task as published until Notion confirms success.

## Partial Publication Recovery

If publication partially succeeds:

1. Identify which sections were created successfully.
2. Identify which sections failed.
3. Avoid duplicating completed sections during the retry.
4. Complete the missing sections.
5. Recheck the entire published page before confirming success.

## Completion Criteria

This phase is complete only when:

- The validated report has been published completely.
- The Notion page has been verified.
- The page title and reference have been recorded.
- Any publishing limitations have been disclosed.
