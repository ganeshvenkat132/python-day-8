Multi-Dimensional Academic Intelligence System

This project is developed as part of the Code2Xplore Day-6 challenge for the course Hands-on Python (CSE205) at SRM University–AP. The aim of this program is to analyze student performance using multiple factors such as marks, attendance, and assignment scores, instead of relying on simple single-dimensional evaluation.

The system generates student data using the random module. Each student record contains student ID, marks, attendance percentage, and assignment score. In addition to these, a performance index is calculated for every student using a mathematical formula. All the records are initially stored in a list of tuples and then converted into a Pandas DataFrame for structured analysis.

The performance index is calculated using the formula:
performance_index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)

This formula works effectively because it gives higher importance to marks while also considering assignment performance. The logarithmic factor of attendance ensures that consistent attendance improves the score gradually without causing extreme changes.

The program classifies students into different categories based on their marks and attendance. Students with low marks or attendance are marked as At Risk. Students with moderate performance fall under Average, while higher-performing students are classified as Good. Students with very high marks and attendance are categorized as Top Performers. These classifications are stored using a dictionary.

Further analysis is performed using NumPy and Pandas. The program calculates mean, median, and standard deviation of marks. It also finds the correlation between marks and attendance to understand their relationship. Marks are normalized using a standard normalization formula to bring all values into a comparable range. A set is used to store unique marks.

The system also performs pattern detection. If the variation in marks is low and there are multiple top performers, the system concludes that the academic environment is stable. If many students have low attendance, the system identifies it as a critical situation. Otherwise, the performance is considered moderate.

The final output displays the complete student data in tabular form, categorized student groups, statistical summary, a tuple containing key values, and an overall system insight.

This project demonstrates the use of core Python concepts such as lists, tuples, dictionaries, sets, functions, and list comprehension, along with libraries like NumPy and Pandas. It shows how data can be processed and analyzed to extract meaningful conclusions.

