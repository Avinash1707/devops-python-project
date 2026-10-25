stage('Test Docker Hub Authentication') {
    steps {
        withCredentials([
            usernamePassword(
                credentialsId: 'dockerhub-credentials-test',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_TOKEN'
            )
        ]) {
            powershell '''
                $ErrorActionPreference = "Stop"

                $user = $env:DOCKER_USER.Trim()
                $token = $env:DOCKER_TOKEN.Trim()

                Write-Output "Username received: $user"
                Write-Output "Token length: $($token.Length)"

                $docker = "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe"
                $config = Join-Path $env:WORKSPACE ".docker-auth-test"

                New-Item -ItemType Directory -Path $config -Force | Out-Null

                try {
                    $env:DOCKER_CONFIG = $config
                    $token | & $docker login --username $user --password-stdin

                    if ($LASTEXITCODE -ne 0) {
                        throw "Pipeline authentication test failed"
                    }

                    Write-Output "PIPELINE AUTHENTICATION TEST SUCCEEDED"
                }
                finally {
                    Remove-Item Env:DOCKER_CONFIG -ErrorAction SilentlyContinue
                    Remove-Item $config -Recurse -Force -ErrorAction SilentlyContinue
                }
            '''
        }
    }
}
