resource "kubernetes_namespace_v1" "homework" {
  metadata {
    name = var.namespace
  }
}

resource "helm_release" "homework" {
  name      = "homework"
  chart     = "${path.module}/../helm/"
  namespace = kubernetes_namespace_v1.homework.metadata[0].name

  set = [
    {
      name  = "image.repository"
      value = var.repository
    },
    {
      name  = "image.tag"
      value = var.image_tag
    },
    {
      name  = "replicaCount"
      value = var.replica_count
    },
    {
      name  = "environment"
      value = var.environment
    }
  ]
}