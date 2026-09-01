# Part 1: Plan

## The problem

People with leasehold or park home problems can feel stressed and may not know
the legal terms for their situation. This prototype will help them explain the
problem, understand its general topic, and find a clear next step.

The first version is for leaseholders and park homeowners in England and Wales.
It should be simple to use on a phone and should not overwhelm someone with
legal information.

The prototype is useful if someone can complete it on a phone, understand the
next step in their own words, understand that it is general information, and
can get help if their problem does not match a topic.

The prototype will cover four common topics:

- service charges and bills;
- repairs, maintenance, and building safety;
- buying, selling, or extending a lease; and
- issues with a landlord, managing agent, or freeholder.

Users can choose a common situation or write a short description. The app then
shows a relevant topic, a short explanation, and suggested next steps.

## Assumptions

- The app will use simple, checked rules to match a user to a topic. It will not
  use AI to make decisions.
- A chosen scenario will be used before keywords in free text. This makes the
  result predictable and easier to explain.
- The app gives general information, not legal advice or a decision about a
  person's case.
- Users will be told not to enter names, addresses, case numbers, or financial
  details. Their text will not be saved.
- Content and contact details would need approval from LAS experts before a
  real launch.
- The app will clearly say it is for England and Wales and provide a general
  contact route when it cannot help.

## Task breakdown

1. **Set up the project**
   - Done means the app runs locally, uses TypeScript, and the README explains
     how to run it.

2. **Add content and rules**
   - Done means topics, scenario choices, messages, and matching rules are kept
     in typed data files, not mixed into the page components.

3. **Build the question page**
   - Done means a user can choose a scenario and optionally write a short
     description. Inputs have clear labels and a warning not to share personal
     information.

4. **Match the enquiry to a topic**
   - Done means a small, testable function returns a topic or a safe “we are not
     sure” result.

5. **Show next steps**
   - Done means the result gives a plain-English explanation, a few useful
     actions, a reminder of the advice limit, and a way to start again.

6. **Check accessibility and mobile use**
   - Done means the journey works with a keyboard, has clear focus and error
     messages, has good colour contrast, and works on a small screen.

7. **Test and document**
   - Done means type checks, linting, and tests pass. Important empty and
     unclear inputs are tested, and the README documents any limits.

8. **Write the review notes**
   - Done means Part 3 includes what I built, what I left out, what I tested,
     and how I used AI help.

## Risks and review checks

| Area          | Risk                                                      | What to check                                                                                   |
| ------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Advice        | Information could be wrong or sound like legal advice.    | Content is reviewed, clear about limits, and has a fallback contact route.                      |
| Accessibility | Someone may not be able to use the form.                  | Keyboard use, error messages, contrast/brightness, and mobile layout.                           |
| Personal data | Users may enter sensitive details.                        | No data is stored, sent, logged, or used.                                                       |
| Security      | Unsafe input or dependencies could create problems later. | User text is safely displayed, dependencies are kept up to date, and secrets are not committed. |
| Matching      | Keywords may give the wrong topic.                        | Scenario priority, unclear result fallback, and tests for confusing examples.                   |
| Testing       | Only testing the happy path misses problems.              | Empty, unclear, conflicting, keyboard, and small screens are tested.                            |
