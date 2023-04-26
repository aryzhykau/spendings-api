resource "aws_vpc" "this" {
  cidr_block = local.tfenv.vpc.cidr
  tags = {
    Name = "${local.service_name}-vpc"
  }
}

resource "aws_subnet" "this" {
  count = length(local.tfenv.vpc.subnets)
  cidr_block = local.tfenv.vpc.subnets[count.index]
  vpc_id     = aws_vpc.this.id
}