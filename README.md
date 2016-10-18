# Udacity - Intro to Machine Learning
## Using Machine Learning to Investigate the Enron fraud
Author : bmatthewtaylor@gmail.com 
github : github.com/aspiringguru/udacityIntroMachineLearning
==============

## Introduction

The Enron scandal, publically revealed in October 2001, led to the bankruptcy of the Enron Corporation, the largest corporate bankruptcy in America at the time. The failure of auditor Arthur Anderson to discharge their professional duties led to the defacto dissolution of one of the largest audit and accountancy partnerships in the world.

Many Enron executives were charged and sentenced to prison for their acts in the case. 

In 2005 the documentry film "Enron: The Smartest Guys in the Room" was made about Enron case.

https://en.wikipedia.org/wiki/Enron_scandal
https://en.wikipedia.org/wiki/Enron:_The_Smartest_Guys_in_the_Room

## Purpose

The purpose of this machine learning analyse is to demonstrate the ability and suitability of machine learning techniques to detect fraud and persons of interest for audit investigations.

## Data

The data available for analysis includes emails and financial information. The financial information includes data on each employees remuneration package, and non direct remuneration. Some of the field names provided are listed below.

1. salary
2. to_messages
3. deferral_payments
4. total_payments
5. exercised_stock_options
6. bonus
7. restricted_stock
8. shared_receipt_with_poi
9. restricted_stock_deferred
10. total_stock_value
11. expenses
12. loan_advances
13. from_messages
14. other
15. from_this_person_to_poi
16. poi
17. director_fees
18. deferred_income
19. long_term_incentive
20. email_address
21. from_poi_to_this_person

Other data considered is a list of known Persons of Interest (POI). This list was collated from court records and media reports of the fraud investigation. 

## Outliers

The numerical data was sorted and plotted for quick visual interpretation. A common outlier across several data columns was the row 'TOTAL' and excluded from further analysis.

Plotting and comparing columns identified a few persons with significantly higher values than the 'normal' distribution, specifically a short list of names appeared in the majority of shortlisted top 10. 

'salary' : 'FREVERT MARK A, LAY KENNETH L, SKILLING JEFFREY K  
'deferral_payments' : FREVERT MARK A  
'total_payments':  'LAY KENNETH L'.  
'exercised_stock_options' : 'HIRKO JOSEPH' and 'LAY KENNETH L'.  
'bonus' : BELDEN TIMOTHY N, SKILLING JEFFREY K, LAY KENNETH L, LAVORATO JOHN J  
'restricted_stock' : WHITE JR THOMAS E, LAY KENNETH L  
'restricted_stock_deferred' : BHATNAGAR SANJAY  
'total_stock_value' : RICE KENNETH D, PAI LOU L, SKILLING JEFFREY K, HIRKO JOSEPH, LAY KENNETH L  
'expenses' : URQUHART JOHN A, MCCLELLAN GEORGE  
'loan_advances' : PICKERING MARK R, FREVERT MARK A, LAY KENNETH L (only three non-zero values in this column)  
'from_messages' : KAMINSKI WINCENTY J  
'from_this_person_to_poi' : BECK SALLY W, KEAN STEVEN J, LAVORATO JOHN J, DELAINEY DAVID W  
'director_fees' : significent banding observed around 1M and at 0.4M. No obvious outliers.  


Several of these plots showed a very significent disparity between the shortlisted names and general employees. Current senior executive remuneration trends commonly result in remuneration packages including various forms of stock incentives. While the disparities in forms of remuneration and total remuneration are not indicative of the person being a Person Of Interest (POI), the recurrence of names known to be POI provides good reason to examine this data in more detail using statistical methods. Also of interest is the correlation between publically reported remuneration packages due to regulatory requirements and remuneration less visible to scrutiny via public financial reports.

## Algorythmic Analysis

Various algorythmic methods were compared as a revision/warm up exercise.

## Naive Bayes

The Naive Bayes method was tested using various keys to identify which provided the highest accuracy. (poi_id_Naive_Bayes1.py)


| keys	                                            | clf.score      | accuracy_score |
| ------------------------------------------------- |:--------------:|:--------------:|
| salary, total_payments, exercised_stock_options   | 0.845360824742 | 0.833333333333 |
| total_payments, exercised_stock_options           | 0.845360824742 | 0.854166666667 |
| total_payments                                    | 0.876288659794 | 0.833333333333 |
| exercised_stock_options                           | 0.886597938144 | 0.875          |
| from_poi_to_this_person                           | 0.886597938144 | 0.854166666667 |
| salary                                            | 0.886597938144 | 0.833333333333 |
| from_this_person_to_poi                           | 0.886597938144 | 0.854166666667 |
nb: clf.score [clf.score(a_train, b_train)] compares the accuracy of predictions on training data.
nbb: accuracy_score [accuracy_score(b_test, b_pred)] compares predicted values with known values on a test set.

Interestingly, while several keys and combinations of keys provided accuracy in the range 83%-88%, none of these models demonstrated a significently higher accuracy than others. The key with the highest accuracy was salary. 

An interesting observation can be drawn from the accuracy wrt emails sent to a poi and emails received from a poi, persons receiving emails from a poi were marginally more likely to be a poi themselve than persons sending emails to a poi. Given the small % difference this factor alone needs further analysis to confirm accuracy as a predictor. 

## Support Vector Machines

The Support Vector Machines method required careful choice of kernel method to achieve a useful result.
Some limited experimentaiton with C values was conducted to optimise results.

| keys	                                            | kernel method | clf.score      | accuracy_score | Fitting Time   | Predicting Time |
| ------------------------------------------------- |:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|
| salary, total_payments, exercised_stock_options   | linear        | no result      | no result      | no result      | no result       |
| total_payments, exercised_stock_options           | linear        | no result      | no result      | no result      | no result       |
| total_payments                                    | linear        | no result      | no result      | no result      | no result       |
| exercised_stock_options                           | linear        | no result      | no result      | no result      | no result       |
| from_poi_to_this_person                           | linear        | 0.886597938144 | 0.854166666667 | 0.0            | 0.0             |
| salary                                            | linear        | 0.876288659794 | 0.854166666667 | 0.0            | 0.0             |
| from_this_person_to_poi                           | linear        | 0.886597938144 | 0.854166666667 | 0.0            | 0.0             |
------------------------------------------------------------------------------------------------------------------------------------------
C=1.0 (default value)
| salary, total_payments, exercised_stock_options   | rbf           | 1.0            | 0.854166666667 | 0.001          | 0.0             |
| total_payments, exercised_stock_options           | rbf           | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| total_payments                                    | rbf           | 1.0            | 0.854166666667 | 0.0            | 0.001           |
| exercised_stock_options                           | rbf           | 0.958762886598 | 0.854166666667 | 0.0            | 0.0             |
| from_poi_to_this_person                           | rbf           | 0.917525773196 | 0.854166666667 | 0.001          | 0.0             |
| salary                                            | rbf           | 1.0            | 0.854166666667 | 0.001          | 0.0             |
| from_this_person_to_poi                           | rbf           | 0.907216494845 | 0.854166666667 | 0.001          | 0.0             |
C=10
------------------------------------------------------------------------------------------------------------------------------------------
| salary, total_payments, exercised_stock_options   | rbf           | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| total_payments, exercised_stock_options           | rbf           | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| total_payments                                    | rbf           | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| exercised_stock_options                           | rbf           | 0.958762886598 | 0.854166666667 | 0.0            | 0.0             |
| from_poi_to_this_person                           | rbf           | 0.948453608247 | 0.8125         | 0.0            | 0.0             |
| salary                                            | rbf           | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| from_this_person_to_poi                           | rbf           | 0.948453608247 | 0.791666666667 | 0.0            | 0.0             |

NB: 'no result' = no solution found in a reasonable time given the dataset size. (cutoffs varied, typically min 3 minutes.)

## Decision Trees

| keys	                                            | clf.score      | accuracy_score | Fitting Time   | Predicting Time |
| ------------------------------------------------- |:--------------:|:--------------:|:--------------:|:---------------:|
| salary, total_payments, exercised_stock_options   | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| total_payments, exercised_stock_options           | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| total_payments                                    | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| exercised_stock_options                           | 0.958762886598 | 0.854166666667 | 0.0            | 0.0             |
| from_poi_to_this_person                           | 0.948453608247 | 0.8125         | 0.0            | 0.0             |
| salary                                            | 1.0            | 0.854166666667 | 0.0            | 0.0             |
| from_this_person_to_poi                           | 0.948453608247 | 0.791666666667 | 0.0            | 0.0             |
------------------------------------------------------------------------------------------------------------------------------------------





Three methods of analysis were considered for the project.
- K nearest neighbours
- Adaboost
- Random Forest




