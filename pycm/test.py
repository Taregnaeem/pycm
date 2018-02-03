# -*- coding: utf-8 -*-
'''
>>> import coverage
>>> from pycm import *
>>> cov=coverage.Coverage()
>>> cov.start()
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> print(cm)
Predict          0        1        2
Actual
0                3        0        0
1                0        1        2
2                2        1        3
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
Overall_ACC                                                      0.58333
Overall_Kappa                                                    0.35484
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(accuracy)                                                    0.83333                 0.75                    0.58333
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0
ERR(Error Rate)                                                  0.16667                 0.25                    0.41667
F0.5(F0.5 Score)                                                 0.65217                 0.45455                 0.57692
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
F2(F2 Score)                                                     0.88235                 0.35714                 0.51724
FDR(false discovery rate)                                        0.4                     0.5                     0.4
FN(false negative/miss/Type II error)                            0                       2                       3
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(false omission rate)                                         0.0                     0.2                     0.42857
FP(false positive/Type I error/false alarm)                      2                       1                       2
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
K(Kappa)                                                         0.81395                 0.73913                 0.47368
LR+(Positive likelihood ratio)                                   4.5                     3.0                     1.5
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NPV(negative predictive value)                                   1.0                     0.8                     0.57143
P(Condition positive)                                            3                       3                       6
POP(Population)                                                  12                      12                      12
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
RACC(Random Accuracy)                                            0.10417                 0.04167                 0.20833
SOA1(Strength of Agreement,Landis and Koch)                      Almost Perfect          Substantial             Moderate
SOA2(Strength of Agreement,Fleiss)                               Excellent               Intermediate to Good    Intermediate to Good
SOA3(Strength of Agreement,Altman)                               Very Good               Good                    Moderate
TN(true negative/correct rejection)                              7                       8                       4
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(true positive/hit)                                            3                       1                       3
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
<BLANKLINE>
>>> cm.stat()
Overall Statistics :
<BLANKLINE>
Overall_ACC                                                      0.58333
Overall_Kappa                                                    0.35484
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(accuracy)                                                    0.83333                 0.75                    0.58333
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0
ERR(Error Rate)                                                  0.16667                 0.25                    0.41667
F0.5(F0.5 Score)                                                 0.65217                 0.45455                 0.57692
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
F2(F2 Score)                                                     0.88235                 0.35714                 0.51724
FDR(false discovery rate)                                        0.4                     0.5                     0.4
FN(false negative/miss/Type II error)                            0                       2                       3
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(false omission rate)                                         0.0                     0.2                     0.42857
FP(false positive/Type I error/false alarm)                      2                       1                       2
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
K(Kappa)                                                         0.81395                 0.73913                 0.47368
LR+(Positive likelihood ratio)                                   4.5                     3.0                     1.5
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NPV(negative predictive value)                                   1.0                     0.8                     0.57143
P(Condition positive)                                            3                       3                       6
POP(Population)                                                  12                      12                      12
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
RACC(Random Accuracy)                                            0.10417                 0.04167                 0.20833
SOA1(Strength of Agreement,Landis and Koch)                      Almost Perfect          Substantial             Moderate
SOA2(Strength of Agreement,Fleiss)                               Excellent               Intermediate to Good    Intermediate to Good
SOA3(Strength of Agreement,Altman)                               Very Good               Good                    Moderate
TN(true negative/correct rejection)                              7                       8                       4
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(true positive/hit)                                            3                       1                       3
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
<BLANKLINE>
>>> cm_2 = ConfusionMatrix(y_actu, 2)
Traceback (most recent call last):
        ...
pycm.pycm.pycmError: Input Vectors Must Be List
>>> cm_3 = ConfusionMatrix(y_actu, [1,2])
Traceback (most recent call last):
        ...
pycm.pycm.pycmError: Input Vectors Must Be The Same Length
>>> pycm_help()
<BLANKLINE>
 _ __   _   _   ___  _ __ ___
| '_ \ | | | | / __|| '_ ` _ \
| |_) || |_| || (__ | | | | | |
| .__/  \__, | \___||_| |_| |_|
|_|     |___/
<BLANKLINE>
__     __     ___      _  _
\ \   / / _  / _ \    | || |
 \ \ / / (_)| | | |   | || |_
  \ V /   _ | |_| | _ |__   _|
   \_/   (_) \___/ (_)   |_|
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
Webpage : http://pycm.shaghighi.ir
>>> TTPN_calc(0,0)
'inf'
>>> FXR_calc(None)
'None'
>>> ACC_calc(0,0,0,0)
'inf'
>>> MCC_calc(0,2,0,2)
'inf'
>>> MK_BM_calc(2,"None")
'None'
>>> PRE_calc(None,2)
'None'
>>> G_calc(None,2)
'None'
>>> kappa_calc(1,None)
'None'
>>> kappa_analysis_koch(None)
'None'
>>> kappa_analysis_fleiss(None)
'None'
>>> kappa_analysis_altman(None)
'None'
>>> F_calc(TP=0,FP=0,FN=0,Beta=1)
'inf'
>>> save_stat=cm.save_stat("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.pycm'"}
True
>>> ERR_calc(None)
'None'
>>> cm.F_beta(4)
{0: 0.9622641509433962, 1: 0.34, 2: 0.504950495049505}
>>> y_test = [5, 5, 5, 0, 0, 0]
>>> y_pred = [5, 0, 0, 0, 0, 0]
>>> cm=ConfusionMatrix(y_test, y_pred)
>>> print(cm)
Predict          0        5
Actual
0                3        0
5                2        1
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
Overall_ACC                                                      0.66667
Overall_Kappa                                                    0.33333
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       5
ACC(accuracy)                                                    0.66667                 0.66667
BM(Informedness or Bookmaker Informedness)                       0.33333                 0.33333
DOR(Diagnostic odds ratio)                                       None                    None
ERR(Error Rate)                                                  0.33333                 0.33333
F0.5(F0.5 Score)                                                 0.65217                 0.71429
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.5
F2(F2 Score)                                                     0.88235                 0.38462
FDR(false discovery rate)                                        0.4                     0.0
FN(false negative/miss/Type II error)                            0                       2
FNR(miss rate or false negative rate)                            0.0                     0.66667
FOR(false omission rate)                                         0.0                     0.4
FP(false positive/Type I error/false alarm)                      2                       0
FPR(fall-out or false positive rate)                             0.66667                 0.0
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.57735
K(Kappa)                                                         0.42857                 0.63636
LR+(Positive likelihood ratio)                                   1.5                     None
LR-(Negative likelihood ratio)                                   0.0                     0.66667
MCC(Matthews correlation coefficient)                            0.44721                 0.44721
MK(Markedness)                                                   0.6                     0.6
N(Condition negative)                                            3                       3
NPV(negative predictive value)                                   1.0                     0.6
P(Condition positive)                                            3                       3
POP(Population)                                                  6                       6
PPV(precision or positive predictive value)                      0.6                     1.0
PRE(Prevalence)                                                  0.5                     0.5
RACC(Random Accuracy)                                            0.41667                 0.08333
SOA1(Strength of Agreement,Landis and Koch)                      Moderate                Substantial
SOA2(Strength of Agreement,Fleiss)                               Intermediate to Good    Intermediate to Good
SOA3(Strength of Agreement,Altman)                               Moderate                Good
TN(true negative/correct rejection)                              1                       3
TNR(specificity or true negative rate)                           0.33333                 1.0
TON(Test outcome negative)                                       1                       5
TOP(Test outcome positive)                                       5                       1
TP(true positive/hit)                                            3                       1
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333
<BLANKLINE>
>>> cov.stop()
>>> cov.save()

'''