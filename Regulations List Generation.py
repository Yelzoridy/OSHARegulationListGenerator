osha_regulations = {
    "general_industry": [
        "29 CFR 1910 Subpart D - Walking-Working Surfaces (Ensure floors are free of hazards, spills, and obstructions)",
        "29 CFR 1910 Subpart E - Exit Routes and Emergency Planning (Check for clear, unobstructed exit routes and emergency signage)",
        "29 CFR 1910 Subpart G - Occupational Health and Environmental Control (Ventilation and air quality assessments)",
        "29 CFR 1910 Subpart I - Personal Protective Equipment (PPE) (Inspect PPE for proper condition and usage, such as gloves, respirators)",
        "29 CFR 1910 Subpart S - Electrical Safety (Regular inspections of electrical wiring, lockout/tagout procedures)"
    ],
    "data_center": [
        "29 CFR 1910 Subpart S - Electrical Safety and Arc Flash Protection (Check for safe electrical installations, proper PPE, and grounding)",
        "29 CFR 1910 Subpart L - Fire Protection (Inspect fire suppression systems, fire extinguishers, and ensure clear fire exits)",
        "29 CFR 1910 Subpart I - Personal Protective Equipment (PPE for Electrical Work) (Ensure all workers handling electrical systems use proper PPE)",
        "29 CFR 1910 Subpart G - Ventilation and Noise Exposure (Check HVAC systems for adequate cooling and noise levels in data center areas)",
        "29 CFR 1910.146 - Confined Spaces (Identify confined spaces and implement safe entry procedures, including air monitoring)"
    ],
    "general_safety": [
        "29 CFR 1910 Subpart I - Personal Protective Equipment (PPE) (Ensure all workers are using appropriate PPE for their tasks)",
        "29 CFR 1910 Subpart D - Walking-Working Surfaces (Check for hazards like wet floors, cluttered walkways, and tripping hazards)",
        "29 CFR 1910 Subpart L - Fire Protection (Inspect fire extinguishers, alarm systems, and emergency exits)",
        "29 CFR 1910.146 - Confined Spaces (Identify, label, and ensure safe entry into confined spaces)",
        "29 CFR 1910 Subpart S - Electrical Safety (Verify compliance with lockout/tagout procedures, grounding, and electrical panel labeling)"
    ]
}

def get_osha_regulations(work_type):
    work_type = work_type.lower()
    if work_type in osha_regulations:
        print(f"OSHA Regulations and On-Site Checks for {work_type.title()}:")
        for regulation in osha_regulations[work_type]:
            print(f" - {regulation}")
    else:
        print(f"No specific OSHA regulations found for '{work_type}'.")

# User input for type of work
work_type = input("Enter the type of work (e.g. general_industry, data_center, general_safety): ").strip()

# Get the OSHA regulations for the provided work type
get_osha_regulations(work_type)
