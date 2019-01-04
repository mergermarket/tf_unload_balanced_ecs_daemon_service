resource "aws_ecs_service" "service" {
  name                = "${var.name}"
  task_definition     = "${var.task_definition}"
  cluster             = "${var.cluster}"

  scheduling_strategy = "DAEMON"
}
