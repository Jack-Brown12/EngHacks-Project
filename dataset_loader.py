import kagglehub
import pandas as pd
from skill_extraction import extract_skills

# Download latest version
path = kagglehub.dataset_download("ravindrasinghrana/job-description-dataset")

print("Path to dataset files:", path)

# Load the dataset into a pandas DataFrame
df = pd.read_csv(f"{path}/job_descriptions.csv")
print("Successfully loaded dataset into DataFrame")

# Count the frequency of each skill in the dataset using extract_skills function
skill_frequency = {}
for skill in df["skills"]:
        skill_tuple = extract_skills(skill)
        for skill_confidence in skill_tuple:
            skill = skill_confidence[0]
            if skill in skill_frequency:
                skill_frequency[skill] += 1
            else:
                skill_frequency[skill] = 1
print("Successfully created skill frequency dictionary.")

# Separate skills into three categories: common, uncommon, and rare.
sorted_skills = sorted(skill_frequency.items(), key=lambda x: x[1], reverse=True)
common_skills = {}
uncommon_skills = {}
rare_skills = {}
third = len(skill_frequency) // 3

# Change frequency into percent occurrence using frequency/total frequency * 100
total_frequency = sum(skill_frequency.values())

for i, (skill, frequency) in enumerate(sorted_skills):
    if i < third:
        common_skills[skill] = frequency/total_frequency * 100
    elif i < 2 * third:
        uncommon_skills[skill] = frequency/total_frequency * 100
    else:
        rare_skills[skill] = frequency/total_frequency * 100

print("Successfully categorized skills into common, uncommon, and rare.")

# Write skills to separate text files with percent occurrence.
with open("common_skills.txt", "w") as outfile:
    for skill in common_skills:
        outfile.write(f"{skill}: {common_skills[skill]:.2f}%\n")
with open("uncommon_skills.txt", "w") as outfile:
    for skill in uncommon_skills:
        outfile.write(f"{skill}: {uncommon_skills[skill]:.2f}%\n")
with open("rare_skills.txt", "w") as outfile:
    for skill in rare_skills:
        outfile.write(f"{skill}: {rare_skills[skill]:.2f}%\n")

print("Successfully wrote skills to separate text files.")