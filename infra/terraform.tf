terraform {
  required_version = ">=1.0.1"
  backend "s3" {
    bucket = "spendings-bot-infra-state"
    key = "terraform.tfstate"
  }
}


