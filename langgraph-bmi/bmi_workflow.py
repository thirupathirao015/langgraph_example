
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. Define State
class BMIStatus(TypedDict):
    weight: float
    height: float
    bmi: float
    status: str


# 2. Define Node
def calculate_bmi(state: BMIStatus):

    print("Executing BMI Node...")

    weight = state["weight"]
    height = state["height"]

    bmi = weight / (height * height)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal Weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return {
        "bmi": round(bmi, 2),
        "status": status
    }


# 3. Create Workflow
workflow = StateGraph(BMIStatus)


# 4. Add Node
workflow.add_node("bodymass", calculate_bmi)


# 5. Connect Nodes
workflow.add_edge(START, "bodymass")
workflow.add_edge("bodymass", END)


# 6. Compile Workflow
app = workflow.compile()


# 7. Execute Workflow
input_data = {
    "weight": 80.0,
    "height": 1.75,
    "bmi": 0.0,
    "status": ""
}

result = app.invoke(input_data)


# 8. Print Result
print("\n========== BMI RESULT ==========")
print("Weight:", result["weight"], "kg")
print("Height:", result["height"], "meters")
print("BMI:", result["bmi"])
print("Status:", result["status"])
print("================================")
