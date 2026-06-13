
function get_token()
{
    $body = @{
        username = "admin"
        password = "qwerty"
    } | ConvertTo-Json


    Invoke-RestMethod "http://localhost:8000/api/token/" -Body $body -Method Post -ContentType "application/json" | ConvertTo-Json
}


function get_protected_path()
{
    $result = get_token | ConvertFrom-Json -AsHashtable

    $headers = @{
        "Authorization" = "Bearer $($result.access)"
    }

    Invoke-RestMethod "http://localhost:8000/api/users/" -Headers $headers -Method Get | ConvertTo-Json > .\result.json
}

get_protected_path