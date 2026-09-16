import json
import re

# =====================================================================
# 1. PERCEPTOR LAYER (Sensing, Parsing & Normalizing Unstructured Data)
# =====================================================================
class Perceptor:
    """Ingests raw, unstructured events and emits clean, structured domain models."""
    
    @staticmethod
    def parse_event(raw_email: str) -> dict:
        # Regex extraction simulating NLP entity recognition
        order_match = re.search(r"ORD-\d+", raw_email)
        order_id = order_match.group(0) if order_match else None
        
        # Simple rule-based intent parsing
        intent = "refund_request" if "refund" in raw_email.lower() or "broken" in raw_email.lower() else "general"
        
        return {
            "order_id": order_id,
            "intent": intent,
            "raw_text": raw_email,
            "urgency": "HIGH" if "broken" in raw_email.lower() else "MEDIUM"
        }


# =====================================================================
# 2. PROCESS LAYER (Tools, API Execution & Deterministic Guardrails)
# =====================================================================
class DatabaseAPI:
    """Simulates internal databases and external payment APIs."""
    ORDERS_DB = {
        "ORD-9821": {"amount": 45.00, "item": "Wireless Mouse", "days_ago": 2},
        "ORD-1102": {"amount": 450.00, "item": "4K Monitor", "days_ago": 25}
    }

    @classmethod
    def get_order_details(cls, order_id: str) -> dict:
        return cls.ORDERS_DB.get(order_id, {})

    @classmethod
    def execute_stripe_refund(cls, order_id: str, amount: float) -> bool:
        print(f"[PROCESS API] 💳 Processing Stripe refund: ${amount} for {order_id}... SUCCESS")
        return True


# =====================================================================
# 3. AGENTIC LAYER (Reasoning, Planning & Multi-step Execution)
# =====================================================================
class SupportAgent:
    """The 'Brain' that receives clean data, applies policy logic, and coordinates tool calls."""
    
    POLICY_MAX_INSTANT_REFUND = 100.00
    POLICY_MAX_DAYS_ELAPSED = 14

    def handle_ticket(self, perceived_data: dict) -> str:
        order_id = perceived_data.get("order_id")
        
        if not order_id:
            return "Plan Aborted: Could not find a valid Order ID."

        # Step 1: Query internal tools
        order_info = DatabaseAPI.get_order_details(order_id)
        if not order_info:
            return f"Plan Aborted: Order {order_id} not found in DB."

        amount = order_info["amount"]
        days = order_info["days_ago"]

        # Step 2: Reason against business policies
        if perceived_data["intent"] == "refund_request":
            if amount <= self.POLICY_MAX_INSTANT_REFUND and days <= self.POLICY_MAX_DAYS_ELAPSED:
                # Step 3: Trigger process layer tool
                success = DatabaseAPI.execute_stripe_refund(order_id, amount)
                if success:
                    return f"Action Completed: Refund of ${amount} issued for {order_id}."
            else:
                return f"Escalated to Human: Order {order_id} exceeds instant refund policy boundaries."
                
        return "Plan Completed: No automated action required."


# =====================================================================
# DEMO EXECUTION
# =====================================================================
if __name__ == "__main__":
    # Raw incoming event
    unstructured_email = "Hi team, my package ORD-9821 arrived completely broken! I want a refund ASAP."
    
    print("--- 1. PERCEPTOR RUNNING ---")
    parsed_payload = Perceptor.parse_event(unstructured_email)
    print(json.dumps(parsed_payload, indent=2))
    
    print("\n--- 2. AGENTIC & PROCESS RUNNING ---")
    agent = SupportAgent()
    final_result = agent.handle_ticket(parsed_payload)
    
    print(f"\n[AGENT DECISION]: {final_result}")