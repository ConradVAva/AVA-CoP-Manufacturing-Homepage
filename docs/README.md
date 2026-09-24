# Manufacturing Community of Practice site

## HTML site entry point
The browser-ready static site now lives in this `docs/` folder, with `docs/index.html` as the main landing page. Open that file directly in a browser or publish the `docs/` directory through GitHub Pages to share the experience.

## Site structure
- `index.html` — welcome landing page with navigation across the Manufacturing Community of Practice.
- `processes.html` — end-to-end processes for manufacturers.
- `production-principles.html` — production operating models.
- `capabilities.html` — manufacturing capabilities and functional domains.
- `industries.html` — industry-specific context.
- `avanade-assets.html` — reusable manufacturing accelerators and assets.
- `isv-solutions.html` — ISV solution categories used in manufacturing transformations.
- `project-lifecycle.html` — presales through delivery guidance.
- `404.html` — fallback page for broken routes.
- `assets/` — shared CSS, JavaScript, and local SVG illustrations.

## Local preview
Because this site is plain HTML, CSS, and JavaScript, no build step is required.

1. From the repository root, start a simple server:
   ```bash
   python3 -m http.server 8000
   ```
2. Open `http://localhost:8000/docs/` in your browser.
3. Optionally run the lightweight validation script before publishing:
   ```bash
   python3 scripts/validate_docs_html.py
   ```

## GitHub Pages publishing
In the repository settings, configure GitHub Pages to publish from the `docs/` folder on the default branch. GitHub Pages will serve `docs/index.html` as the landing page automatically.

## Existing project management documentation
This repository still includes the original project management Markdown guides for reference. They remain linked below so the exercise checks continue to pass and so teams can connect manufacturing content back to delivery governance.

- [Project Management Overview](./octoacme-project-management-overview.md) — principles, roles, key artifacts, lifecycle stages, and communication cadence.
- [Project Initiation Guide](./octoacme-project-initiation.md) — validate new work, align stakeholders, define success criteria, and decide whether to move into planning.
- [Project Planning](./octoacme-project-planning.md) — break initiatives into shippable increments, estimate scope, define the backlog, and plan milestones.
- [Execution & Tracking](./octoacme-execution-and-tracking.md) — manage team rhythms, pull requests, quality checks, reporting, and blocker escalation.
- [Risk Management & Communication](./octoacme-risks-and-communication.md) — maintain the risk register, communicate status, and escalate issues through the right paths.
- [Release & Deployment Guide](./octoacme-release-and-deployment.md) — prepare for releases, deploy safely, verify outcomes, and handle rollback or incidents.
- [Retrospective & Continuous Improvement](./octoacme-retrospective-and-continuous-improvement.md) — capture learnings, track action items, and reinforce iterative improvement.
- [OctoAcme Personas](./octoacme-roles-and-personas.md) — role summaries, responsibilities, goals, and communication patterns for the delivery team.
