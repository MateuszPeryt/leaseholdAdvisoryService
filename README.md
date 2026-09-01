# Leasehold Advisory Service prototype

**Prepared by:** Matthew Peryt
**Date:** 1 September 2026

A small take-home prototype for helping someone with a leasehold question find
a clearer next step. It is not a legal advice service.

## What it does

The user can choose a common situation or write a short description. A React
form sends this to a Django API. The API uses small, predictable rules to choose
one of four topics:

- service charges and bills;
- repairs, maintenance, and building safety;
- buying, selling, or extending a lease; or
- problems with a landlord, freeholder, or managing agent.

The result gives a short explanation and a few general next steps. When the
description is unclear or matches more than one topic, it uses a safe “not
sure” result instead of guessing.

## Tech choices

- **Frontend:** React, TypeScript, and Vite
- **Backend:** Django with one JSON API endpoint
- **Tests:** Django's built-in test runner

The frontend talks to `POST /api/triage/`. During local development, Vite
proxies this request to Django. The matching rules are in
`backend/triage/rules.py`, separate from the API view and React components.

## Run locally

Python 3.12 is installed. The project also includes a local Node.js runtime in
`.tools/` (which is ignored by Git), because the normal Windows Node installer
was not available. Before running an npm command in PowerShell, run this from
the repository root:

```powershell
$env:Path = "$PWD\.tools\node-v24.20.0-win-x64;$env:Path"
```

Open two terminals in the repository folder.

**Terminal 1 — Django API**

```powershell
cd backend
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py runserver
```

If you are setting the project up on a different computer, create the virtual
environment first with `python -m venv .venv`, then run
`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.

**Terminal 2 — React app**

```powershell
cd frontend
npm run dev
```

On a different computer, run `npm install` before `npm run dev`.

Open the local address printed by Vite, usually `http://localhost:5173`.

Useful extra checks:

```powershell
cd frontend
npm run lint
npm run build
```

## Tests

Run the backend tests with:

```powershell
cd backend
python manage.py test
```

The tests cover scenario priority, keyword matching, unclear descriptions, empty
requests, descriptions that are too long, and making sure the API does not send
the user's description back in its response.

## Deliberately left out

- Real LAS advice content, contact details, and legal signposting.
- Accounts, authentication, a database, CMS, analytics, and saved enquiries.
- Complex natural-language matching or AI advice.
- Production deployment settings and a full GOV.UK Design System.

These choices keep the prototype small, understandable, and safe to discuss.
Real advice content would need review by LAS content and legal specialists.

## Privacy and advice boundary

The app asks users not to add names, addresses, case numbers, or payment
details. The API does not save the scenario or description and does not return
the description in its response. This is general information for England and
Wales, not legal advice or a decision about a person's case.

## Submission notes

- [Part 1 plan](PLAN.md)
- [Part 3 hardening and self-review](HARDENING_REVIEW.md)
