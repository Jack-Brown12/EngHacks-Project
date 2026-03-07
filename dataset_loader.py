import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("ravindrasinghrana/job-description-dataset")

print("Path to dataset files:", path)

# Load the dataset into a pandas DataFrame
df = pd.read_csv(f"{path}/job_description_dataset.csv")

# Count the frequency of each skill in the dataset
skill_frequency = {}
for skills in df["skills"]:
    for skill in skills.split(","):
        skill = skill.strip()
        if skill in skill_frequency:
            skill_frequency[skill] += 1
        else:
            skill_frequency[skill] = 1

# Separate skills into three categories: common, uncommon, and rare.
common_skills = {}
uncommon_skills = {}
rare_skills = {}
third = len(skill_frequency) // 3

