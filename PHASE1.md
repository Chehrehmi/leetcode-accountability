# Phase 1: MVP Validation

**Objective:** Validate daily accountability for a small Discord group (10-30 people).
**Success Metrics:** 15 users, 70% daily activity, one week continuous usage.

## Scope
- Slash commands: `/register`, `/done`, `/stats`, `/leaderboard`, `/help`.
- Schedulers: Morning goal (using APScheduler), Nightly reminder, Sunday leaderboard.
- Database: SQLite (via SQLAlchemy).
- Models: `users`, `submissions`, `streaks`.

## Out of Scope (Do NOT build yet)
- XP, Badges, Roles, Rich embeds
- Dashboards, Graphs
- LeetCode API integration
- Authentication

## Definition of Done
- Tests written for streak calculation and leaderboards.
- Bot runs locally and responds to commands.
