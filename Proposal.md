### __Section 1: Motivation and Purpose__


Our role: Data scientist focus on HR consulting

Target audience: Company Decision Maker, HR & Job Seeker

Current companies have already paid more and more attention on hiring, a good hiring strategy can help significantly reducing the cost on training and also can have a return of a more appropriate selection among the candidates. Big Data is the most popular method that are used for hiring. One general method is that these companies will conduct some training courses to the candidates and hiring by combining the test result with the candidates’ basic information. Many people signup for their training. Companies wants to know which of these candidates have higher probability passing the test then get the job after because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment. From the company decision maker perspective, they would also like to know the distribution of the candidates(include the relationship between candidates’ factors) hence they can make the future decision that can be helpful on hiring more suitable employee

### __Section 2: Description of the data__

We will be visualizing a dataset of basic information from approximately 20000 job candidates. Each candidate has 14 associated variables that describe candidates’ gender(gender), enrollment identification(enrollee_id), the city he/she based(city), development level of city he/she based in(city_development_index). Also, it includes the candidates’ education level(education_level), education major discipline of candidate(major_discipline), total experience in years(experience), no of employees in current employer's company(company_size), type of current employer(company_type), difference in years between previous job and current job(lastnewjob) and training hours completed from each candidate(training_hours). Using this data we will also derive a new variable, which is whether this candidate is seeking job change(target: 0 with Not looking for job change and 1 with Looking for a job change)

We can also check the percentage of total missing values.

Null value percentage: 0.077 

Dimension of hr dataset is  19158 14 

Total non-nul value numer is 20733

### __Section 3: Research questions and usage scenarios___

1. From HR perspective, we would like to raise two research questions, we will raise first two questions:  
- What is the relationship between education level and training time?
- Does environmental factors like city development motivate people seeking new job?

2. From Decision Maker perspective, we will raise another two questions:
- What is the relationship between education level and work experience?
- What is the relationship between enrolled university and major discipline

Barry is a HR in a company who is in charge of the training course for new employee/job candidates and because the cost on training each year is really not a small number and the yearly KPI for him is to reduce the cost. However, blindly cut cost is inadvisable, because the hiring quality is also of vital importance. Hence, how to precisely select the most appropriate individual among all candidates become crucial. Given the dataset of some history candidates, he would like to explore two parts that relates to his job, one is how to cut the cost through reduce the training time, as we all know the training course need teacher, and the teacher means salary. Common sense tells us that individual with high education level may accept the knowledge faster, and this means less training time for them to gather a same test result. Another part for Barry’s exploration is how to accurately select the candidates who have higher probability for seeking a new job. From Barry’s experience, if the city’s development level is not considerable, that usually means the overall financial situation for this city is not under a positive cycle and people this will motivate people seek new job. If this assumption is verified in this dataset, select appropriate candidates from these cities may increase the probability of success hiring.

Martin is a VP in a company who is in charge of make decision on recruiting publicity, each year the company need hire some new graduate students in university and employee that have work experience on some specific realm. And he would like to dig up the way for attracting more fresh graduate and experienced candidates, wide range advertising seems not a cost-saving method and he aims to find more accurate group of people to make the publicity of hiring advertisement. For new graduates, locate the popular(success hiring) major discipline in each university from history record can help the enactment of advertising plan. For experienced employee, broadcasting the advertisement in university/high school alumni would be more targeted to some specific educational level group.
