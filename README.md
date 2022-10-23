# university_admisor_procedure

#### Stage 1/7: No one is left behind!

##### Objectives

At this stage, your program should:

- [x] Take three inputs as integer numbers. They are the exam results.
- [x] Calculate the mean score of all three numbers. If the mean is a fractional number, don't discard the fractional part.
- [x] Print the resulting number.
- [x] Print the `Congratulations, you are accepted!` line.

#### Stage 2/7: Raising the bar

##### Objectives

At this stage, your program should:

- [x] Read the numbers and output the mean score, as in the previous stage.
- [x] If the mean score is equal to or greater than `60.0`, output the following message: `Congratulations, you are accepted!`
- [x] If the mean score is less than `60.0`, output the following message: `We regret to inform you that we will not be able to offer you admission.`


#### Stage 3/7: Going big

##### Objectives

At this stage, your program should:

- [x] Read the first input, an N integer representing the total number of applicants.
- [x] Read the second input, an M integer representing the number of applicants that should be accepted to the university.
- [x] Read N lines from the input. Each line contains the first name, the last name, and the applicant's GPA. These values are separated by one whitespace character. A GPA is a floating-point number with two decimals.
- [x] Output the `Successful applicants:` message.
- [x] Output M lines for applicants with the top-ranking GPAs. Each line should contain the first and the last name of the applicant separated by a whitespace character. Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on.
- [x] If two applicants have the same GPA, rank them in alphabetical order using their full names (we know it's not really fair to choose students by their names, but what choice do we have?)

#### Stage 4/7: Choose your path

##### Objectives

In this stage, your program should:

- [x] Read an **N** integer from the input. This integer represents the maximum number of students for each department.
- [x] Read the file named `applicants.txt` (this file is already included in the project's files, even though it is not visible; so you only need to download it if you want to take a closer look at it). Each line equals one applicant, their first name, last name, GPA, first priority department, second priority department, and third priority department. Columns with values are separated by whitespace characters. For example, `Laura Spungen 3.71 Physics Engineering Mathematics`.
- [x] Sort applicants according to their GPA and priorities (and names, if their GPA scores are the same). As in the previous stage, if two applicants to the same department have the same GPA, sort them by their full names in alphabetical order.
- [x] For each department, choose the **N** best candidates. Some departments are less popular than others, so there may be fewer available candidates for a department. However, their number shouldn't be more than **N**.
- [x] Print the departments in the alphabetic order (Biotech, Chemistry, Engineering, Mathematics, Physics), output the names and the GPA of enrolled applicants for each department. Separate the name and the GPA with a whitespace character. Here's an example (you may add empty lines between the departments' lists to increase the text readability):
```
department_name
applicant1 GPA1
applicant2 GPA2
applicant3 GPA3
<...>
```

#### Stage 5/7: Special knowledge

##### Objectives

At this stage, your program should:

- [x] Read an **N** integer. This integer represents the maximum number of students for each department.
- [x] Read the file named applicants.txt once again. The structure has changed a bit: instead of the GPA column, each line contains four columns with scores for particular exams: physics, chemistry, math, computer science (in this order). For example, `John Ritchie 89 45 83 75 Physics Engineering Mathematics`.
- [x] Take into account the following exam results for the departments: physics for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science for the Engineering, and chemistry (again) for the Biotech department.
- [x] Do the same steps as in the previous stage: perform three stages of admission based on the applicants' priorities. Applicants should be ranked by their exam score and, in case they have the same score, their full name in alphabetic order. There should be no more than N accepted applicants for each department. One student can only be accepted to one department.
- [x] One thing has changed — output the exam result (instead of the GPA) for each student:
```
department_name
applicant1 exam1
applicant2 exam2
applicant3 exam3
<...>
```

#### Stage 6/7: Extensive training

##### Objectives

In this stage, your program should:

- [x] Read an **N** integer from the input. This integer represents the maximum number of students for each department.
- [x] Read the file named applicants.txt once again. The file has the same structure as in the previous stage.
- [x] Consider the following exam results for departments: physics and math for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department.
- [x] As in the previous stage, the exams are listed in the following order for each applicant: physics, chemistry, math, computer science.
- [x] For the departments that need several exams, calculate the mean score and use it to rank the applicants (use floating-point numbers with at least one decimal). Otherwise, use the result for a single exam.
- [x] Keep the rest of the steps the same as in the previous stage (once again, there should be no more than N accepted applicants for each department; use the same principles for sorting).
- [x] Instead of printing the results (you may do it if you want), output the admission lists to files. Create a file for each department, name it %department_name%.txt, for example, physics.txt. Write the names of the students accepted to the department and their mean finals score to the corresponding file (one student per line).

#### Stage 7/7: Something special

##### Objectives

At this stage, your program should:

- [x] Read an **N** integer from the input. This integer represents the maximum number of students for each department.
- [x] Read the file named `applicants.txt` once again. Mind one additional column, right after the last exam's result. This column represents the special exam's score. For example, Willie McBride 76 45 79 80 100 Physics Engineering Mathematics(where 100 is the admission exam's score).
- [x] Choose the best score for a student in the ranking: either the mean score for the final exam(s) or the special exam's score. Use the same set of finals for each Department as in the previous stage. Note that you may need to compare the values several times: for example, if a student doesn't get accepted to the Department of the first priority, compare the finals mean score and the special exam's score once again (but this time, for the second priority department).
- [x] Keep the rest of the steps the same as in the previous stage. Once again, there should be no more than N accepted applicants for each department; use the same principles for sorting.
- [x] Output the names and the student's best score, either the mean finals score or the special exam's score to the files.






