export type TriageResult = {
  category: string;
  title: string;
  summary: string;
  steps: string[];
  matchedBy: string;
};

type TriageResponse = { result: TriageResult } | { error: string };

export async function submitTriage(scenario: string, description: string): Promise<TriageResult> {
  const response = await fetch("/api/triage/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ scenario, description }),
  });
  const body: TriageResponse = await response.json();
  if (!response.ok || "error" in body) {
    throw new Error("error" in body ? body.error : "We could not check your question. Please try again.");
  }
  return body.result;
}

