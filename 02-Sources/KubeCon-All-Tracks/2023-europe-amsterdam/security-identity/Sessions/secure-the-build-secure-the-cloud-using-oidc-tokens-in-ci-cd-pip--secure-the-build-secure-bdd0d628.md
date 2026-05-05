---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Alex Ilgayev", "Elad Pticha", "Cycode"]
sched_url: https://kccnceu2023.sched.com/event/1HyRY/secure-the-build-secure-the-cloud-using-oidc-tokens-in-cicd-pipelines-alex-ilgayev-elad-pticha-cycode
youtube_search_url: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+Secure+the+Build%2C+Secure+the+Cloud%3A+Using+OIDC+Tokens+in+CI%2FCD+Pipelines+CNCF+KubeCon+2023
slides: []
status: parsed
---

# 🦝 Secure the Build, Secure the Cloud: Using OIDC Tokens in CI/CD Pipelines - Alex Ilgayev & Elad Pticha, Cycode

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alex Ilgayev, Elad Pticha, Cycode
- Schedule: https://kccnceu2023.sched.com/event/1HyRY/secure-the-build-secure-the-cloud-using-oidc-tokens-in-cicd-pipelines-alex-ilgayev-elad-pticha-cycode
- Busca YouTube: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+Secure+the+Build%2C+Secure+the+Cloud%3A+Using+OIDC+Tokens+in+CI%2FCD+Pipelines+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre 🦝 Secure the Build, Secure the Cloud: Using OIDC Tokens in CI/CD Pipelines.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyRY/secure-the-build-secure-the-cloud-using-oidc-tokens-in-cicd-pipelines-alex-ilgayev-elad-pticha-cycode
- YouTube search: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+Secure+the+Build%2C+Secure+the+Cloud%3A+Using+OIDC+Tokens+in+CI%2FCD+Pipelines+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iS-KvD6huWc
- YouTube title: Secure the Build, Secure the Cloud: Using OIDC Tokens in CI/CD Pipelines- Alex Ilgayev & Elad Pticha
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/secure-the-build-secure-the-cloud-using-oidc-tokens-in-ci-cd-pipelines/iS-KvD6huWc.txt
- Transcript chars: 21731
- Keywords: identity, github, tokens, gitlab, popular, authentication, secret, access, account, create, security, provider, manager, secrets, docker, workflow, simple, nowadays

### Resumo baseado na transcript

hello everyone I'm Alex and today's topic will be how to secure both your build and your Cloud by utilizing IDC tokens in your pipeline so let's start with the agenda before diving into any solution let's start with understanding the the problem let's start with discovering how modern sdlc pipelines are working how they are built and why there could be a possible issue with the cloud Authentication after understanding the problem and that ODC could be the solution to several of these issues we'll understand what is oledc

### Excerpt da transcript

hello everyone I'm Alex and today's topic will be how to secure both your build and your Cloud by utilizing IDC tokens in your pipeline so let's start with the agenda before diving into any solution let's start with understanding the the problem let's start with discovering how modern sdlc pipelines are working how they are built and why there could be a possible issue with the cloud Authentication after understanding the problem and that ODC could be the solution to several of these issues we'll understand what is oledc open ID connect what are the its concept and how it can be used in cicd environments then we will build some really simple real world scenario which will go through the slides and finally we'll show you several demos and how we can you can build a more secure authentication to your Cloud environments using IDC I'm a head of security research in scicode previously I led I led the Marvel research team at a checkpoint where we're doing a lot of reverse engineering for the complex pieces of malware discovering a campaigns for a cyber crime and apts and nowadays inside code we're a researching vulnerabilities in software supply chain security and hopefully also mitigations for these vulnerabilities I'm security research at cycode used to do API security and iots before I came to recycle okay so in short the cycle road is a cyber security company based in a Tel Aviv that they are doing complete software supply chain security for organizations and in all various of kinds of security both in searching hard-coded secrets in your code securing your pipeline misconfigurations Cloud security and many more so let's start with the problem so after investigating and understanding how most of the modern sdlc pipelines works we can divide it to several several parts the first is the developer whether it's a contributor a maintainer collaborator doesn't matter instead the actual person that pushes the code the second part is the SCM system Source Control Management mostly a git based it could be a GitHub gitlab bitbucket Azure devops doesn't matter and and most of the code is pushed through one of two ways either a direct push which is usually not recommended or through a pull request or marriage request depends on the system where you suggest a piece of code that should be reviewed by multiple developers and before it's been pushed to the to your Cod Repository and whenever uh you push a new piece of code usually which is the most important part in the rec
