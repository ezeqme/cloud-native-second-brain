---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Unclassified"
themes: ["AI ML", "GitOps Delivery"]
speakers: ["Michael Medellin", "Gordon Tillman", "Department of Defense"]
sched_url: https://kccnceu2021.sched.com/event/iE2o/how-dod-uses-k8s-and-flux-to-achieve-compliance-and-deployment-consistency-michael-medellin-gordon-tillman-department-of-defense
youtube_search_url: https://www.youtube.com/results?search_query=How+DoD+Uses+K8s+and+Flux+to+Achieve+Compliance+and+Deployment+Consistency+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How DoD Uses K8s and Flux to Achieve Compliance and Deployment Consistency - Michael Medellin & Gordon Tillman, Department of Defense

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[GitOps Delivery]]
- País/cidade: Virtual / Virtual
- Speakers: Michael Medellin, Gordon Tillman, Department of Defense
- Schedule: https://kccnceu2021.sched.com/event/iE2o/how-dod-uses-k8s-and-flux-to-achieve-compliance-and-deployment-consistency-michael-medellin-gordon-tillman-department-of-defense
- Busca YouTube: https://www.youtube.com/results?search_query=How+DoD+Uses+K8s+and+Flux+to+Achieve+Compliance+and+Deployment+Consistency+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How DoD Uses K8s and Flux to Achieve Compliance and Deployment Consistency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2o/how-dod-uses-k8s-and-flux-to-achieve-compliance-and-deployment-consistency-michael-medellin-gordon-tillman-department-of-defense
- YouTube search: https://www.youtube.com/results?search_query=How+DoD+Uses+K8s+and+Flux+to+Achieve+Compliance+and+Deployment+Consistency+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ewCnqDgewMg
- YouTube title: How DoD Uses K8s & Flux to Achieve Compliance & Deployment Consistency - M. Medellin & G. Tillman
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-dod-uses-k8s-and-flux-to-achieve-compliance-and-deployment-consist/ewCnqDgewMg.txt
- Transcript chars: 25672
- Keywords: cluster, flux, actually, around, application, deploy, deployment, software, running, mission, environment, infrastructure, clusters, capability, platform, resources, engineering, gordon

### Resumo baseado na transcript

hey everyone good morning good afternoon wherever in the world you may be uh i'm michael medellin i am the director of engineering for a software engineering unit inside the air force called kessel run uh and joining me today is gordon who will introduce himself hi folks um my name is gordon tillman i'm a principal engineer with f9 and have been working with kestrel run for almost a year now awesome thank you gordon today we're going to spend about 20 25 minutes or so talking to everyone

### Excerpt da transcript

hey everyone good morning good afternoon wherever in the world you may be uh i'm michael medellin i am the director of engineering for a software engineering unit inside the air force called kessel run uh and joining me today is gordon who will introduce himself hi folks um my name is gordon tillman i'm a principal engineer with f9 and have been working with kestrel run for almost a year now awesome thank you gordon today we're going to spend about 20 25 minutes or so talking to everyone about how the department of defense is using kubernetes and flux uh to achieve our compliance and deployment consistency that we're looking for um in our efforts to develop the capabilities that our users are looking from us from us on a day-to-day basis uh just you know i you know coming into context i want to make sure i can explain a bit more about what customer running is and what we're doing um our vision is to deliver combat capability that can sense and respond to conflict in any domain any time and anywhere uh we are part of the mission just as much as uh the exercises and operations that go on with flying planes around the world or flying aircraft or um you know driving aircraft carriers around the world uh we are we are building the capability necessary for the air men and women uh who serve the united states and our coalition partners uh to win the next war and the software teams both myself and gordon on the teams that it's working on the platform and also our application teams who take dependency on our work are shipping that software every day to our users around the world so we want to take a time to kind of just brief you a little bit on castle one and that mission overall um so if you dive into it what really is castle run uh kessel run is an acquisition development environment so uh traditionally within the government we have acquisition units that are going out and awarding contracts to software engineering teams and other teams to in other companies to actually build capability much like you would go out and build an airplane or a ship or some some type of capability or for the department of defense uh we would be acquiring that and we are part of that acquisitions uh uh infrastructure for the department of defense but uh internally we are very much a software engineering organization um you know in kind of the buzz wordy term we're we're doing devsecops we're trying to unify a way to ship software to our users around the world um do it securely do it r
