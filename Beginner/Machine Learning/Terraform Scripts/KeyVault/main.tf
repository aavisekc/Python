data "azurerm_key_vault" "existing" {
  provider            = azurerm.kv_provider
  name                = "UMPKeyVault"
  resource_group_name = "CIAVDRg"
}

data "azurerm_key_vault_secret" "vmusername" {
  provider = azurerm.kv_provider
  name     = "VmAdminUsername"
  key_vault_id = data.azurerm_key_vault.existing.id
}

data "azurerm_key_vault_secret" "vmadminpassword" {
  provider = azurerm.kv_provider
  name     = "VmAdminPassword"
  key_vault_id = data.azurerm_key_vault.existing.id
}

data "azurerm_key_vault_secret" "domainadminusername" {
  provider = azurerm.kv_provider
  name     = "DomainAdminUserName"
  key_vault_id = data.azurerm_key_vault.existing.id
}

data "azurerm_key_vault_secret" "domainadminpassword" {
  provider = azurerm.kv_provider
  name     = "DomainAdminPassword"
  key_vault_id = data.azurerm_key_vault.existing.id
}

data "azurerm_key_vault_secret" "domainname" {
  provider = azurerm.kv_provider
  name     = "DomainName"
  key_vault_id = data.azurerm_key_vault.existing.id
}

