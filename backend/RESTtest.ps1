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

        $headers = @{
            "Authorization" = "Bearer $($result.access)"
        }

        Invoke-RestMethod "http://localhost:8000/api/users/" -Headers $headers -Method Get | ConvertTo-Json -Depth 10 > .\result.json

    }
    catch {
        $_

        $statusCode = $_.Exception.Response.StatusCode.value__
        Write-Error "Status Code: $statusCode"
    }
    
}

get_protected_path