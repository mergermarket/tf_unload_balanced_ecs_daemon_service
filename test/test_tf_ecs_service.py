import unittest
import time
from subprocess import check_call, check_output


class TestTFECSService(unittest.TestCase):

    def setUp(self):
        check_call(['terraform', 'init', 'test/infra'])
        check_call(['terraform', 'get', 'test/infra'])

    def test_create_ecs_service(self):
        # Given
        name = 'test-' + str(int(time.time() * 1000))
        task_definition = (
            "arn:aws:ecs:us-east-1:123456789012:task-definition/hello_world:8"
        )

        # When
        output = check_output([
            'terraform',
            'plan',
            '-var', 'name={}'.format(name),
            '-var', 'task_definition={}'.format(task_definition),
            '-no-color',
            '-target=module.service_raw',
            'test/infra'
        ]).decode('utf-8')

        # Then
        assert """
+ module.service_raw.aws_ecs_service.service
      id:                      <computed>
      cluster:                 "default"
      enable_ecs_managed_tags: "false"
      iam_role:                <computed>
      launch_type:             "EC2"
      name:                    "{name}"
      platform_version:        <computed>
      scheduling_strategy:     "DAEMON"
      task_definition:         "{task_definition}"
        """.format(
            name=name, task_definition=task_definition
        ).strip() in output
