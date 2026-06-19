function get_token()
{
    $body = @{
        username = "admin"
        password = "qwerty"
    } | ConvertTo-Json


    Invoke-RestMethod "http://localhost:8000/auth/login/" -Body $body -Method Post -ContentType "application/json" | ConvertTo-Json

}


function get_protected_path()
{
    try {
        $result = get_token | ConvertFrom-Json -AsHashtable
        Write-Host $result.Keys
        
        $headers = @{
            "Authorization" = "Bearer $($result.access)"
        }

        Invoke-RestMethod "http://localhost:8000/api/users/" -Headers $headers -Method Get | ConvertTo-Json -Depth 10 > .\result.json

        $result.refresh

    }
    catch {
        $_

        $statusCode = $_.Exception.Response.StatusCode.value__
        Write-Error "Status Code: $statusCode"
    }
    
}

function refresh_token($boom)
{
    $body = @{
        "refresh" = $boom
    } | ConvertTo-Json

    Invoke-RestMethod "http://localhost:8000/api/token/refresh/" -Body $body -Method Post -ContentType "application/json" -Debug
}

$refresh = get_protected_path

refresh_token $refresh