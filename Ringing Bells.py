'''
Ringing Bells
There are N bells in a city. Each bell rings after a particular period of time(given in minutes). The period of each bell is provided in form of an array of integers. The moment when all the bells ring together is considered an auspicious moment by the people of the city and they take decisions on the basis of this. However, the people of the city are mathematically dumb and think it as a form of some sort of a magic. When you entered the city you saw all the bells ringing together. Lets say it was T=0(time). Can you use your knowledge of mathematics to predict how many minutes from T=0, would all the bells ring again?

Constraints
1<= Number of bells <=1000000 1<= Time period of bells<= 1000

Input
First line of the input contains the number of bells in the city. The second line contains the time periods of ringing of each of the N bells in a space separated manner.

Output
Print the time(in minutes) from T=0 when the all the bells in the city are supposed to ring together again.

Example
Input:

6

3 4 6 2 1 18

Output:

36

Explanation:

Next time All the bells of the city will ring together at T=36 minutes.
'''
# your code goes here
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
n=int(input())
arr=[int(x) for x in input().split()]
ans=arr[0]
for i in range(1,n):
	ans=(ans*arr[i])//gcd(ans,arr[i])
print(ans)