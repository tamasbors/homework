variable "namespace" {
  type        = string
  default     = "myapp-namespace"
  description = "Name of the kubernetes namespace"
}

variable "environment" {
  type        = string
  default     = "dev"
  description = "Name of the environment"
}

variable "image_tag" {
  type        = string
  default     = "latest"
  description = "The tag of the image"
}

variable "repository" {
  type        = string
  default     = "tamasbors/myapp"
  description = "The repository of the image"
}

variable "replica_count" {
  type        = number
  default     = 1
  description = "The number of replicas to deploy"
}

variable "kube_config_path" {
  type        = string
  default     = "~/.kube/config"
  description = "Path to kubeconfig file"
}