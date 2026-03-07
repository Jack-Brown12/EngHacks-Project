from rapidfuzz import fuzz

def load_rarity_file(filename):
    skills_map = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                if ":" in line:
                    parts = line.split(":")
                    skill_name = parts[0].strip().lower()
                    
                    try:
                        freq_val = float(parts[1].replace('%', '').strip())
                        skills_map[skill_name] = freq_val
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Warning: {filename} not found.")
    return skills_map


def get_skill_frequencies_fuzzy(job_skills, master_market_data, threshold=85):
    skill_frequency_report = []
    
    for skill in job_skills:
        skill_lower = skill.lower()
        best_match_freq = None
        highest_score = 0
        
        for market_skill, frequency in master_market_data.items():
            score = fuzz.ratio(skill_lower, market_skill)
            if score > highest_score:
                highest_score = score
                best_match_freq = frequency
        
       
        final_freq = best_match_freq if highest_score >= threshold else None
            
        skill_frequency_report.append({
            "skill": skill_lower,
            "frequency": final_freq, 
            "is_unknown": final_freq is None
        })

    return skill_frequency_report

def get_final_market_analysis(job_skills, threshold=85):
   
    master_data = load_rarity_file('skills.txt')
    raw_frequencies = get_skill_frequencies_fuzzy(job_skills, master_data, threshold)
    
    analysis = {
        "core_skills": [],
        "optional_skills": [],
        "rare_skills": [],
        "unknown_skills": [] 
    }

    for item in raw_frequencies:
        skill = item["skill"]
        freq = item["frequency"]

        if freq is None:
            analysis["unknown_skills"].append(skill)
        elif freq >= 8.0:
            analysis["core_skills"].append(skill)
        elif freq >= 5.0:
            analysis["optional_skills"].append(skill)
        else:
            analysis["rare_skills"].append(skill)

    return analysis
