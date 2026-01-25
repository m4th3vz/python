# Caminho do diretório principal onde estão as pastas a serem personalizadas
$rootPath = "C:\Caminho\Para\Seu\Diretorio"

# Obtém todas as pastas dentro do diretório principal, recursivamente
$folders = Get-ChildItem -Path $rootPath -Directory -Recurse

foreach ($folder in $folders) {
    $iniPath = Join-Path -Path $folder.FullName -ChildPath "desktop.ini"
    $icoPath = Join-Path -Path $folder.FullName -ChildPath "favicon.ico"
    
    # Verifica se o arquivo favicon.ico existe na pasta
    if (Test-Path $icoPath) {
        $content = @"
[.ShellClassInfo]
IconFile=favicon.ico
IconIndex=0
"@
        # Cria ou substitui o arquivo desktop.ini com o conteúdo necessário
        Set-Content -Path $iniPath -Value $content -Force
        
        # Define os atributos do arquivo desktop.ini para oculto e somente leitura
        attrib +h +s $iniPath
        
        # Define a pasta como somente leitura
        attrib +r $folder.FullName
    }
}

# Reinicia o Windows Explorer para aplicar as mudanças
Stop-Process -Name explorer -Force
Start-Process explorer
