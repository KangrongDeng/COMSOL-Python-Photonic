COMSOL-Python-Photonic

Python–COMSOL integration for automated Kagome photonic crystal simulations.

This project demonstrates how to connect Python with COMSOL Multiphysics to automate photonic crystal simulations and extract corner-state quality factors.

Features

* 🔗 Connect Python with COMSOL Multiphysics
* ⚙️ Modify COMSOL model parameters using Python
* 🚀 Automatically run electromagnetic simulations
* 📊 Export COMSOL results to CSV files
* 🔍 Extract simulation data with Python
* 📈 Automatically calculate corner-state quality factors
* 🤖 Ready for parameter optimization and reinforcement learning

Workflow

Python
   ↓
Load COMSOL Model
   ↓
Modify Parameters
   ↓
Run COMSOL Simulation
   ↓
Evaluate Corner States
   ↓
Export Results
   ↓
Read Data with Python
   ↓
Extract Quality Factor

Example: Kagome Photonic Crystal

The example uses a Kagome photonic crystal model to demonstrate the complete Python–COMSOL workflow.

Eight geometric parameters can be controlled from Python:

a1, a2, a3, a4
b1, b2, b3, b4

The parameters are passed directly to the COMSOL model:

model.param().set("a1", str(a1))
model.param().set("a2", str(a2))
model.param().set("a3", str(a3))
model.param().set("a4", str(a4))
model.param().set("b1", str(b1))
model.param().set("b2", str(b2))
model.param().set("b3", str(b3))
model.param().set("b4", str(b4))

The COMSOL study is then executed automatically:

model.study("std1").run()

Extracting Corner-State Quality Factors

Four COMSOL numerical tables are used to collect simulation results:

tbl1
tbl2
tbl3
tbl4

The exported data can then be processed with Pandas:

data = pd.read_csv(path, header=None)
values = pd.to_numeric(
    data.iloc[5:17, 1],
    errors="coerce"
)
max_value = values.max()

The maximum value from each evaluation region is extracted and averaged:

average_max = np.mean(max_values)

This allows the corner-state response to be obtained automatically without manually inspecting the COMSOL results.

Project Structure

COMSOL-Python-Photonic/
│
├── Kagome.mph
├── data_import.py
├── table1.csv
├── table2.csv
├── table3.csv
└── README.md

File	Description
Kagome.mph	COMSOL Kagome photonic crystal model
data_import.py	Python script for COMSOL automation and data extraction
table1.csv	COMSOL numerical results
table2.csv	COMSOL numerical results
table3.csv	COMSOL numerical results
README.md	Project documentation

Requirements

* Python 3.x
* COMSOL Multiphysics
* MPh
* NumPy
* Pandas

Install the Python dependencies:

pip install mph numpy pandas

Usage

1. Clone the repository

git clone https://github.com/KangrongDeng/COMSOL-Python-Photonic.git
cd COMSOL-Python-Photonic

2. Configure the COMSOL model path

Open data_import.py and change the model path:

pymodel = client.load("D:\\Kagome.mph")

to your local .mph file:

pymodel = client.load("your/path/Kagome.mph")

3. Run

python data_import.py

Python will:

1. Start COMSOL
2. Load the Kagome photonic crystal model
3. Modify the geometric parameters
4. Run the COMSOL study
5. Export numerical results
6. Read the results with Pandas
7. Extract the maximum corner-state response

From Simulation to Optimization

Once COMSOL can be controlled by Python, the same framework can be extended to automated optimization:

Parameter
    ↓
Python
    ↓
COMSOL
    ↓
Simulation
    ↓
Quality Factor
    ↓
Optimization Algorithm
    ↓
New Parameters
    ↺

Possible applications include:

* Parameter sweep
* Genetic algorithms
* Bayesian optimization
* Deep Q-Network (DQN)
* Proximal Policy Optimization (PPO)
* Other reinforcement learning methods

Why Python + COMSOL?

COMSOL provides powerful multiphysics simulation capabilities, while Python provides flexible programming, data processing, and optimization tools.

Combining them creates a programmable simulation workflow:

Design → Simulate → Extract → Analyze → Optimize

This project uses a Kagome photonic crystal as a practical example of this workflow.

Notes

* A valid COMSOL Multiphysics installation and license are required.
* The parameter names in Python must match those defined in the COMSOL model.
* The numerical table names must match the COMSOL model.
* Please modify the file paths according to your local environment.
* The .mph model may require a compatible COMSOL version.

Reference

* MPh — Pythonic scripting interface for COMSOL Multiphysics

License

This project is intended for research and educational purposes.
