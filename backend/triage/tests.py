import json

from django.test import Client, TestCase

from .rules import classify


class TriageRuleTests(TestCase):
    def test_selected_scenario_has_priority(self):
        result = classify("repair", "I have a service charge bill too")
        self.assertEqual(result["category"], "repairs")
        self.assertEqual(result["matchedBy"], "your selected situation")

    def test_single_keyword_group_returns_matching_category(self):
        result = classify("", "There is damp in my flat and I need a repair")
        self.assertEqual(result["category"], "repairs")

    def test_ambiguous_words_return_safe_fallback(self):
        result = classify("", "I have a bill and need to extend my lease")
        self.assertEqual(result["category"], "not_sure")


class TriageEndpointTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_empty_request_is_rejected(self):
        response = self.client.post(
            "/api/triage/", data=json.dumps({}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Choose a situation or write a short description.")

    def test_too_long_description_is_rejected(self):
        response = self.client.post(
            "/api/triage/",
            data=json.dumps({"description": "a" * 501}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Please keep your description to 500 characters or fewer.")

    def test_endpoint_does_not_echo_description(self):
        response = self.client.post(
            "/api/triage/",
            data=json.dumps({"description": "I have a service charge bill"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"]["category"], "service_charges")
        self.assertNotIn("description", response.json())
