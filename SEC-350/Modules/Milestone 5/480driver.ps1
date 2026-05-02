$conf = Get-480Config -config_path ":/home/anthony"
480Connect -server $conf.vcenter_server

Write-Host "Please Select your VM"
Select-VM -folder "BASEVM"
