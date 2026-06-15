![Status](https://img.shields.io/badge/status-active-brightgreen)
![AI Project](https://img.shields.io/badge/AI-Study%20Planner-blue)


# StudyBuddy AI – Personal Study Planner
<img src="https://images.unsplash.com/photo-1456324504439-367cee3b3c32?auto=format&fit=crop&w=900&q=60" width="500">

## Summary

StudyBuddy AI is a simple AI-based study planning tool that helps students organize their study time efficiently. It creates personalized study schedules based on available time, subject difficulty, and exam dates to reduce stress and improve learning outcomes.

## Background
<img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=900&q=60" width="500">

Many students struggle with time management and do not know how to prioritize what to study. This often leads to inefficient studying and last-minute stress before exams. This problem is very common among high school and university students.

My motivation comes from personal experience as a student and observing how many learners waste time deciding what to study instead of actually studying.

This project aims to solve problems like:
- Poor study planning and time management
- Over-focusing on easy topics instead of difficult ones
- Stress caused by unstructured exam preparation
- Lack of personalized study guidance

## How is it used?
<img src="https://images.unsplash.com/photo-1506784365847-bbad939e9335?auto=format&fit=crop&w=900&q=60" width="500">

The user inputs basic information such as:
- Available study hours per day
- List of subjects or topics
- Difficulty level (self-rated or based on past performance)
- Upcoming exam dates

The AI then generates a structured daily or weekly study plan, prioritizing more difficult subjects and urgent deadlines.

This solution can be used:
- At home while planning daily study sessions
- During exam preparation periods
- By high school and university students

It can be implemented as a mobile app or simple web application.

Example of scheduling logic:

def priority_score(difficulty, days_left):
    return difficulty * 2 + (1 / days_left)

Example subjects
topics = ["Math", "Physics", "History"]
difficulty = [5, 4, 2]      # 1 = easy, 5 = hard
days_left = [3, 7, 10]      # exam urgency

Calculate priority for each subject
for i in range(len(topics)):
    score = priority_score(difficulty[i], days_left[i])
    print(topics[i], "priority:", round(score, 2))

Output:
Math priority: 10.33
Physics priority: 8.14
History priority: 4.10

## Tech Stack (Conceptual)

![Python](https://img.shields.io/badge/python-3670A3?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-orange?style=for-the-badge)
![Planning AI](https://img.shields.io/badge/AI-Recommendation%20System-purple?style=for-the-badge)

## Data sources and AI methods

The system uses user-provided data such as study time, subjects, and exam schedules. No external dataset is strictly required, but future versions could integrate academic performance data.

AI methods used include:
- Simple rule-based prioritization system
- Weighted scoring model for task ranking
- Optional machine learning regression model for predicting study difficulty or performance

Possible external tools:
- Google Calendar API for scheduling integration

## Challenges

This project does not solve deeper psychological issues such as motivation, procrastination, or learning disabilities. It also depends heavily on accurate user input.

Limitations include:
- No real understanding of student emotions or stress levels
- May oversimplify complex learning needs
- Effectiveness depends on user consistency

Ethical considerations:
- Should not pressure students into overworking
- Must avoid reinforcing unhealthy study habits

## What next?
<img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=900&q=60" width="500">

Future improvements could include:
- AI chatbot for daily motivation and reminders
- Integration with calendar apps (Google Calendar, Outlook)
- Adaptive learning system based on user performance
- Gamification features (streaks, rewards, progress tracking)

To improve the project, skills in full-stack development, machine learning, and mobile app development would be useful.

## Acknowledgments

- Inspired by personal student experience and common study challenges
- Elements of AI course materials by University of Helsinki & Reaktor
- Time management techniques such as Pomodoro method
