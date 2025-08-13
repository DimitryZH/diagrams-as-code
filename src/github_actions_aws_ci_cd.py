import yaml
from graphviz import Digraph
from pathlib import Path

# Path to the GitHub Actions YAML
yaml_path = Path(".github/workflows/main.yaml")

# Load the GitHub Actions YAML
with open(yaml_path, "r") as file:
    workflow = yaml.safe_load(file)

# Main diagram top-to-bottom (each part vertical)
dot = Digraph(comment=workflow.get("name", "GitHub Actions Workflow"))
dot.attr(fontsize="10")

jobs = workflow.get("jobs", {})

# Separate jobs into CI and CD lists
ci_jobs = {j: d for j, d in jobs.items() if "ci" in j.lower()}
cd_jobs = {j: d for j, d in jobs.items() if "cd" in j.lower()}

# CI cluster (left)
with dot.subgraph(name="cluster_ci") as ci_cluster:
    ci_cluster.attr(
        rankdir="TB",
        style="filled",
        color="#D5F5E3",
        fontsize="12",
    )
    for job_name, job_data in ci_jobs.items():
        ci_cluster.node(
            job_name,
            f"{job_name}\n({job_data.get('runs-on', '')})",
            shape="box",
            style="filled",
            fillcolor="#AED6F1",
        )
        prev_step_node = None
        for idx, step in enumerate(job_data.get("steps", []), 1):
            step_name = step.get("name", f"Step {idx}")
            step_node_id = f"{job_name}_{idx}"
            ci_cluster.node(
                step_node_id,
                step_name,
                shape="rect",
                style="rounded,filled",
                fillcolor="#F9E79F",
            )
            if prev_step_node:
                ci_cluster.edge(prev_step_node, step_node_id)
            else:
                ci_cluster.edge(job_name, step_node_id)
            prev_step_node = step_node_id

# CD cluster (right)
with dot.subgraph(name="cluster_cd") as cd_cluster:
    cd_cluster.attr(
        rankdir="TB",
        style="filled",
        color="#D6EAF8",
        fontsize="12",
    )
    for job_name, job_data in cd_jobs.items():
        cd_cluster.node(
            job_name,
            f"{job_name}\n({job_data.get('runs-on', '')})",
            shape="box",
            style="filled",
            fillcolor="#AED6F1",
        )
        prev_step_node = None
        for idx, step in enumerate(job_data.get("steps", []), 1):
            step_name = step.get("name", f"Step {idx}")
            step_node_id = f"{job_name}_{idx}"
            cd_cluster.node(
                step_node_id,
                step_name,
                shape="rect",
                style="rounded,filled",
                fillcolor="#F9E79F",
            )
            if prev_step_node:
                cd_cluster.edge(prev_step_node, step_node_id)
            else:
                cd_cluster.edge(job_name, step_node_id)
            prev_step_node = step_node_id

# Optional: link last CI step to CD job (dashed)
if ci_jobs and cd_jobs:
    last_ci_job = list(ci_jobs.keys())[0]
    last_ci_step = f"{last_ci_job}_{len(ci_jobs[last_ci_job]['steps'])}"
    first_cd_job = list(cd_jobs.keys())[0]
    dot.edge(last_ci_step, first_cd_job, style="dashed", label="trigger")

# Footer note
dot.attr(
    label="Designed by Dmitry Zhuravlev",
    fontsize="14",
    labelloc="b",
    fontcolor="black",
    style="dashed",
)

# Save and render
output_file = "ci_cd_pipeline_diagram_aws_beanstalk"
dot.render(output_file, format="png", cleanup=True)

print(f"Diagram generated: {output_file}.png")
