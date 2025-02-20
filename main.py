class CurriculumVitae:
    def __init__(self, name, contact_info, objective):
        self.name = name
        self.contact_info = contact_info
        self.objective = objective
        self.education = []
        self.experience = []
        self.skills = []
        self.certifications = []
        self.publications = []

    def add_education(self, degree, school, year):
        self.education.append((degree, school, year))

    def add_experience(self, title, company, start_year, end_year, details):
        self.experience.append((title, company, start_year, end_year, details))

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_certification(self, certification):
        self.certifications.append(certification)

    def add_publication(self, publication):
        self.publications.append(publication)

    def __str__(self):
        cv = f"{self.name}\n{self.contact_info}\n\nObjective: {self.objective}\n"
        cv += "\nEducation:\n"
        for edu in self.education:
            cv += f"{edu[0]}, {edu[1]}, {edu[2]}\n"
        cv += "\nExperience:\n"
        for exp in self.experience:
            cv += f"{exp[0]}, {exp[1]} ({exp[2]} - {exp[3]})\n  {exp[4]}\n"
        cv += "\nSkills:\n" + ", ".join(self.skills) + "\n"
        cv += "\nCertifications:\n" + "\n".join(self.certifications) + "\n"
        cv += "\nPublications:\n" + "\n".join(self.publications) + "\n"
        return cv

# Creating CV for Tony Stark
tony_stark = CurriculumVitae(
    "Tony Stark",
    "Email: tony.stark@proton.me | Phone: +1234567890",
    "Innovative and driven technology leader with proven track record of pioneering advancements in the high-tech world. Seeking to leverage my expertise in technology innovation and business management to push the boundaries of science and industry."
)

# Adding Education
tony_stark.add_education("Master of Science in Electrical Engineering", "Massachusetts Institute of Technology (MIT)", "1987")

# Adding Experience
tony_stark.add_experience("CEO", "Stark Industries", 1991, 2025, "Transformed the company into a multi-national corporation pioneering in weapons manufacturing, energy, and aerospace.")
tony_stark.add_experience("Consultant", "S.H.I.E.L.D.", 2010, 2025, "Advised on and developed high-tech solutions for national security and global protection.")

# Adding Skills
skills = ["Inventor", "Business Strategy", "Robotics", "Artificial Intelligence", "Public Speaking", "Problem Solving", "Leadership"]
for skill in skills:
    tony_stark.add_skill(skill)

# Adding Certifications
certifications = [
    "Advanced Robotics - MIT",
    "AI and Machine Learning - Stanford Online"
]
for cert in certifications:
    tony_stark.add_certification(cert)

# Adding Publications
publications = [
    "Reactor Technology Advancements - Journal of Advanced Physics",
    "Future of Sustainable Energy - Global Energy Conference"
]
for pub in publications:
    tony_stark.add_publication(pub)

print(tony_stark)
