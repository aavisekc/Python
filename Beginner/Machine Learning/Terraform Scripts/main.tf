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

resource "azurerm_network_interface" "ntwrk_intr" {
  provider            = azurerm.vm_provider
  name                = "networkInterface1"
  location            = "Central India"
  resource_group_name = "LARAVEL-OPEN-AI"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = data.azurerm_subnet.existing_subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_windows_virtual_machine" "azrciavdimg1" {
  provider            = azurerm.vm_provider
  name                = "AZRCIAVDIMG1"
  location            = "Central India"
  resource_group_name = "LARAVEL-OPEN-AI"
  size                = "Standard_B2ms"
  admin_username      = data.azurerm_key_vault_secret.vmusername.value
  admin_password      = data.azurerm_key_vault_secret.vmadminpassword.value

  network_interface_ids = [
    azurerm_network_interface.ntwrk_intr.id
  ]

  os_disk {
    name                 = "AZRCIAVDIMG1-OSDisk"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsDesktop"
    offer     = "windows-11"
    sku       = "win11-23h2-ent"
    version   = "latest"
  }

  tags = {
    Owner      = "LM-Noida"
    Type       = "VDI"
    Location   = "Noida"
    ALocation  = "Central India"
  }
}

resource "azurerm_virtual_machine_extension" "domain_join" {
  provider            = azurerm.vm_provider
  name                = "domainJoin"
  virtual_machine_id  = azurerm_windows_virtual_machine.azrciavdimg1.id
  type                = "JsonADDomainExtension"
  publisher           = "Microsoft.Azure.ActiveDirectory"
  type_handler_version = "1.3"

  settings = <<SETTINGS
    {
      "Name": "${data.azurerm_key_vault_secret.domainname.value}",
      "OUPath": "",
      "User": "${data.azurerm_key_vault_secret.domainadminusername.value}",
      "Restart": "true",
      "Options": "3"
    }
SETTINGS

  protected_settings = <<PROTECTED_SETTINGS
    {
      "Password": "${data.azurerm_key_vault_secret.domainadminpassword.value}"
    }
PROTECTED_SETTINGS
}

resource "azurerm_virtual_machine_extension" "test_ps_script" {
  provider            = azurerm.vm_provider
  name                = "testPSScript"
  virtual_machine_id  = azurerm_windows_virtual_machine.azrciavdimg1.id
  type                = "CustomScriptExtension"
  publisher           = "Microsoft.Compute"
  type_handler_version = "1.10"

  settings = <<SETTINGS
    {
      "commandToExecute": "powershell.exe -ExecutionPolicy Unrestricted -File example.ps1"
    }
SETTINGS

  depends_on = [
    azurerm_virtual_machine_extension.domain_join
  ]
}