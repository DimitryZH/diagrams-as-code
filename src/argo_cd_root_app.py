from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.k8s.ecosystem import Helm
from diagrams.k8s.compute import Deployment
from diagrams.aws.network import ELB
from diagrams.onprem.gitops import ArgoCD
from diagrams.onprem.vcs import Github


# Define attributes for Nodes.
# The Node is an abstract concept that represents a single system component object.
# The node object consists of three parts: provider, resource type and name.

ic_attrs = {
    "fontsize": "16",
    "fontname": "Helvetica bold" 
   }


# Define attributes for the Cluster
# Cluster allows you group (or clustering) the nodes in an isolated group.
ea = {
    "fontsize": "26",
    "style": "filled",
    "color": "lightgrey",
    "fontname": "Helvetica bold"
}


# Define global attributes for the diagram
global_attrs = {
    "fontsize": "40",
    "fontname": "Helvetica bold"
   }


with Diagram("Argo CD Root Application Manager Overview", show=True, direction="LR", graph_attr=global_attrs):
    eks = EKS("EKS Cluster", **ic_attrs)
    github = Github("GitHub Repo", **ic_attrs)

    with Cluster("ArgoCD", graph_attr=ea):
        argocd = ArgoCD("Root App",**ic_attrs)
        app1 = ArgoCD("App1", **ic_attrs)
        app2 = ArgoCD("App2", **ic_attrs)
        argocd - [app2, app1]

    with Cluster("Development Environment", graph_attr=ea):
        dev_helm = Helm("Dev Helm Chart", **ic_attrs)
        dev_deployment = Deployment("Dev Deployment", **ic_attrs)
        dev_elb = ELB("Dev ELB", **ic_attrs)
        dev_helm >> dev_deployment >> dev_elb

    with Cluster("Production Environment", graph_attr=ea):
        prod_helm = Helm("Prod Helm Chart", **ic_attrs)
        prod_deployment = Deployment("Prod Deployment", **ic_attrs)
        prod_elb = ELB("Prod ELB", **ic_attrs)
        prod_helm >> prod_deployment >> prod_elb

    eks >> argocd
    app1 >> [dev_helm, prod_helm]
    app2 >> [dev_helm, prod_helm]
    github >> argocd