import json
import csv
from datetime import datetime


def priority_score(difficulty, days_left):
    """Calculate priority score based on difficulty and time remaining."""
    if days_left == 0:
        return float('inf')
    return difficulty * 2 + (1 / days_left)


def validate_input(topics, difficulty, days_left, hours):
    """Validate all input parameters."""

    if not topics or not difficulty or not days_left:
        raise ValueError("Topics, difficulty, and days_left cannot be empty.")

    if not (len(topics) == len(difficulty) == len(days_left)):
        raise ValueError("All lists must have the same length.")

    if hours <= 0:
        raise ValueError("Total hours must be greater than 0.")

    return True


def create_plan(topics, difficulty, days_left, hours):
    """Create study plan."""

    validate_input(topics, difficulty, days_left, hours)

    scores = []

    for i in range(len(topics)):
        score = priority_score(difficulty[i], days_left[i])
        scores.append((topics[i], score, difficulty[i], days_left[i]))

    scores.sort(key=lambda x: x[1], reverse=True)

    total_score = sum(score for _, score, _, _ in scores)

    plan = []

    print("\n📚 Study Plan\n")

    for topic, score, diff, days in scores:
        study_hours = round((score / total_score) * hours, 2)

        print(
            f"{topic}: {study_hours} hours "
            f"(Difficulty {diff}/10, Exam in {days} days)"
        )

        plan.append({
            "topic": topic,
            "hours": study_hours,
            "difficulty": diff,
            "days_left": days
        })

    return plan


def export_to_json(plan, hours):
    filename = "sample_output.json"

    data = {
        "created_at": datetime.now().isoformat(),
        "total_hours": hours,
        "subjects": plan
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nSaved to {filename}")


def export_to_csv(plan):
    filename = "sample_output.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Subject",
            "Hours",
            "Difficulty",
            "Days Left"
        ])

        for item in plan:
            writer.writerow([
                item["topic"],
                item["hours"],
                item["difficulty"],
                item["days_left"]
            ])

    print(f"Saved to {filename}")


def prompt_list(message, item_type=str):
    raw_value = input(message).strip()
    values = [item.strip() for item in raw_value.split(",") if item.strip()]

    if item_type is int:
        return [int(item) for item in values]

    return values


def main():
    print("Enter your study details as comma-separated values.")
    topics = prompt_list("Subjects/topics: ")
    difficulty = prompt_list("Difficulty for each subject (1-10): ", int)
    days_left = prompt_list("Days left until each exam: ", int)
    hours = float(input("Total study hours available: ").strip())

    plan = create_plan(
        topics,
        difficulty,
        days_left,
        hours
    )

    export_to_json(plan, hours)
    export_to_csv(plan)


if __name__ == "__main__":
    main()