
import os
import shutil

from data import students

STUDENTS_DIRPATH = os.path.join(os.path.dirname(__file__), "submissions")
GROUPS_DIRPATH = os.path.join(os.path.dirname(__file__), "group_submissions")

dirs = os.listdir(STUDENTS_DIRPATH)
dirs = [d for d in dirs if d not in [".DS_Store", ".gitignore", "grades.csv"]]
dirs.sort()

print("---------------------")
print(f"PROCESSING {len(dirs)} DIRECTORIES:")

for dirname in dirs:
    parts = dirname.split("(")
    #student_name = parts[0]
    net_id = parts[-1].replace(")", "")
    group_id = [s["group_id"] for s in students if s["net_id"] == net_id][0]

    attachments_dirpath = os.path.join(STUDENTS_DIRPATH, dirname, "Submission attachment(s)")
    attachment_filenames = os.listdir(attachments_dirpath)
    for attachment_filename in attachment_filenames:
        attachment_filepath = os.path.join(attachments_dirpath, attachment_filename)
        print("...", group_id, net_id, attachment_filename)

        file_extension = "pdf"
        if file_extension not in attachment_filename:
                file_extension = attachment_filename.split(".")[-1]

        group_submission_filepath = os.path.join(GROUPS_DIRPATH, f"{group_id}.{file_extension}")
        shutil.copyfile(attachment_filepath, group_submission_filepath)
