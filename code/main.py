import read_file as rf
import clean_text as ct
import calculate_metrics as cm

#Read resume file and return cleaned string
resume_string = rf.check_file_ext('../examples/sample_resume_cc.txt')
resume_cleaned = ct.file_prep(resume_string)
print(resume_cleaned)

#For resume length
length_chars, length_words = cm.get_length_of_resume(resume_cleaned)
length_eval = cm.resume_length_checker(length_words)
print(f'\nResume statistics\n\nYour resume is {length_words} words, which is {length_eval}.')

#For measurable metrics
count_keywords = cm.count_quantifiable_metrics(resume_cleaned)
print(f'In addition, it consists of at least {len(count_keywords)} measurable metrics, which include:\n {count_keywords}.')

#Email check
email = cm.check_email(resume_cleaned)
print(f'Email address is {email[1]} and it is a {email[0]} email.')

#LinkedIn check
linkedin = cm.check_linkedin(resume_cleaned)
print(f'The resume {linkedin} a linked profile address.')