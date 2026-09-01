# Part 3: Hardening and self-review

## Improvements made

- Added a 500-character limit in the browser and API. The API rejects longer
  input even if somebody bypasses the browser limit.
- Added a safe result for unclear or equally matched descriptions. The app does
  not pretend it knows the answer when it does not.
- Added a prominent warning not to enter personal information. The description
  is not saved or sent back in the response.
- Improved keyboard and screen-reader behaviour: real radio inputs and labels,
  labelled text area, visible focus styles, error alerts, 44px buttons, and
  focus moved to the result after submission.
- Added tests for an empty request, ambiguous matching, and input that is too
  long, as well as the main matching paths.

## Personal data and security

This prototype collects a scenario and optional description only long enough to
produce a response. It has no database, user account, analytics, or contact
form, so it does not intentionally store personal data. The page warns users
not to add identifying or financial details.

In a real service, I would agree a retention period, restrict staff access by
role, document how people can request deletion, use HTTPS, and keep audit logs
that never contain enquiry text. I would also use environment variables for
secrets, set production security headers, validate and rate-limit requests, and
review dependencies regularly.

The main current risk is that a user may still type personal details. Avoiding
persistence reduces this risk, but the warning is not a complete solution. The
API is CSRF-exempt only because it has no login, cookies, or stored state. If
the endpoint ever saved anything, I would restore CSRF protection.

## Accessibility

I checked the code for semantic form controls, labels, keyboard focus, colour
contrast, error messages, screen-reader announcements, and a small-screen
layout. I added focus movement to the results so keyboard users know that the
page has changed.

I could not run a browser or a screen reader in this environment. With more
time, I would manually test with NVDA and Chrome, test at 200% zoom and narrow
screen sizes, use an automated checker such as axe, and test the wording with
people who have low confidence with legal information.

## Self code review

### Strengths

- The main flow is small and easy to follow.
- Matching rules are separate, deterministic, and covered by unit tests.
- The ambiguous fallback is safer than forcing a category.
- The app makes the advice and personal-data boundaries clear.

### Risks and work I would do before merging to production

- The example advice content has not been approved by LAS specialists; I would
  not merge it to a public service without that review.
- Keyword matching is limited and could misunderstand a real question. It needs
  research, content testing, and regular review rather than adding many rules.
- Frontend form behaviour is not covered by automated tests yet. I would add
  React tests for showing API errors, the loading state, and the result view.
- The Django settings are local-development settings, including the placeholder
  secret key and `DEBUG=True`. They are not deployable as they are.
- The UI has basic custom styles, not a full reviewed design system. A designer
  and accessibility specialist should check the finished journey.
- There is no rate limiting or monitoring. These would be needed if the endpoint
  was publicly available.

## AI usage note

I used an AI coding assistant after making the small plan and task breakdown.
It helped draft the project structure, simple rule examples, tests, and this
documentation. I kept the solution deliberately small, changed the wording to
be simpler, and rejected a complex advice engine and any use of real personal
data. I reviewed the rules, privacy boundary, accessibility choices, and every
file myself. I installed the local dependencies and verified the six Django
tests, frontend linting, and frontend production build. I did not run a manual
browser or screen-reader test in this environment.
