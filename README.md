<a id="top"></a>

# 📊 ScholarOps Performance & Institutional Analytics Dashboard — Day 6 & 7 Submission

### A comprehensive data analysis pipeline and visual dashboard utilizing Pandas for text wrangling, NumPy for array slicing, and Matplotlib for multi-chart matrix rendering.

<p align="center">
  A self-contained analytics sandbox transforming raw, corrupted, and missing student datasets into structured, indexable arrays and exportable administrative spreadsheets.
  <br />
  <a href="https://drive.google.com/file/d/1rxEKAecrCMhq4s-_DC35tEhQCe6VpI7L/view?usp=sharing"><strong>Watch App Demo Video »</strong></a>
  <br />
  <br />
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_6and7">Explore Codebase</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_6and7/Issues">Report Bug</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_6and7/Issues">Request Feature</a>
</p>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#data-wrangling-pipeline-day-6">Data Wrangling Pipeline (Day 6)</a></li>
    <li><a href="#analytics--visualization-dashboard-day-7">Analytics & Visualization Dashboard (Day 7)</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage--test-input-matrix">Usage & Test Input Matrix</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    
  </ol>
</details>

---

## About The Project

This dual-day combined milestone serves as the primary practical task submission for Day 6 and Day 7 of the Python Intermediate Internship framework. It demonstrates end-to-end data engineering skills: from handling corrupted tabular text files on disk to optimizing array processing tracks and rendering institutional analytics charts.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## 🧹 Data Wrangling Pipeline (Day 6)

The data backend relies on the **Pandas** library to ingest records and sanitize structural abnormalities directly inside an internal DataFrame workspace:
* **Spelling Alignment:** Automatically matches categorical variants by scanning data arrays and replacing string typos (e.g., correcting `"Histroy"` to `"History"`).
* **Missing Value Imputation (`fillna`):** Prevents downstream statistical dropouts by replacing isolated null markers (`NaN`) dynamically with the calculated mean score of the entire data matrix.
* **Categorical Summarization (`groupby`):** Segmentally pools matching subject tokens to produce clear, structured institutional performance summaries.

---

## 📈 Analytics & Visualization Dashboard (Day 7)

Once sanitized, the datasets are transferred to high-performance math processing and visualization tracks:
* **NumPy Memory Slicing:** Transforms active data vectors into pure memory grids (`np.array`), utilizing memory slicing segments (`marks_array[:3]`) for lightning-fast top-tier performance lookups.
* **Multi-Chart Subplots Canvas:** Utilizes `plt.subplots(1, 3)` to map out three distinct evaluation layout screens side-by-side:
  1. **📊 Bar Chart:** Compares subject-wise grade point averages clearly.
  2. **📈 Line Chart:** Illustrates individual student metric distribution trends across data bounds.
  3. **🥧 Pie Chart:** Tracks the percentage share of data entries across fields.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
* [![Matplotlib](https://img.shields.io/badge/Matplotlib-📈-blue?style=for-the-badge)](https://matplotlib.org/)

---

## Getting Started

To verify the analytical calculations and interact with the dynamic chart display dashboards locally, follow these simple environment configuration steps.

### Prerequisites
* **Python 3.8 or higher** available in your local shell framework.
* Install the essential data packages mapping to your workspace environment:
  ```bash
  pip install pandas numpy matplotlib openpyxl
Local Setup Instructions
Bash
# 1. Clone your project workspace repository down from GitHub
git clone [https://github.com/github_username/unprof.git](https://github.com/github_username/unprof.git) && cd unprof

# 2. Confirm your local Git remote origin configurations
git remote -v

# 3. Boot up the data processing pipeline script
python data_dashboard.py
💻 Usage & Test Input Matrix
The dashboard processes raw transactional rows and generates completely clean console metrics alongside an exportable sheet layout:

Input Mock Dataset Layout (student_marks.csv):
Code snippet
Student_ID,Name,Subject,Marks
101,Ananya,Mathematics,95
102,Diya,Mathematics,NaN
103,Esha,Mathematics,88
104,Kshiraja,Mathematics,92
101,Ananya,Physics,89
102,Diya,Physics,74
103,Esha,Physics,NaN
104,Kshiraja,Physics,96
101,Ananya,History,91
102,Diya,History,82
103,Esha,Histroy,78
104,Kshiraja,History,85
Processed Console Summary Grid Output:
Plaintext
⏳ Step 1: Reading student marks from local CSV file...
✅ Data Cleaning Complete (Spelling fixed & missing values patched).

--- Grouping Summary Metrics Using Pandas groupby() ---
       Subject  Average_Mark
0      History        84.000
1  Mathematics        90.525
2      Physics        86.400

🚀 Transferring data pipelines to NumPy for matrix arrays...
Slice Check (First 3 marks in array): [95.   87.1  88.  ]

🎨 Displaying active dashboard window renderer panel...
Code Implementation Showcase: Multi-Chart Plot Configuration
Python
# Configure a side-by-side subplots grid canvas matrix
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("⚡ ScholarOps Academic Institutional Performance Dashboard", fontsize=16, fontweight='bold')

# Construct the standard Bar chart performance map on sub-grid 0
axes[0].bar(subjects_array, averages_array, color=['#3498db', '#e74c3c', '#2ecc71'], edgecolor='black')
axes[0].set_title("Subject-Wise Averages")
axes[0].set_ylim(0, 100)

plt.tight_layout()
plt.show()
🎯 Roadmap
[x] Phase 1 Day 4: Integrate external API request pipelines (requests.get).

[x] Phase 1 Day 5: Implement Regular Expression parsing utilities (re.findall).

[x] Phase 1 Day 6: Engineer Pandas DataFrame cleaning pipelines and automated Excel exporters.

[x] Phase 1 Day 7: Design interactive NumPy + Matplotlib visualization dashboards.

[ ] Phase 2: Integrate multi-source database connections (SQL and PostgreSQL integration channels).

🤝 Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any improvements you bring to optimizing this operational system workspace are highly valued.

If you have a structural suggestion that would make this model better, please fork the repository workspace and open a clean pull request. You can also simply open an issue ticket flagged with the "enhancement" metadata tag.

Fork the Project Workspace

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your configuration updates safely (git commit -m 'Add some AmazingFeature')

Push code updates directly to your tracking origin (git push origin feature/AmazingFeature)

Open a professional Pull Request
