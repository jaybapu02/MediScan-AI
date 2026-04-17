import json
from ai_simplifier3 import simplify_text  # ✅ move import to the top


def analyze_report(report_dict):
    # Load reference ranges
    with open("reference_range.json") as f:
        normal_ranges = json.load(f)

    # Convert reference keys to lowercase for easy comparison
    normal_ranges = {k.lower(): v for k, v in normal_ranges.items()}

    results = []
    for test, value in report_dict.items():
        test_lower = test.lower()
        if test_lower in normal_ranges:
            low, high = normal_ranges[test_lower]
            if value < low:
                results.append(f"{test}: {value} — Low ⚠️ (Below normal range)")
            elif value > high:
                results.append(f"{test}: {value} — High ⚠️ (Above normal range)")
            else:
                results.append(f"{test}: {value} — Normal ✅")
        else:
            results.append(f"{test}: {value} — No reference range found.")
    return results


if __name__ == "__main__":
    print("Enter your medical values like: Hemoglobin: 9.8, Glucose: 160")
    user_input = input("➡️ Enter here: ")

    # Convert input to dictionary
    report_dict = {}
    for item in user_input.split(","):
        key, val = item.split(":")
        report_dict[key.strip()] = float(val.strip())

    # Analyze
    output = analyze_report(report_dict)
    print("\n📋 Results:")
    for line in output:
        print(line)

    # ✅ Simplify text with AI (now inside the same block)
    raw_text = "\n".join(output)
    summary = simplify_text(raw_text)
    print("\n📋 Detailed AI Explanation:\n")
    print(summary)