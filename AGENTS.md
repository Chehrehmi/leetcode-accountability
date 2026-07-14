# Agent Instructions

## Project Vision
A lightweight accountability platform that helps small coding communities consistently practice coding through automation, gamification, and progress tracking.
Discord is just the first interface. Treat the core logic as platform-agnostic.

## Architecture
- **Commands** (`app/commands/`): Parse input, call services, send responses. No business logic.
- **Services** (`app/services/`): Core business logic. Validations, calculations.
- **Repositories** (`app/repositories/`): Database abstraction (CRUD). No logic other than querying/saving.
- **Database** (`app/models/`, `app/database/`): SQLAlchemy Models.

## Coding Standards
- Every function has one responsibility.
- No SQL inside commands.
- No Discord API inside services.
- Use `logging` instead of `print()`.

## Rules
- Avoid prematurely implementing Phase 2+ features (No XP, badges, dashboards, LeetCode APIs yet).
- Never hardcode configuration. Use `.env`.
