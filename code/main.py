import read_file as rf
import clean_text as ct
import calculate_metrics as cm
#from read_file import read_txt_file

resume_string = rf.check_file_ext('../examples/sample_resume_cc.txt')
resume_cleaned = ct.file_prep(resume_string)

print(resume_cleaned)

# resume_no_sw = ct.remove_stop_words(resume_cleaned)

#For resume length
length = cm.get_length_of_resume(resume_cleaned)
length_rank = cm.resume_length_checker(length[1])

print('\nResume statistics\n\nYour resume is', length[1], 'words, which is a', length_rank, 'length.')

#For measurable metrics
count_keywords = cm.count_quantifiable_metrics(resume_cleaned)

print('In addition, it consists of at least',len(count_keywords), 'measurable metrics, which include:\n',count_keywords)