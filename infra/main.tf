locals {
  service_name = 'spendings-bot'
  environment = terraform.workspace
  tfenvfile = "${path.module}/config/tfenv-${local.environment}"
  tfenv = jsondecode(file(local.tfenvfile))
}

