import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#  DAY 6: PANDAS DATA WRANGLING & CLEANING


def clean_and_process_data(file_path):
    print("⏳ Step 1: Reading student marks from local CSV file...")
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    print("\n--- Raw Data Snippet ---")
    print(df)

    # 1. Standardize text values (Fixing the 'Histroy' spelling mistake)
    df['Subject'] = df['Subject'].replace({'Histroy': 'History'})

    # 2. Clean missing data using fillna()
    # We will replace any missing Mark (NaN) with the overall average mark of the dataset
    overall_average = df['Marks'].mean()
    df['Marks'] = df['Marks'].fillna(overall_average)
    
    print("\n✅ Data Cleaning Complete (Spelling fixed & missing values patched).")
    return df

def generate_summary_report(df):
    print("\n--- Grouping Summary Metrics Using Pandas groupby() ---")
    # Calculate subject-wise average marks using groupby()
    subject_summary = df.groupby('Subject')['Marks'].mean().reset_index()
    
    # Rename columns for clarity
    subject_summary.columns = ['Subject', 'Average_Mark']
    print(subject_summary)
    return subject_summary



#  DAY 7: NUMPY & MATPLOTLIB VISUALIZATION


def build_analytics_dashboard(df, subject_summary):
    print("\n🚀 Transferring data pipelines to NumPy for matrix arrays...")
    
    # Convert Pandas columns into NumPy arrays for slicing operations
    marks_array = np.array(df['Marks'])
    subjects_array = np.array(subject_summary['Subject'])
    averages_array = np.array(subject_summary['Average_Mark'])

    # Show an example of NumPy Array Slicing (grabbing top 3 marks records)
    print(f"Slice Check (First 3 marks in array): {marks_array[:3]}")

    # Set up a multi-chart Matplotlib plotting layout (1 row, 3 columns)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("⚡ ScholarOps Academic Institutional Performance Dashboard", fontsize=16, fontweight='bold')

    # 📊 Chart 1: Bar Chart (Subject Averages)
    axes[0].bar(subjects_array, averages_array, color=['#3498db', '#e74c3c', '#2ecc71'], edgecolor='black')
    axes[0].set_title("Subject-Wise Averages")
    axes[0].set_ylabel("Average Marks")
    axes[0].set_ylim(0, 100)
    for i, v in enumerate(averages_array):
        axes[0].text(i, v + 2, f"{v:.1f}", ha='center', fontweight='bold')

    # 📈 Chart 2: Line Chart (Marks Distribution Trend)
    student_names = df['Name'] + " (" + df['Subject'] + ")"
    axes[1].plot(student_names, marks_array, marker='o', linestyle='-', color='#9b59b6', linewidth=2)
    axes[1].set_title("Individual Marks Distribution Trend")
    axes[1].set_xticklabels(student_names, rotation=90, fontsize=8)
    axes[1].set_ylabel("Scored Marks")
    axes[1].grid(True, linestyle='--', alpha=0.6)

    # 🥧 Chart 3: Pie Chart (Share of Total Dataset Points per Subject)
    subject_counts = df['Subject'].value_counts()
    axes[2].pie(subject_counts, labels=subject_counts.index, autopct='%1.1f%%', startangle=140, colors=['#f1c40f', '#e67e22', '#1abc9c'])
    axes[2].set_title("Dataset Subject Distribution Share")

    # Clean layout rendering and display dashboard window
    plt.tight_layout()
    print("\n🎨 Displaying active dashboard window renderer panel...")
    plt.show()


#  APPLICATION ENTRY RUNNER


def main():
    print("⚡ ScholarOps Institutional Analytics Engine Initialized")
    csv_file = "student_marks.csv"
    
    # Run Day 6 Routines
    processed_df = clean_and_process_data(csv_file)
    summary_rep = generate_summary_report(processed_df)
    
    # Run Day 7 Routines
    build_analytics_dashboard(processed_df, summary_rep)

if __name__ == "__main__":
    main()