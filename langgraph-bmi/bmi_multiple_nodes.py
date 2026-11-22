
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# STEP 1: Define Shared State
class BMIStatus(TypedDict):
    weight: float
    height: float
    bmi: float
    status: str


# STEP 2: Node 1 - Calculate BMI
def calculate_bmi(state: BMIStatus):

    print("\nExecuting Node 1: Calculate BMI")

    weight = state["weight"]
    height = state["height"]

    bmi = weight / (height * height)

    print("Calculated BMI:", round(bmi, 2))

    # Return updated state
    return {
        "bmi": round(bmi, 2)
    }


# STEP 3: Node 2 - Check BMI Status
def check_bmi_status(state: BMIStatus):

    print("\nExecuting Node 2: Check BMI Status")

    bmi = state["bmi"]

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal Weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    print("BMI Category:", status)

    # Return updated state
    return {
        "status": status
    }


# STEP 4: Create StateGraph
workflow = StateGraph(BMIStatus)


# STEP 5: Register Nodes
workflow.add_node("calculate_bmi", calculate_bmi)
workflow.add_node("check_bmi_status", check_bmi_status)


# STEP 6: Define Workflow Connections
workflow.add_edge(START, "calculate_bmi")

workflow.add_edge("calculate_bmi", "check_bmi_status")

workflow.add_edge("check_bmi_status", END)


# STEP 7: Compile Workflow
app = workflow.compile()


# STEP 8: Provide Input
input_data = {
    "weight": 80.0,
    "height": 1.75,
    "bmi": 0.0,
    "status": ""
}


# STEP 9: Execute Workflow
result = app.invoke(input_data)


# STEP 10: Display Final Result
print("\n========== FINAL BMI RESULT ==========")
print("Weight:", result["weight"], "kg")
print("Height:", result["height"], "meters")
print("BMI:", result["bmi"])
print("Status:", result["status"])
print("======================================")
