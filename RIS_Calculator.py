def RIS_calculator(matched_skills, missing_skills, skill_category_lists):
    score = 0
    cumulative = 0

    common_skills = skill_category_lists["core_skills"]
    uncommon_skills = skill_category_lists["optional_skills"]
    rare_skills = skill_category_lists["optional_skills"]

    for skill in matched_skills:
        if skill in common_skills:
            score += 1
            cumulative += 1
        elif skill in uncommon_skills:
            score += 2
            cumulative += 2
        elif skill in rare_skills:
            score += 3
            cumulative += 3

    for skill in missing_skills:
        if skill in common_skills:
            score -= 3
            cumulative += 1
        elif skill in uncommon_skills:
            score -= 2
            cumulative += 2
        elif skill in rare_skills:
            score -= 1
            cumulative += 3

    eval = ((score / cumulative) + 1 ) / 2

    return eval