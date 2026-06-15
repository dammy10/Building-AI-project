import json
from datetime import datetime


def priority_score(difficulty, days_left):
    """Calculate priority score based on difficulty and time remaining."""
    if days_left == 0:
        return float('inf')
    return difficulty * 2 + (1 / days_left)


def validate_input(topics, difficulty, days_left, hours):
    """Validate all input parameters."""
    # Check if lists are not empty
    if not topics or not difficulty or not days_left:
        raise ValueError("❌ Topics, difficulty, and days_left cannot be empty.")
    
    # Check if all lists have same length
    if not (len(topics) == len(difficulty) == len(days_left)):
        raise ValueError("❌ All lists must have the same length.")
    
    # Check if hours is positive
    if hours <= 0:
        raise ValueError("❌ Total hours must be greater than 0.")
    
    # Check if difficulty values are valid (1-10 range)
    for d in difficulty:
        if not isinstance(d, (int, float)) or d < 1 or d > 10:
            raise ValueError("❌ Difficulty must be a number between 1 and 10.")
    
    # Check if days_left values are valid (non-negative integers)
    for d in days_left:
        if not isinstance(d, (int, float)) or d < 0:
            raise ValueError("❌ Days left must be non-negative numbers.")
    
    # Check if topics are non-empty strings
    for topic in topics:
        if not isinstance(topic, str) or not topic.strip():
            raise ValueError("❌ All topics must be non-empty strings.")
    
    return True


def create_plan(topics, difficulty, days_left, hours):
    """Create and display study plan based on priorities."""
    try:
        validate_input(topics, difficulty, days_left, hours)
    except ValueError as e:
        print(str(e))
        return None
    
    scores = []
    
    for i in range(len(topics)):
        score = priority_score(difficulty[i], days_left[i])
        scores.append((topics[i], score, difficulty[i], days_left[i]))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    
    total = sum([s[1] for s in scores])
    
    plan = []
    print("\n📚 Study Plan:\n")
    
    for topic, score, diff, days in scores:
        time = (score / total) * hours
        priority_level = "🔴 HIGH" if time > hours/3 else "🟡 MEDIUM" if time > hours/6 else "🟢 LOW"
        output_line = f"{topic}: {round(time, 2)} hours | Difficulty: {diff}/10 | Days left: {days} {priority_level}"
        print(output_line)
        plan.append({
            "topic": topic,
            "hours": round(time, 2),
            "difficulty": diff,
            "days_left": days,
            "priority": priority_level.split()[0]
        })
    
    print(f"\n⏱️  Total study time: {hours} hours\n")
    return plan


def get_user_input():
    """Get study plan details from user interactively."""
    print("🎓 Welcome to the Study Plan Generator!\n")
    
    # Get number of topics
    while True:
        try:
            num_topics = int(input("How many subjects do you want to study? "))
            if num_topics <= 0:
                print("❌ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")
    
    topics = []
    difficulty = []
    days_left = []
    
    # Get topic details
    for i in range(num_topics):
        print(f"\n--- Subject {i + 1} ---")
        
        # Topic name
        while True:
            topic = input("Subject name: ").strip()
            if topic:
                topics.append(topic)
                break
            print("❌ Topic name cannot be empty.")
        
        # Difficulty level
        while True:
            try:
                diff = int(input("Difficulty level (1-10): "))
                if 1 <= diff <= 10:
                    difficulty.append(diff)
                    break
                print("❌ Please enter a number between 1 and 10.")
            except ValueError:
                print("❌ Please enter a valid number.")
        
        # Days left
        while True:
            try:
                days = int(input("Days until exam (0-365): "))
                if 0 <= days <= 365:
                    days_left.append(days)
                    break
                print("❌ Please enter a number between 0 and 365.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    # Total hours
    while True:
        try:
            hours = float(input("\nTotal study hours available: "))
            if hours > 0:
                break
            print("❌ Hours must be greater than 0.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    return topics, difficulty, days_left, hours


def export_to_file(plan, hours, filename=None):
    """Export study plan to a JSON file."""
    if not plan:
        print("❌ No plan to export.")
        return
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"study_plan_{timestamp}.json"
    
    export_data = {
        "created_at": datetime.now().isoformat(),
        "total_hours": hours,
        "subjects": plan
    }
    
    try:
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        print(f"✅ Study plan exported to '{filename}'")
    except IOError as e:
        print(f"❌ Error exporting file: {e}")


def export_to_csv(plan, hours, filename=None):
    """Export study plan to a CSV file."""
    if not plan:
        print("❌ No plan to export.")
        return
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"study_plan_{timestamp}.csv"
    
    try:
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Subject", "Hours", "Difficulty", "Days Left", "Priority"])
            for item in plan:
                writer.writerow([
                    item["topic"],
                    item["hours"],
                    item["difficulty"],
                    item["days_left"],
                    item["priority"]
                ])
        print(f"✅ Study plan exported to '{filename}'")
    except IOError as e:
        print(f"❌ Error exporting file: {e}")


def main():
    """Main function to run the study plan generator."""
    while True:
        print("\n" + "="*50)
        print("1. Create new study plan (Interactive)")
        print("2. Use sample data")
        print("3. Exit")
        print("="*50)
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            topics, difficulty, days_left, hours = get_user_input()
            plan = create_plan(topics, difficulty, days_left, hours)
            
            if plan:
                export_choice = input("\nExport plan? (json/csv/skip): ").strip().lower()
                if export_choice == 'json':
                    export_to_file(plan, hours)
                elif export_choice == 'csv':
                    export_to_csv(plan, hours)
        
        elif choice == '2':
            topics = ["Math", "Physics", "History", "Biology"]
            difficulty = [5, 4, 2, 3]
            days_left = [3, 5, 10, 7]
            hours = 6
            
            plan = create_plan(topics, difficulty, days_left, hours)
            
            if plan:
                export_choice = input("\nExport plan? (json/csv/skip): ").strip().lower()
                if export_choice == 'json':
                    export_to_file(plan, hours)
                elif export_choice == 'csv':
                    export_to_csv(plan, hours)
        
        elif choice == '3':
            print("\n👋 Thank you for using Study Plan Generator!")
            break
        
        else:
            print("❌ Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
