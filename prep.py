
import os

from data import students

SUBMISSIONS_DIRPATH = os.path.join(os.path.dirname(__file__), "submissions")
dirs = os.listdir(SUBMISSIONS_DIRPATH)
dirs = [d for d in dirs if d not in [".DS_Store", ".gitignore", "grades.csv"]]
dirs.sort()

print("---------------------")
print(f"PROCESSING {len(dirs)} DIRECTORIES:")
for dirname in dirs:
    parts = dirname.split("(")
    student_name = parts[0]
    net_id = parts[-1].replace(")", "")
    group_id = [s["group_id"] for s in students if s["net_id"] == net_id][0]
    print("...", group_id, net_id)

    #breakpoint()
    attachments_dirpath = os.path.join(os.path.dirname(__file__), "submissions", dirname, "Submission attachment(s)")
    attachment_filenames = os.listdir(attachments_dirpath)
    for attachment_filename in attachment_filenames:
        print("...", "...", attachment_filename)
