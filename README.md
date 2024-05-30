# Object-Centric Process Mining with PM4Py

This repository contains a Python script that demonstrates the use of PM4Py for object-centric process mining. The script processes an Object-Centric Event Log (OCEL) and applies both object-centric and classical process mining techniques to discover Petri nets.

## Features

- **Read and Print OCEL**: Load an OCEL file and print its contents to verify correct loading and formatting.
- **Discover Object-Centric Petri Net**: Discover an object-centric Petri net from the provided OCEL.
- **Flatten OCEL**: Flatten the OCEL log for different object types ('ticket', 'agent', 'meeting').
- **Discover and View Traditional Petri Nets**: Discover and visualize traditional Petri nets for each object type.

## Prerequisites

Before running the script, ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/). Additionally, this script requires the `pm4py` library.

## Installation

Install PM4Py using pip:

```bash
pip install pm4py

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. **Running the Script**:
   - Place your OCEL file named `running_example.xmlocel` in the script's directory or modify the script to point to the location of your OCEL file.
   - Run the script:
   ```bash
   python script_name.py

The script will output the results directly to your console, and visualizations will appear in separate windows if all operations complete successfully.
