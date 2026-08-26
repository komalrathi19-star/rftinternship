import os
import re
import pandas as pd


# Common skills to search for
SKILLS = [
    "python", "java", "c", "c++", "sql", "html", "css",
    "javascript", "react", "node.js", "machine learning",
    "deep learning", "artificial intelligence", "data science",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "streamlit", "git", "github", "mongodb", "mysql",
    "power bi", "tableau", "excel"
]


def read_txt_resume(file_path):
    """Read TXT resume."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_name(text):
    """Extract candidate name."""
    patterns = [
        r"Name\s*:\s*(.+)",
        r"Name\s*-\s*(.+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return "Unknown"


def extract_skills(text):
    """Extract skills from resume."""
    text_lower = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))


def extract_experience(text):
    """Extract experience."""
    pattern = r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)"

    matches = re.findall(pattern, text, re.IGNORECASE)

    if matches:
        return max(float(x) for x in matches)

    return 0


def extract_education(text):
    """Extract education details."""
    education_keywords = [
        "b.tech", "btech", "b.e", "be",
        "m.tech", "mtech", "mca", "bca",
        "b.sc", "bsc", "m.sc", "msc",
        "mba", "phd"
    ]

    found = []

    for keyword in education_keywords:
        if keyword.lower() in text.lower():
            found.append(keyword.upper())

    return ", ".join(set(found)) if found else "Not Mentioned"


def extract_job_skills(job_description):
    """Extract skills required by job description."""
    jd_lower = job_description.lower()

    required_skills = []

    for skill in SKILLS:
        if skill.lower() in jd_lower:
            required_skills.append(skill)

    return list(set(required_skills))


def calculate_match_score(resume_skills, required_skills):
    """Calculate percentage skill match."""

    if not required_skills:
        return 0

    matched = set(resume_skills).intersection(set(required_skills))

    score = (len(matched) / len(required_skills)) * 100

    return round(score, 2)


def analyze_resume(file_path, required_skills):
    """Analyze a single resume."""

    text = read_txt_resume(file_path)

    name = extract_name(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    education = extract_education(text)

    matched_skills = list(
        set(skills).intersection(set(required_skills))
    )

    missing_skills = list(
        set(required_skills) - set(skills)
    )

    score = calculate_match_score(
        skills,
        required_skills
    )

    return {
        "Name": name,
        "Skills": ", ".join(skills),
        "Experience": experience,
        "Education": education,
        "Matched Skills": ", ".join(matched_skills),
        "Missing Skills": ", ".join(missing_skills),
        "Resume Match Score": score
    }


def process_resumes(resume_folder, job_description):

    required_skills = extract_job_skills(job_description)

    results = []

    for file_name in os.listdir(resume_folder):

        if file_name.endswith(".txt"):

            file_path = os.path.join(
                resume_folder,
                file_name
            )

            result = analyze_resume(
                file_path,
                required_skills
            )

            results.append(result)

    df = pd.DataFrame(results)

    # Rank candidates
    df = df.sort_values(
        by="Resume Match Score",
        ascending=False
    )

    df["Rank"] = range(1, len(df) + 1)

    return df


if __name__ == "__main__":

    resume_folder = "resumes"

    with open(
        "job_description.txt",
        "r",
        encoding="utf-8"
    ) as file:
        job_description = file.read()

    results = process_resumes(
        resume_folder,
        job_description
    )

    print("\n===== AI RESUME SCREENING RESULTS =====\n")

    print(results.to_string(index=False))

    # Shortlist candidates
    shortlisted = results[
        results["Resume Match Score"] >= 50
    ]

    shortlisted.to_csv(
        "shortlisted_candidates.csv",
        index=False
    )

    print(
        "\nShortlisted candidates exported to "
        "shortlisted_candidate.csv")