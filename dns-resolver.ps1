# dns-resolver.ps1
# Usage: .\dns-resolver.ps1 192.168.3 192.168.4.5

$Subnet = $args[0]
$DnsServer = $args[1]

1..254 | ForEach-Object {
    $ip = "$Subnet.$_"
    $result = Resolve-DnsName -Name $ip -DnsOnly -Server $DnsServer -Type PTR -ErrorAction Ignore
    if ($result.NameHost) {
        "$ip $($result.NameHost)"
    }
}

