terraform {
  required_version = ">=1.0.1"
  backend "s3" {
    bucket = "spendings-bot-infra-state"
    key = "terraform.tfstate"
  }
}
locals {
  service_name = "spendings-bot"
}
resource "aws_ecs_cluster" "this" {
  name = "${local.service_name}-cluster"
}

resource "aws_instance" "this" {
  instance_type = "t3.micro"
}
