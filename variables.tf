# required
variable "name" {
  description = "Name/name prefix to apply to the resources in the module."
  type        = "string"
}

variable "task_definition" {
  description = "The family and revision (family:revision) or full ARN of the task definition that you want to run in your service."
  type        = "string"
}

variable "cluster" {
  description = "The name of the ECS cluster to deploy the service to."
  type        = "string"
  default     = "default"
}
