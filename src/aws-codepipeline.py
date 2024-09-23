from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM
from diagrams.aws.network import VPC
from diagrams.aws.devtools import Codecommit, Codepipeline, Codebuild, Codedeploy
from diagrams.aws.management import Cloudformation

graph_attr = {
    "fontsize": "45",
    "bgcolor": "black",
    "fontcolor": "white"
}

node_attr = {
    "fontsize": "14",
    "color": "white",
    "fontcolor": "white"
}

edge_attr = {
    "fontsize": "12",
    "color": "white",
    "fontcolor": "white"
}

cluster_attr = {
    "bgcolor": "black",
    "color": "white",
    "fontcolor": "white",
    "fontsize": "20"  # Increased font size for clusters
}

with Diagram("AWS CodePipeline Infrastructure with CloudFormation", show=False, direction="LR", graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
    cfn = Cloudformation("CloudFormation")

    codecommit = Codecommit("CodeCommit\nRepository")
    
    with Cluster("CodePipeline", graph_attr=cluster_attr):
        pipeline = Codepipeline("Pipeline")
        
        with Cluster("Stages", graph_attr=cluster_attr):
            source = Codecommit("Source")
            deploy = Codedeploy("Deploy")
            test = Codebuild("Acceptance\nTest")
        
        pipeline >> Edge(color="lightgreen", style="bold") >> source >> deploy >> test

    with Cluster("VPC", graph_attr=cluster_attr):
        ec2 = EC2("EC2 Instance")

    s3 = S3("Artifact\nStore")
    
    iam_role = IAM("IAM Roles")

    cfn >> Edge(color="lightblue", style="bold") >> [codecommit, pipeline, ec2, s3, iam_role]
    codecommit >> Edge(color="lightgreen", style="bold") >> pipeline
    pipeline >> Edge(color="lightgreen", style="bold") >> s3
    pipeline >> Edge(color="lightgreen", style="bold") >> ec2
    iam_role - Edge(color="pink", style="bold") - pipeline
    iam_role - Edge(color="pink", style="bold") - ec2
