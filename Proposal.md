### __Section 1: Motivation and Purpose__


Our role: Data scientist focus on HR consulting

Target audience: Company Marketing Department, HR & Job Seekers

Nowadays companies are paying more and more attention to hiring. A good hiring strategy can significantly help reducing the cost on training and also have a return of a more appropriate selection among the candidates. Big Data is one of the most popular method that are used for hiring. One general method is that these companies will conduct some training courses to the candidates and hiring by combining the test result with the candidates’ basic information. Many people signup for their training. In our case, our company wants to know which of these candidates has higher probability passing the test then get the data scientist position after. This will help to reduce the cost and time as well as to increase quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment. From the company decision maker perspective, they would also like to know the distribution of the candidates (relationship between features of candidates) so that they can make future predictions that may be helpful in hiring suitable employees.

### __Section 2: Description of the data__

We will be visualizing a dataset with approximately 20000 basic information from candidates who are applying for our data scientist job position. Each candidate has 14 associated features, which are candidate's gender (gender), enrollment identification (enrollee_id), the city he/she based (city), development level of city he/she based (city_development_index), education level (education_level), education major discipline of candidate (major_discipline), total experience in years (experience), number of employees in current employer's company (company_size), type of current employer (company_type), difference in years between previous job and current job (lastnewjob), and training hours completed by each candidate (training_hours). And the last feature is that whether this candidate is seeking for a job change (target: 0 stands for not looking for a job change and 1 stands for looking for a job change).

- Null value percentage: 0.077.

- Dimension of our dataset is 19158 rows and 14 columns.

- Total non-null value number is 20733.

### __Section 3: Research questions and usage scenarios__

1. From HR perspective, we would like to raise two research questions, we will raise first two questions:  
- What is the relationship between education level and training time for candidates applying for data scientist job?
- Does work experience significantly impact training time?

2. From public advertising perspective, we will raise another two questions:
- Are environmental factors like city development motivating people to seek new jobs?
- How does the distribution of major discipline look like?

Barry is an HR in a company who is in charge of training courses for new employee/job candidates. Company spends a lot of money each year on training courses. Annual KPI for Barry is to reduce the cost. However, blindly cut cost is inadvisable because the hiring quality has the same vital importance. Hence, how to precisely select the most appropriate individual among all candidates become crucial. Given the dataset of historical candidates' records, he would like to explore more deeply on candidate's features. Firstly, how to cut the cost through reducing the training time? As we know that training courses need instructors, and instructors need salary. Common sense tells us that individual with higher education level may learn knowledge faster, which means less training time for them to pass the same test. Another significant factor impacting training time is work experience. Barry is interested in finding the relationship between work experience and training time as well. New graduates will have less experience, they may or may not learn things faster since they are more likely to be younger. Thus, Barry wants to find the relationship between work experience and training time through exploring the data.

Martin is working in the marketing department of a company and in charge of doing public advertising on recruiting. Company wants to hire some new data scientists, either new graduates in educational institutions or experienced data scientists. Since wide range advertising seems to be costly, Martin would like to dig up a way to narrow down target population group. For new graduates, locate the popular (success hiring) major discipline in each educational institution from historical record can help the enactment of advertising plan. For experienced employees, broadcasting the advertisement in university/high school alumni who graduated in certain majors would be helpful in saving money. First guess by Martin would be people studying in Math/Stat/Computer Science related programs tend to be more interested in signing up for training. Another part for Martin’s exploration is how to accurately select the cities which have more suitable skills for the company and are seeking new jobs. It would better to verify his assumption by exploring the dataset. If the city’s development level is not considerable, the overall financial situation for this city may not be operating under a positive financial cycle. This may motivate people to seek for new jobs. If this assumption is verified in this dataset, advertisement targeting these cities may increase the probability of successful hiring.
