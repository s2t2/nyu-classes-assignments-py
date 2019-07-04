
import os

from data import students

SUBMISSIONS_DIRPATH = os.path.join(os.path.dirname(__file__), "submissions")

student_dirs = [d for d in os.listdir(SUBMISSIONS_DIRPATH) if d not in [".DS_Store", ".gitignore", "grades.csv"]]
student_dirs.sort()

print("---------------------")
print(f"PROCESSING {len(student_dirs)} DIRECTORIES:")

groups = []

for dirname in student_dirs:
    parts = dirname.split("(")
    student_name = parts[0]
    net_id = parts[-1].replace(")","")
    group_id = [s["group_id"] for s in students if s["net_id"] == net_id][0]
    print("...", group_id, net_id)
    #breakpoint()
