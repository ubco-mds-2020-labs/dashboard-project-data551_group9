# Reflection
------
## What we have implemented:

At milestone4 stage, we have implemented all four graphs into our hr-marketing-analytics project. Basically it suggests the way it is in our [milestone1](https://github.com/ubco-mds-2020-labs/dashboard-project-data551_group9/releases/tag/v1.0) stage. The difference is that we split four graphs into two tabs. Audience can select the topic that they want to explore, either HR perspective or marketing perspective. 

- The first tab (HR perspective): title is given as "HR Analytics on Training". On the left hand side, there are two dropdown menus and one radio button menu. Users can select desired education levels and do comparisons by using the two dropdown menus. Users can select previous company size by using the radio button menu. These two graphs can help HR to explore the relationship between education level or previous company size, and training hours. 

- The second tab (Advertising perspective): title is given as "Advertising Analytics on Job Change". On the left hand side, there's a slider and a dropdown menu. Users can select desired city index range by using the slider. Users can select experience level by using the dropdown menu. The first graph on the right shows the relationship between city index and percentage of people who want to change their job, given their last job duration. The will help marketing department to allocate advertisement fees in cities with different development index. The second graph on the right will help marketing department to explore more in the question of which major and education level will have more people who want to switch their job. 

- We added our information and hyper links in our Dashboard. Users can now directly get into our github repo and original data set by clicking the hyper link. We have also modified several details suggested by Firas. "Graduate" might be a confusing term, so we changed it into "Undergraduate". Background color has been changed into gray, and background color for tabs has been changed into blue. Our stacked bar plot in Milestone 2 stage contains too many colors in each bar. We now reduced the number of groups into two or one.

## What we have not implemented:

We can do so much things with this data set. Since we only have two people in this group, we have limited time to implement our Dashboard. Below points are implements or improvements that we can add in the future.

- We can plot relationship between other factors. Making more comparison between the candidates who would like to change job and who would not, this is also important for us to pick up the difference of candidates feature in these groups. Measuring the qualification is important, but we also need pay more attention to the group who would like to select our position as his/her next job.

- Using an algorithm to calculate the comprehensive grader from each candidates(convert factors into a more quantifiaable level)and plot them, through which we are able to get a more direct conclusion from visual. This would be more convenient for recuitment decision maker to make decisions based on the quantification indicator.

- Maybe find a better way to handle missing values. This is hard to improve since we have no further information about the data.

- We can make predictions with some given features. For example, we can estimate a candidate's training time given some of his/her features. We can also estimate the probability that whether he/her wants to change job.