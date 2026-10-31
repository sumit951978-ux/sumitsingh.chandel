# from statistics import mean
# data=[10,20,30,40,50]
# print(mean(data))

# from statistics import(mean,median, mode, variance,stdev)
# data=[10,20,30,40,50]
# print(mean,median, mode, variance,stdev(data))

# from statistics import(
#     median_low,
#     median_high

# )
# data=[10,20,30,40]
# print(median_low(data))
# print(median_high(data))

# import time
# timestamp=time.time()
# print(timestamp)

# import time
# print("start")
# time.sleep(3)
# print("end")

# import time
# for i in range(5,0,-1):
#     print(i)
#     time.sleep(1)
# print("time up!")

#satatistics
# from statistics import mode
# data=[10,20,20,30,40]
# print(mode(data))

#multimode
# from statistics import multimode
# data=[10,20,20,30,30,40]
# print(multimode(data))

#geometric
# from statistics import geometric_mean
# data=[2,8]
# print(geometric_mean(data))

#harmonic
# from statistics import harmonic_mean
# speeds=[40,60]
# print(harmonic_mean(speeds))

#weighted 
# from statistics import fmean
# marks=[80,70,90]
# weights=[0.3,0.2,0.5]
# result=fmean(
#     marks,
#     weights=weights

# )
# print(result)

#quantiles
# from statistics import quantiles
# data=[10,20,30,40,50,60,70,80,90,100]
# result=quantiles(
#     data,
#     n=4

# )
# print(result)

# variance
# from statistics import variance
# data=[10,20,30,40,50]
# print(variance(data))

#population
# from statistics import pvariance
# data=[10,20,30,40,50]
# print(pvariance(data))

#standard deviation
# from statistics import stdev
# data=[10,20,30,40,50]
# print(stdev(data))

#population standard ddeviatin
# from statistics import pstdev
# data=[10,20,30,40,50]
# print(pstdev(data))

#conariance
# from statistics import covariance
# sales=[100,200,300,400,500]
# advertising=[10,20,30,40,50]
# result=covariance(
#     sales,
#     advertising

# )
# print(result)

#correlation
# from statistics import correlation
# x=[10,20,30,40,50]
# y=[15,25,35,45,55]
# result=correlation(
#     x,
#     y

# )
# print(result)

#person correlations
# from statistics import correlation
# x=[10,20,30,40,50]
# y=[12,24,29,43,48]
# r=correlation(
#     x,
#     y
# )
# print("correlation:",r)


#speraman correlation
# from statistics import correlation
# x=[10,20,30,40,50]
# y=[15,35,25,45,55]
# result=correlation(
#     x,
#     y,
#     method="ranked"

# )
# print(result)


# linear regression
# from statistics import linear_regression
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# result=linear_regression(
#     x,
#     y

# )
# print(
#     "slope:",
#     result.slope
# )
# print("intercept:", result.intercept)

# predication
# from statistics import linear_regression
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# model=linear_regression(
#     x,
#     y

# )
# new_x=10
# predication=(
#     model.slope * new_x
#     + model.intercept

# )
# print("predication:",predication)

#type of  pata supported
# from statistics import mean
# data=[10,20,30,40]
# print(mean(data))

#tuple
# from statistics import mean
# data=[10,20,30,40,50]
# print(mean(data))

#set
# from statistics import mean
# data={10,20,30,40}
# print(mean(data))

#generator
# from statistics import mean
# data=(
#     x * 10
#     for  x in range(1,6)

# )
# print(mean(data))

#handling missing value
# from statistics import mean
# from math import nan
# data=[10,20,nan,40]
# print(mean(data))

#filtering nan value
# from math import isnan
# from statistics import mean
# data=[10,20,float("nan"),40]
# clean_data=[
#     x
#     for x in data
#     if not isnan(x)

# ]
# print(mean(clean_data))

#statistics
# from statistics import(
#     mean,
#     StatisticsError

# )
# data=[]
# try:
#     print(
#         mean(data)

#     )
# except StatisticsError:
#     print("invalid statistical data")

#exerise salution
# from statistics import mean
# data=[10,20,30,40,50]
# print("mean:",mean(data))


#student marks
# from statistics import mean
# marks=[75,82,68,91,88]
# average=mean(marks)
# print("average marks:",average)

#median
# from statistics import median
# data=[15,10,25,20,30]
# print("median:",median(data))


#mode
# from statistics import mode
# data=[10,20,20,20,30,40]
# print("mode:",mode(data))

#mulitple mode
# from statistics import multimode
# data=[10,20,20,30,30,]
# print("modes:",multimode(data))

#weighted average
# from statistics import fmean
# marks=[80,70,90]
# weights=[0.3,0.2,0.5]
# result=fmean(
#     marks,
#     weights=weights

# )
# print("weighted average:",result)


#gemetric mean
# from statistics import geometric_mean
# data=[2,8]
# print(geometric_mean(data))

#harmonic mean 
# from statistics import harmonic_mean
# data=[40,80]
# print(harmonic_mean(data))

#quartiles
# from statistics import quantiles
# data=[10,20,30,40,50,60,70,80,90,100]
# q=quantiles(data,n=4)
# print("quartiles:",q)

#simple variance
# from statistics import variance
# data=[10,20,30,40,50,]
# print("simple variance:",variance(data))

#population variance
# from statistics import pvariance
# data=[10,20,30,40,50]
# print("population variance:",pvariance(data))

#standard deviation
# from statistics import (stdev,pstdev)
# data=[10,20,30,40,50]
# print("simple sd:",stdev(data))
# print("population sd:",pstdev(data))

#sales analysis
# from statistics import (mean,median,variance,stdev)
# sales=[12000,15000,11000,22000,25000,19000]
# print("mean:",mean(sales))
# print("median:",median(sales))
# print("variance:",variance(sales))
# print("standard deviation:",stdev(sales))
 

#salary anmalysis
# from statistics import (mean,median)
# salaries=[25000,30000,28000,45000,50000,32000,38000]
# print("average salary:",mean(salaries))
# print("median salary:",median(salaries))
# print("minimun:",min(salaries))
# print("maximun:",max(salaries))

#sales advertising
# from statistics import (covariance,correlation)
# advertising=[10,20,30,40,50]
# sales=[100,180,250,330,420]
# print("covariance:",covariance(advertising,sales))
# print("correlation:",correlation(advertising,sales))

#regression
# from statistics import linear_regression
# advertising=[10,20,30,40,50]
# sales=[100,180,250,330,420]
# model=linear_regression(advertising,sales)
# print("slope:",model.slope)
# print("intercept:",model.intercept)
# new_advertising = 60
# prediction=(model.slope * new_advertising + model.intercept)
# print("predicted sales:",prediction)

#outlier detecion
# from statistics import quantiles
# data=[10,20,30,40,50,60,70,80,90,100]
# q1,q2,q3=quantiles(data,n=4)
# iqr=q3-q1
# lower_limit=(q1-1.5*iqr)
# upper_limit=(q3 + 1.5 * iqr)
# print("q1:",q1)
# print("q3:",q3)
# print("iqr:",iqr)
# print("lower limit:",lower_limit)
# print("upper limit:",upper_limit) 
# outliers=[
#     x
#     for x in data
#     if x < lower_limit
#     or x > upper_limit

# ]
# print("outliers:",outliers)

#student  performance
# from statistics import (mean,median,mode,stdev)
# marks=[75,80,85,80,90,75,80,95]
# print("average:",mean(marks))
# print("median:",median(marks))
# print("mode:",mode(marks))
# print("standard deviation:",stdev(marks))

#business kpl analysis
# from statistics import(mean ,median, stdev )
# revenue=[120000,135000,128000,145000,152000,160000]
# print("average revenue:",mean(revenue))
# print("median revenue:",median(revenue))
# print("revenue sd:",stdev(revenue))
# print("minimum revenue:",min(revenue))
# print("maximum revenue:",max(revenue))

#complete real world project
#employyee performance statistics system
# from statistics import (mean,median,mode,multimode,stdev,variance,correlation,linear_regression)
# employees=[
#     {
#         "name":"Rahul",
#         "salary":30000,
#         "performance":75

#     },
#     {
#         "name":"Amit",
#         "salary":35000,
#         "performance":80

#     },
#     {
#         "name":"Neha",
#         "salary":40000,
#         "performance":85

#     },
#     {
#         "name":"Priya",
#         "salary":45000,
#         "performance":90


#     },
#     {
#         "name":"Ankit",
#         "salary":38000,
#         "performance":80

#     },
#     {
#         "name":"Riya",
#         "salary":42000,
#         "performance":85

#     },
#     {
#         "name":"Vikas",
#         "salary":50000,
#         "performance":95
#     }
# ]
# salaries=[
#     employee["salary"]
#     for employee in employees
# ]
# performance=[
#     employee["performance"]
#     for employee in employees
# ]
# print("="*55)
# print(
#     "Employee STATISTICS REPORT"
# )
# print("="*55)
# print("\nSalary ANALYSIS:")
# print("average salary:",mean(salaries))
# print("median salary:",median(salaries))
# print("minimum salary:",min(salaries))
# print("maximum salary:",max(salaries))
# print("salary variance:",variance(salaries))
# print("salary standard deviation:",stdev(salaries))
# print("\nPerformance ANALYSIS:")
# print("average performance:",mean(performance))
# print("median performance:",median(performance))
# print("performance mode:",mode(performance))
# print("all performance modes:",multimode(performance))
# print("performance variance:",variance(performance))
# print("performance standard deviation:",stdev(performance))
# print("\nRelationship ANALYSIS")
# correlation_value=correlation(salaries,performance)
# print("correlation between salary and performance:",correlation_value)
# print("\nRegression ANALYSIS")
# model=linear_regression(salaries,performance)
# print("slope:",model.slope)
# print("intercept:",model.intercept)
# test_salary=60000
# predicted_performance=(model.slope * test_salary + model.intercept)
# print("predicted performance for salary",test_salary,":",predicted_performance)
# print("Predicted Performance:",predicted_performance)
# print("\nEMPLOYEE SUMMARY")
# for employee in employees:
#     print(
#         employee["name"],
#         "- Salary:",
#         employee["salary"],
#         "- Performance:", 
#        employee["performance"]
#    )

#print("\nReport Completed.")

#sales data statistics analysis
# from statistics import (mean, median, stdev ,variance,quantiles,correlation)
# sales=[12000,15000,18000,14000,22000,25000,28000,24000,30000,32000]
# customers=[120,140,150,135,180,200,220,210,250,270]
# print("="*50)
# print("SALES ANALYSIS")
# print("="*50)
# print("\nMean Sales:",mean(sales))
# print("Median Sales:",median(sales))
# print("variance:",variance(sales))
# print("standard deviation:",stdev(sales))
# q1,q2,q3=quantiles(sales,n=4)
# print("Q1:",q1)
# print("Q2:",q2)
# print("Q3:",q3)
# print("\ncustomer-sales correlation:",correlation(customers,sales))
# print("\nminimum sales:",min(sales))
# print("maximum sales:",max(sales))
# print("total sales:",sum(sales))


