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
14. director_fees
15. deferred_income
16. long_term_incentive
17. email_address
18. from_poi_to_this_person

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

'from_this_person_to_poi' : BECK SALLY W, KEAN STEVEN J, ,LAVORATO JOHN J, DELAINEY DAVID W

'director_fees' : significent banding observed around 1M and at 0.4M. No obvious outliers.


Several of these plots showed a very significent disparity between the shortlisted names and the rest. Current senior executive remuneration trends commonly result in remuneration packages including various forms of stock incentives. While these disparities are not indicative of the person being a POI in terms of the criminal issues, the recurrence of names known to be POI provides good reason to examine this data in more detail using statistical methods. Also of interest is the correlation between publically reported remuneration packages due to regulatory requirements and remuneration less visible to scrutiny via public financial reports.








