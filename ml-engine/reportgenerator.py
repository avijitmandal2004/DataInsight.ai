import os

def generate_report():
    files = [
    "reports/data_overview.md",
    "reports/data_cleaning_summary.md",
    "reports/model_baseline_results.md"
]

    final_report = "automated_report.md"

    with open(final_report, "w") as outfile:
        outfile.write("# DataInsight.ai Automated Report\n\n")

        for file in files:
            if os.path.exists(file):
                with open(file, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n")

    print("Report generated successfully:", final_report)