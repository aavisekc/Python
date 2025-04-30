# variables.tf

variable "key_vault_name" {
  description = "Name of the existing Azure Key Vault"
  type        = string
}

variable "key_vault_resource_group" {
  description = "Name of the resource group containing the Key Vault"
  type        = string
}

variable "secret_names" {
  description = "List of secret names to retrieve from the Key Vault"
  type        = list(string)
  default     = []
}

variable "use_kv_provider" {
  description = "Whether to use the alternate KV provider configuration"
  type        = bool
  default     = false
}

variable "key_vault_subscription_id" {
  description = "Subscription ID for the Key Vault (if different from main)"
  type        = string
  default     = null
}