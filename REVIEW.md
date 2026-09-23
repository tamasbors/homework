# Review


1. **Terraform**: invalid use of the "set" block
   - use `terraform validate` to check code
   - use the documententation: [helm_release](https://registry.terraform.io/providers/hashicorp/helm/latest/docs/resources/release#example-usage---chart-repository)
2. **Terraform**:  missing value in the set block,and use variables rather hard-coded values
3. **Terraform**: fix `helm` provider in `providers.tf` file
   - documententation of helm provider: [helm provider](https://registry.terraform.io/providers/hashicorp/helm/latest/docs#resources)
4. **Helm**: wrong containerPort in `deployment.yaml` (or inconsistency with ports elsewhere)
5. **Helm**: fix naming, labels and selectors across the templates


---
Nice to have:
1. **Terraform**: keep modules up to date (`kubernetes_namespace` -> `kubernetes_namespace_v1`)

2. **Terraform**: provide default values in `variables.tf`
3. **Helm**: unused or unnecessary variables
     - unused: replicaCount
     - unnecessary: service.port

+1. **Formatting**:
   - unnecessary empty lines and trailing whitespaces (use `Trailing Spaces` extension in VSCode)
   - messed up indentation (use `indent-rainbow` extension)
   - `terraform fmt` helps with terraform :)
