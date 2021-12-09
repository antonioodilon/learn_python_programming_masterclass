required_skills = ["React", "Design", "Vue.js"]

candidate = {
    "Christopher": {"javascript", "Java", "fullstack", "Python", "linux"},
    "Anthony": {"mongoDB", "Python", "React", "windows"},
    "Rafaela": {"Design", "javascript", "React", "Vue.js", "CSS"},
    "Mary": {"Vue.js", "Java", "React", "windows", "linux", "Design"},
    "Jonathan": {"windows", "Design", "Vue.js", "Python"},
    "Caroline": {"linux", "javascript", "React", "Vue.js", "Design", "CSS"},
    "Jane": {"Vue.js", "Design", "React"},
}

interviewees = set()

# Code that I wrote:
for candidate, skills in candidate.items():
    if set(required_skills).issubset(skills):
        interviewees.add(candidate)

print(interviewees)

# Code that Tim Buchalka wrote:
# for candidate, skills in candidate.items():
#     if skills.issuperset(required_skills):
#         interviewees.add(candidate)

print("-"*80)

candidate2 = {
    "Christopher": {"javascript", "Java", "fullstack", "Python", "linux"},
    "Anthony": {"mongoDB", "Python", "React", "windows"},
    "Rafaela": {"Design", "javascript", "React", "Vue.js", "CSS"},
    "Mary": {"Vue.js", "Java", "React", "windows", "linux", "Design"},
    "Jonathan": {"windows", "Design", "Vue.js", "Python"},
    "Caroline": {"linux", "javascript", "React", "Vue.js", "Design", "CSS"},
    "Jane": {"Vue.js", "Design", "React"},
}

interviewees2 = set()

# Now imagine that we have to ignore some people for an interview because
# there are too many. Let's check for proper supersets and proper subsets
# instead.

# Code that I wrote:
for candidates, skills2 in candidate2.items():
    if not skills2 > set(required_skills):
        pass
    else:
        interviewees2.add(candidates)

# Code that Tim Buchalka wrote:
# for candidates, skills2 in candidate2.items():
#     if skills2 > set(required_skills):
#         interviewees2.add(candidates)

# Jane is ignored
print(interviewees2)