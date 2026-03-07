import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("asaniczka/software-engineer-job-postings-linkedin")

print("Path to dataset files:", path)

# Load the dataset into a pandas DataFrame
df = pd.read_csv(f"{path}/postings.csv")
print("Successfully loaded dataset into DataFrame")

# Count the frequency of each skill in the dataset
skill_frequency = {}
for skills in df["job_skills"]:
    for skill in str(skills).split(","):
        skill = skill.strip().lower()
        if skill in skill_frequency:
            skill_frequency[skill] += 1
        else:
            skill_frequency[skill] = 1
print("Successfully created skill frequency dictionary.")


# Make a list containing tuples of (skill, frequency) for each skill in the dataset that has a frequency greater than 1.
total_postings = len(df)
skills = [(skill, frequency) for skill, frequency in skill_frequency.items() if frequency > 1]

print("Successfully made skill list.")

# Write skills to a text file with percent occurrence.
with open("skills.txt", "w") as outfile:
    for skill, frequency in skills:
        outfile.write(f"{skill}: {frequency / total_postings * 100:.2f}%\n")

print("Successfully wrote skills to text file.")