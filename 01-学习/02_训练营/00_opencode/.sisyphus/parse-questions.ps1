# Parse all question bank markdown files and generate index
$basePath = ".sisyphus\java-interview\question-bank"
$modules = @{}

$rootPath = Get-Location

$moduleMap = @{
    "Redis\u9898\u5e93 1.md" = "redis"
    "Java/Java\u96c6\u5408.md" = "java_collections"
    "Java/Java\u57fa\u7840.md" = "java_basics"
    "Java/SpringCloud.md" = "spring_cloud"
    "Java/SSM.md" = "ssm"
    "Java/JVM.md" = "jvm"
    "Java/Java\u5e76\u53d1\u7f16\u7a0b.md" = "concurrency"
    "Java/\u591a\u7ebf\u7a0b\u7f16\u7a0b\u9898.md" = "concurrency_coding"
    "\u5206\u5e03\u5f0f/\u5206\u5e03\u5f0f\u9898\u5355.md" = "distributed"
    "MySql/MYSQL\u9898\u5e93.md" = "mysql"
}

foreach ($file in $moduleMap.Keys) {
    $moduleKey = $moduleMap[$file]
    $fullPath = Join-Path $rootPath $file
    $content = Get-Content $fullPath -Raw -Encoding utf8
    
    $questions = @()
    $currentSection = "\u672a\u5206\u7c7b"
    $questionNum = 0
    
    $lines = $content -split "`n"
    
    foreach ($line in $lines) {
        $line = $line.Trim()
        
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        
        if ($line -match '^#{2,3}\s+(.+)$') {
            $currentSection = $matches[1].Trim()
            continue
        }
        
        if ($line -match '^(?:###\s*)?(\d+[\.\d]*)\.\s+(.+)$') {
            $questionNum++
            $num = $matches[1]
            $text = $matches[2].Trim()
            
            if ([string]::IsNullOrWhiteSpace($text)) { continue }
            
            $questions += @{
                id = "$moduleKey-$questionNum"
                number = $num
                text = $text
                section = $currentSection
                module = $moduleKey
                status = "unanswered"
                score = $null
                attempts = 0
                last_answered = $null
                tags = @()
                related_questions = @()
                notes = ""
            }
        }
    }
    
    $modules[$moduleKey] = @{
        total = $questions.Count
        questions = $questions
    }
    
    Write-Host "Parsed $moduleKey : $($questions.Count) questions"
}

$result = @{
    version = "1.0.0"
    description = "\u9898\u5e93\u7d22\u5f15 - \u6bcf\u9053\u9898\u7684\u5143\u6570\u636e\u548c\u72b6\u6001\u8ffd\u8e2a"
    generated = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    modules = $modules
}

$jsonPath = Join-Path $rootPath "$basePath\index.json"
$result | ConvertTo-Json -Depth 5 | Out-File $jsonPath -Encoding utf8

Write-Host "`nTotal modules: $($modules.Count)"
$totalQ = ($modules.Values | ForEach-Object { $_.total }) | Measure-Object -Sum
Write-Host "Total questions: $($totalQ.Sum)"
Write-Host "Index saved to: $jsonPath"
