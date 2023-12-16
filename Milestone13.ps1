cls
$readName = Read-Host -Prompt "Which VM would you like to edit? Seperate with commas."
cls
choice

function choice() {

    Write-Host " [1] Start VM"
    Write-Host " [2] Stop VM"
    Write-Host " [3] Change VM Network"
    Write-Host " [4] Snapshot VM"
    Write-Host " [5] Delete VM"
    Write-Host " [6] Change CPU Count"

  
    $readChoice = Read-Host -Prompt "Which action would you like to complete?"
    
    choice_check -userChoice $readChoice
}

function choice_check() {
    Param([String]$userChoice)

    if ($userChoice -Match "1") {
        choice_one
        choice
    }

    if ($userChoice -Match "2") {
        choice_two
        choice
    }

    if ($userChoice -Match "3") {
        choice_three

        choice
    }
    if ($userChoice -Match "4") {
        choice_four
        choice
    }

    if ($userChoice -Match "5") {
        choice_five
        choice
    }

    if ($userChoice -Match "6") {
        choice_six
        choice
    }
}

function choice_one() {
    Start-VM $readName
    Start-Sleep -Seconds 5
    cls
}

function choice_two() {
    Stop-VM $readName
    Start-Sleep -Seconds 5
    cls
}

function choice_three() {
    $readSwitch = Read-Host -Prompt "Specify your switch name."
    Connect-VMNetworkAdapter -VMName $readName -SwitchName $readSwitch
    Start-Sleep -Seconds 5
    cls
}


function choice_four() {
    $readSnapshot = Read-Host -Prompt "Specify your snapshot name."
    Checkpoint-VM -Name $readName -SnapshotName $readSnapshot
    Start-Sleep -Seconds 5
    cls
}

function choice_five() {
    Remove-VM $readName
    Start-Sleep -Seconds 5
    cls
}

function choice_six() {
    $readCPU = Read-Host -Prompt "How many CPU's do you want?"
    Set-VMProcessor $readName -Count $readCPU
    Start-Sleep -Seconds 5
    cls
}