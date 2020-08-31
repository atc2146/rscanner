import read_file as rf
import clean_text as ct
#from read_file import read_txt_file

resume_string = rf.check_file_ext('../examples/sample_resume_cc.txt')

resume_cleaned = ct.file_prep(resume_string)

resume_no_sw = ct.remove_stop_words(resume_cleaned)

print(resume_cleaned)

#this is a new comment to test the new branch