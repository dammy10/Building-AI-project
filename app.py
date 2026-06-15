def priority_score(difficulty, days_left):
    if days_left == 0:
        return float('inf')
    return difficulty * 2 + (1 / days_left)


def create_plan(topics, difficulty, days_left, hours):
    scores = []

    for i in range(len(topics)):
        score = priority_score(difficulty[i], days_left[i])
        scores.append((topics[i], score))

    scores.sort(key=lambda x: x[1], reverse=True)

    total = sum([s[1] for s in scores])

    print("\n📚 Study Plan:\n")

    for topic, score in scores:
        time = (score / total) * hours
        print(f"{topic}: {round(time, 2)} hours")


topics = ["Math", "Physics", "History", "Biology"]
difficulty = [5, 4, 2, 3]
days_left = [3, 5, 10, 7]
hours = 6

create_plan(topics, difficulty, days_left, hours)
