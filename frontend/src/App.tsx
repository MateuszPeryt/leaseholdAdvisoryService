import { FormEvent, useEffect, useRef, useState } from "react";
import { submitTriage, type TriageResult } from "./api";

const scenarios = [
  { value: "service-charge", label: "I have a question about a service charge or bill" },
  { value: "repair", label: "My home needs repairs or I am worried about building safety" },
  { value: "lease-change", label: "I want to buy, sell, or extend my lease" },
  { value: "management", label: "I have a problem with my landlord, freeholder, or managing agent" },
];

function App() {
  const [scenario, setScenario] = useState("");
  const [description, setDescription] = useState("");
  const [result, setResult] = useState<TriageResult | null>(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const resultRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (result) resultRef.current?.focus();
  }, [result]);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setResult(null);
    if (!scenario && !description.trim()) {
      setError("Choose a situation or write a short description.");
      return;
    }
    setIsLoading(true);
    try {
      setResult(await submitTriage(scenario, description));
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : "Please try again.");
    } finally {
      setIsLoading(false);
    }
  }

  function startAgain() {
    setScenario("");
    setDescription("");
    setResult(null);
    setError("");
  }

  return (
    <main className="page">
      <header className="header">
        <p className="service-name">Leasehold Advisory Service</p>
        <h1>Help with a leasehold question</h1>
        <p className="lead">Tell us a little about your situation. We will suggest a useful place to start.</p>
      </header>

      <section className="notice" aria-label="Important information">
        <strong>Please do not include personal details.</strong> Do not enter names, addresses, case numbers, or payment details. This tool gives general information, not legal advice.
      </section>

      {!result ? (
        <form onSubmit={handleSubmit} noValidate aria-describedby={error ? "form-error" : undefined}>
          <fieldset>
            <legend>Which option is closest to your question?</legend>
            <p className="hint">Choose one option, or write a short description below.</p>
            <div className="choices">
              {scenarios.map((item) => (
                <label className="choice" key={item.value}>
                  <input type="radio" name="scenario" value={item.value} checked={scenario === item.value} onChange={() => setScenario(item.value)} />
                  <span>{item.label}</span>
                </label>
              ))}
            </div>
          </fieldset>

          <label className="textarea-label" htmlFor="description">Or, describe your question in your own words</label>
          <p className="hint" id="description-hint">For example: “I do not understand a bill I have received.”</p>
          <textarea id="description" value={description} onChange={(event) => setDescription(event.target.value)} maxLength={500} rows={5} aria-describedby="description-hint character-count" />
          <p className="character-count" id="character-count">{description.length} of 500 characters</p>

          {error && <p className="error" id="form-error" role="alert">{error}</p>}
          <button type="submit" disabled={isLoading}>{isLoading ? "Checking your question…" : "Find a next step"}</button>
        </form>
      ) : (
        <div className="result" ref={resultRef} tabIndex={-1} aria-labelledby="result-heading">
          <p className="eyebrow">Suggested topic</p>
          <h2 id="result-heading">{result.title}</h2>
          <p>{result.summary}</p>
          <h3>What you can do now</h3>
          <ol>{result.steps.map((step) => <li key={step}>{step}</li>)}</ol>
          <p className="notice small"><strong>Remember:</strong> this is general information for England and Wales. If you are unsure, contact the Leasehold Advisory Service for guidance.</p>
          <button type="button" onClick={startAgain}>Start again</button>
        </div>
      )}
    </main>
  );
}

export default App;

