# LangGraph BMI Calculator – Python

A beginner-friendly project demonstrating the fundamentals of **LangGraph** using a Body Mass Index (BMI) calculator.

This project demonstrates how to create a simple workflow using Python and LangGraph concepts such as State, Nodes, Edges, START, END, compile(), and invoke().

## 1. Technologies Used

- Python 3.14.10
- LangGraph 1.2.24
- pip (Python Package Manager)
- VS Code
- Windows 10/11

## 2. Project Structure

```text
langgraph-bmi/
│
├── venv/
│
├── bmi_workflow.py
│
└── README.md
```

## 3. Prerequisites

Install the following software:

- Python: https://www.python.org/downloads/windows/
- VS Code: https://code.visualstudio.com/download
- LangGraph: https://docs.langchain.com/oss/python/langgraph/overview

During Python installation, select:

`Add python.exe to PATH`

Verify Python installation:

```cmd
py --version
py -m pip --version
```

## 4. Project Setup

### Step 1: Create Project Directory

```cmd
mkdir langgraph-bmi
cd langgraph-bmi
```

### Step 2: Create Virtual Environment

```cmd
py -m venv venv
```

### Step 3: Activate Virtual Environment

```cmd
venv\Scripts\activate
```

After activation, the terminal displays:

```text
(venv) C:\...\langgraph-bmi>
```

### Step 4: Upgrade pip

```cmd
python -m pip install --upgrade pip
```

### Step 5: Install LangGraph

```cmd
python -m pip install -U langgraph
```

### Step 6: Verify LangGraph Installation

```cmd
python -m pip show langgraph
```

## 5. BMI Calculator – LangGraph Workflow

### Workflow Architecture

```text
       START
         |
         v
   Node: bodymass
         |
         v
   calculate_bmi()
         |
         v
        END
```

### LangGraph Concepts

| Concept    | Description                                |
| ---------- | ------------------------------------------ |
| State      | Stores workflow input and output           |
| Node       | Python function that performs an operation |
| add_node() | Registers a function as a node             |
| add_edge() | Connects workflow nodes                    |
| START      | Workflow entry point                       |
| END        | Workflow exit point                        |
| compile()  | Compiles the workflow                      |
| invoke()   | Executes the workflow                      |

## 6. Execution Steps

### Step 1: Create Python File

Create a file named:

`bmi_workflow.py`

### Step 2: Execute Application

Make sure the virtual environment is activated.

```cmd
python bmi_workflow.py
```

### Step 3: Expected Output

```text
BMI Result: {
    'weight': 80.0,
    'height': 1.75,
    'bmi': 26.12,
    'status': 'Overweight'
}
```

## 7. BMI Calculation Formula

BMI (Body Mass Index) is calculated using:

```text
BMI = Weight (kg) / Height (m)²
```

Example:

```text
Weight = 80 kg
Height = 1.75 m

BMI = 80 / (1.75 * 1.75)

BMI = 26.12
```

## 8. BMI Categories

| BMI Range    | Category      |
| ------------ | ------------- |
| Below 18.5   | Underweight   |
| 18.5 – 24.9  | Normal weight |
| 25 – 29.9    | Overweight    |
| 30 and above | Obese         |

Note: These are general adult BMI categories, not a medical diagnosis.

## 9. Important Commands

| Command                              | Purpose                    |
| ------------------------------------ | -------------------------- |
| `py --version`                       | Check Python version       |
| `py -m pip --version`                | Check pip version          |
| `py -m venv venv`                    | Create virtual environment |
| `venv\Scripts\activate`              | Activate environment       |
| `python -m pip install -U langgraph` | Install LangGraph          |
| `python -m pip show langgraph`       | Verify LangGraph           |
| `python -m pip list`                 | List installed packages    |
| `python bmi_workflow.py`             | Execute application        |
| `deactivate`                         | Deactivate environment     |

## 10. How to Run the Project Next Time

You do not need to reinstall Python or LangGraph every time.

Navigate to the project directory:

```cmd
cd /d C:\Users\HP\Documents\3.Python_Basics\langgraph_example\langgraph-bmi
```

Activate the existing virtual environment:

```cmd
venv\Scripts\activate
```

Execute the application:

```cmd
python bmi_workflow.py
```

## 11. Learning Roadmap

After completing this project, explore the following LangGraph concepts:

1. Single Node Workflow
2. Multiple Node Workflow
3. State Management
4. Node-to-Node Communication
5. Conditional Edges
6. State Updates
7. LLM Integration
8. Tool Calling
9. AI Agents
10. Retrieval Augmented Generation (RAG)

## 12. Official Documentation

- Python: https://docs.python.org/3/
- LangGraph: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph Quickstart: https://docs.langchain.com/oss/python/langgraph/quickstart

---

**Author:** LangGraph Learning Project

**Project:** BMI Calculator using Python and LangGraph

**Purpose:** Learning and understanding LangGraph workflow fundamentals.

### Execution commands For Output Verification

**Open PowerShell** To execute below commands to run Langgraph py file

```
PS C:\Users\HP\Documents\3.Python_Basics> cd C:\Users\HP\Documents\3.Python_Basics\langgraph_example\langgraph-bmi
PS C:\Users\HP\Documents\3.Python_Basics\langgraph_example\langgraph-bmi> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\HP\Documents\3.Python_Basics\langgraph_example\langgraph-bmi> python bmi_workflow.py
Executing BMI Node...

========== BMI RESULT ==========
Weight: 80.0 kg
Height: 1.75 meters
BMI: 26.12
Status: Overweight
================================
(venv) PS C:\Users\HP\Documents\3.Python_Basics\langgraph_example\langgraph-bmi> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\HP\Documents\3.Python_Basics\langgraph_example\langgraph-bmi> python bmi_multiple_nodes.py

Executing Node 1: Calculate BMI
Calculated BMI: 26.12

Executing Node 2: Check BMI Status
BMI Category: Overweight

========== FINAL BMI RESULT ==========
Weight: 80.0 kg
Height: 1.75 meters
BMI: 26.12
Status: Overweight
======================================
```
