terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
  required_version = ">= 0.14.9"
}
provider "aws" {
    profile = "default"
    region  = var.region
}
resource "aws_instance" "app_server" {
    ami = "ami-09ce2fc392a4c0fbc"
    instance_type = "t2.micro"
    tags = {
    Name = var.instance_name
    }
}
