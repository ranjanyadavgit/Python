text = "Python is awesome"
words = text.split()
print("Words:", words)

arn="arn:aws:ec2:us-east-1:123456789012:instance/i-012abcd34efghi56"

splitss=arn.split("/")


print("arns:",splitss[1])

o/p->Words: ['Python', 'is', 'awesome']
arns: i-012abcd34efghi56
