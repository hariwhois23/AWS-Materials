## getting name of the key being used
   ``` $ aws ec2 describe-instances --instance-ids <instance_id> --query "Reservations[0].Instances[0].KeyName" --output text ```
