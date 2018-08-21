import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='rakesh')
    ec2 = session.resource('ec2')
    for k in ec2.instances.all():
        print(k)
