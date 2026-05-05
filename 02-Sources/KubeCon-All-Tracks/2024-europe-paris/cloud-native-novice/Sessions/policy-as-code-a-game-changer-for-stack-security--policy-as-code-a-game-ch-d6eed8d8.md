---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["Security"]
speakers: ["Raz Cohen", "Permit.io"]
sched_url: https://kccnceu2024.sched.com/event/1Yhg6/policy-as-code-a-game-changer-for-stack-security-raz-cohen-permitio
youtube_search_url: https://www.youtube.com/results?search_query=Policy+as+Code%3A+A+Game-Changer+for+Stack+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Policy as Code: A Game-Changer for Stack Security - Raz Cohen, Permit.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Raz Cohen, Permit.io
- Schedule: https://kccnceu2024.sched.com/event/1Yhg6/policy-as-code-a-game-changer-for-stack-security-raz-cohen-permitio
- Busca YouTube: https://www.youtube.com/results?search_query=Policy+as+Code%3A+A+Game-Changer+for+Stack+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Policy as Code: A Game-Changer for Stack Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhg6/policy-as-code-a-game-changer-for-stack-security-raz-cohen-permitio
- YouTube search: https://www.youtube.com/results?search_query=Policy+as+Code%3A+A+Game-Changer+for+Stack+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4-qmiGT31jY
- YouTube title: Policy as Code: A Game-Changer for Stack Security - Raz Cohen, Permit.io
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/policy-as-code-a-game-changer-for-stack-security/4-qmiGT31jY.txt
- Transcript chars: 28300
- Keywords: access, policy, control, authorization, understand, basically, application, document, security, trying, specific, authentication, important, enough, delete, folder, google, inside

### Resumo baseado na transcript

my name is Ras Goen um I hope you hear me well uh I'm the head of devops at permito and today I wanted to talk with you about policy as code about how it can actually change your your way that you basically look at your security all across your stuck um so stting from the devops from the infrastructure going through uh the back end maybe databases and also uh the front endend and we will start by actually understanding what authorization authentication Access Control means I will

### Excerpt da transcript

my name is Ras Goen um I hope you hear me well uh I'm the head of devops at permito and today I wanted to talk with you about policy as code about how it can actually change your your way that you basically look at your security all across your stuck um so stting from the devops from the infrastructure going through uh the back end maybe databases and also uh the front endend and we will start by actually understanding what authorization authentication Access Control means I will start by scaring you a bit uh why it is such an important thing and then we will understand how we can solve everything by polic as code it's not that simple but I will I will try to convince you that it's simple so let's start so first of all welcome everyone to cubec Paris I hope you're doing a good time here here for me it's amazing it's good food good weather so I'm doing good and there are a lot of I don't know interesting Comm companies here uh everyone is trying to integrate AI inside their product so it's nice to see actually how it's getting traction and I don't know getting some improvements through the time and eventually we all have one goal doesn't matter if you are devops doesn't matter if you are data analyst developer product manager we all have one simple goal and it's to get our application to production right and that can be simple but through the time we understand that there are a lot of small things that will make our life really miserable um but we did it we deployed our application to production we're super excited about it and now we need to understand what else we can just you know we made it but unfortunately this is not enough and most of the time we understand that deploying and you know making an iccd making a well performance uh code it's not enough and you guessed it right we always have this small pool request that says urgent security fixes um starting from vulnerabilities in our code or I don't know maybe other cloud misconfigurations and stuff like this um and this is nice um but this is not solving all the security issues that we have and we can talk about security again around the code maybe in the docker image or something like this but we can't forget the security inside our application so the first step that I'm going to talk about or the F first thing basically is authentication and authentication is something very very important because if you think about it maybe our code is very secured but maybe everyone can access my application maybe
