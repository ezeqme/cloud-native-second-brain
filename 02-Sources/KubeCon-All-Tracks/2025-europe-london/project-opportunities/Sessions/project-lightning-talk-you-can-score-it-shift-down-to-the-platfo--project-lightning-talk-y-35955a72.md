---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Mathieu Benoit", "Core Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwp/project-lightning-talk-you-can-score-it-shift-down-to-the-platform-do-not-shift-left-to-the-developers-mathieu-benoit-core-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+You+Can+Score+It%21+Shift+Down+to+the+Platform.+Do+Not+Shift+Left+to+the+Developers.+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: You Can Score It! Shift Down to the Platform. Do Not Shift Left to the Developers. - Mathieu Benoit, Core Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Mathieu Benoit, Core Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwp/project-lightning-talk-you-can-score-it-shift-down-to-the-platform-do-not-shift-left-to-the-developers-mathieu-benoit-core-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+You+Can+Score+It%21+Shift+Down+to+the+Platform.+Do+Not+Shift+Left+to+the+Developers.+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: You Can Score It! Shift Down to the Platform. Do Not Shift Left to the Developers..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwp/project-lightning-talk-you-can-score-it-shift-down-to-the-platform-do-not-shift-left-to-the-developers-mathieu-benoit-core-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+You+Can+Score+It%21+Shift+Down+to+the+Platform.+Do+Not+Shift+Left+to+the+Developers.+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Nq_PgPKZHsc
- YouTube title: Project Lightning Talk: You Can Score It! Shift Down to the Platform. Do Not Shift... Mathieu Benoit
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-you-can-score-it-shift-down-to-the-platform-do/Nq_PgPKZHsc.txt
- Transcript chars: 5325
- Keywords: platform, developer, engineer, implementation, please, workload, cubecon, describe, radius, targeting, recipe, compose, deploy, provision, runtime, support, docker, contribute

### Resumo baseado na transcript

I'm uh very glad excited to represent the score project a sendox uh sandbox sorry CNCF project. So I'm representing the project the maintainer the community the contributor the user as well. the first step but now on the other end as platform engineer my goal is to support any deployment request of this file of this kind of file at scale. So here the goal is to bring what we call the score one of the score implementation and the score implementation is very much about hey are you targeting a docker runtime are you targeting a kubernetes runtime are you targeting flyio are you targeting another platform orchestrating this deployment yes sure I will support you and here you have a second opportunity as platform engineer as platform engineer you will be able to author and design wells supported golden path right and the goal is to say yeah sure you ask for radius and a DNS because you want to expose your workload previously sure let me write down the recipe with my cloud engineer security engineer let me write down the recipe to provision posgressql on docker compose maybe on kubernetes in the

### Excerpt da transcript

How are you doing? First day of CubeCon officially. Thank you for being here. I'm uh very glad excited to represent the score project a sendox uh sandbox sorry CNCF project. So I'm representing the project the maintainer the community the contributor the user as well. Um thank you for being here. So that for sure Kubernetes is a key component, key pieces and key piece of building a platform building what we call maybe an internal developer platform. But the reality is Kubernetes is not the platform itself, right? There is tools around that. There is tools to interact as an interface to deploy into this Kubernetes engine and platform. And there is also other tool CI/CD tool maybe other tool to u provision infrastructure and cloud infrastructure. So that's one thing. Another thing is maybe in your organization Kubernetes is not the only runtime. Maybe your developer would like to deploy their application on serverless for some reason on VM from some other reason. So let's imagine that um you have as a developer you describe your intent to deploy a workload.

So you could describe here via the workload specification the score workload specification here it's a score file and you say I have a workload I know the metadata I know some environment variable I know the port I want to expose my application from and to and I want at the very bottom of this file you could see that I will also describe the resources that I need is it in AWS is it in GCP Is it locally? I don't know. I don't know the platform, right? And I hope it's Kubernetes because Kubernetes is awesome. But as a developer, I don't know this technical detail, right? And that's where you could see line 17 and and and um below, I want a radius database. That's what I know. And please when someone will provision this radius database wherever the platform is wherever the environment dev staging production is please inject the necessary information to get the connection string that's what this file is about I'm just describing what I want right so that's the first step but now on the other end as platform engineer my goal is to support any deployment request of this file of this kind of file at scale.

Right? So here the goal is to bring what we call the score one of the score implementation and the score implementation is very much about hey are you targeting a docker runtime are you targeting a kubernetes runtime are you targeting flyio are you targeting another platform orchestrating this deployment yes
