kor_score=[49,79,20,100,80]
math_score=[43,59,85,30,90]
eng_score=[49,79,48,60,100]

midterm_score=[kor_score,math_score,eng_score]

student_score = [0,0,0,0,0]
student_score_avg=[0,0,0,0,0]
idx=0
for key in midterm_score:
    for val in key:
        student_score[idx]+=val
        idx+=1

idx=0
# for i in student_score:
#     for val in student_score_avg:
#         int(val)=int(student_score/3)
#     else:print(student_score_avg)