"""So the problem is that you forgot your anniversary year (Dangerous Year!). However, you remember that you have been married for N years. Can you print your marriage year to impress your angry wife?

Input Format

N

Constraints

1 <= N <= 88

Output Format

Year of your marriage

Sample Input 0

23

Sample Output 0

2000

Explanation 0

So only if you were married at 2000, then you are married for 23 years."""

from datetime import datetime

married_for = int(input("What's your married life age? :) "))

current_year = datetime.now().year

married_year = current_year - married_for

print("You marreid at", married_year)