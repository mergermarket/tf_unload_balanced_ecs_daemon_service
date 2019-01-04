# fixture
module "service_raw" {
  source = "../.."

  # required
  name            = "${var.name}"
  task_definition = "${var.task_definition}"
}

# configure provider to not try too hard talking to AWS API
provider "aws" {
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_get_ec2_platforms      = true
  skip_region_validation      = true
  skip_requesting_account_id  = true
  max_retries                 = 1
  access_key                  = "a"
  secret_key                  = "a"
  region                      = "eu-west-1"
}

# variables
variable "name" {}

variable "task_definition" {}
