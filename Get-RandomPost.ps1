<#
.SYNOPSIS
    Updates GitHub Profile README.md with a random repository.

.DESCRIPTION
    - Fetches all public repositories from your GitHub profile.
    - Picks one at random.
    - Builds a Markdown snippet with name, link, and description.
    - Injects it between markers in README.md:
        <!-- RANDOM-REPO:START --> ... <!-- RANDOM-REPO:END -->
#>

# -------- CONFIG --------
$githubUser = "Knoph1"
$readmePath = "./README.md"

# -------- FETCH REPOS --------
Write-Output "Fetching repositories for $githubUser ..."
$repos = Invoke-RestMethod "https://api.github.com/users/$githubUser/repos?per_page=100"

if (-not $repos) {
    Write-Error "No repositories found for user $githubUser."
    exit 1
}

# Pick a random repo
$randomRepo = $repos | Get-Random

# -------- BUILD MARKDOWN --------
$repoName = $randomRepo.name
$repoUrl  = $randomRepo.html_url
$repoDesc = if ($randomRepo.description) { $randomRepo.description } else { "No description provided." }

$snippet = @"
<!-- RANDOM-REPO:START -->
### 🎯 Random Featured Repository
- **[$repoName]($repoUrl)**  
  $repoDesc
<!-- RANDOM-REPO:END -->
"@

# -------- UPDATE README --------
$readmeContent = Get-Content $readmePath -Raw

if ($readmeContent -match "(?s)(<!-- RANDOM-REPO:START -->).*?(<!-- RANDOM-REPO:END -->)") {
    # Replace existing block
    $updatedReadme = $readmeContent -replace "(?s)(<!-- RANDOM-REPO:START -->).*?(<!-- RANDOM-REPO:END -->)", $snippet
}
else {
    # Append if markers missing
    $updatedReadme = $readmeContent + "`n`n" + $snippet
}

Set-Content -Path $readmePath -Value $updatedReadme -Encoding UTF8
Write-Output "README.md updated successfully with a random repo!"
