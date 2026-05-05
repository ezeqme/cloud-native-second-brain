---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Experience"
themes: ["Networking"]
speakers: ["Beka Modebadze", "Google", "Christine Kim", "Isovalent at Cisco"]
sched_url: https://kccnceu2026.sched.com/event/2CW6b/navigating-the-gateway-api-maze-40+-implementations-55+-features-and-a-path-to-portability-beka-modebadze-google-christine-kim-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+the+Gateway+API+Maze%3A+40%2B+Implementations%2C+55%2B+Features%2C+and+a+Path+to+Portability+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Navigating the Gateway API Maze: 40+ Implementations, 55+ Features, and a Path to Portability - Beka Modebadze, Google & Christine Kim, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Beka Modebadze, Google, Christine Kim, Isovalent at Cisco
- Schedule: https://kccnceu2026.sched.com/event/2CW6b/navigating-the-gateway-api-maze-40+-implementations-55+-features-and-a-path-to-portability-beka-modebadze-google-christine-kim-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+the+Gateway+API+Maze%3A+40%2B+Implementations%2C+55%2B+Features%2C+and+a+Path+to+Portability+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Navigating the Gateway API Maze: 40+ Implementations, 55+ Features, and a Path to Portability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6b/navigating-the-gateway-api-maze-40+-implementations-55+-features-and-a-path-to-portability-beka-modebadze-google-christine-kim-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Navigating+the+Gateway+API+Maze%3A+40%2B+Implementations%2C+55%2B+Features%2C+and+a+Path+to+Portability+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aBoqH0wf4Yk
- YouTube title: Navigating the Gateway API Maze: 40+ Implementations, 55+ Features... Beka Modebadze & Christine Kim
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/navigating-the-gateway-api-maze-40-implementations-55-features-and-a-p/aBoqH0wf4Yk.txt
- Transcript chars: 29050
- Keywords: gateway, features, ingress, controller, controllers, pretty, cluster, version, release, feature, started, versions, another, inference, standard, resources, extension, coming

### Resumo baseado na transcript

Um, I think there might be a few more seats and a few more people coming in. It will be uploaded and the slides are online on the schedule uh website as well. It's also one of the most collaborative uh API designs in Kubernetes history. you know it's trying to match your desired state to what you want and also lastly it's not developed in core Kubernetes it's its own project which is really good because if you you know getting a keen versus getting a gapin I think it's It solved um a lot of problems that existed with the previous solutions and gateway API is definitely a huge improvement over what we had before. So his responsibility is setting up Kubernetes cluster for multiple tenants with various rules and accesses including the networking solution.

### Excerpt da transcript

Thank you so much for coming on the very last day. Not the last slot, but pretty close to it. Um, I think there might be a few more seats and a few more people coming in. But don't worry people outside. This was recorded on YouTube. It will be uploaded and the slides are online on the schedule uh website as well. Um, so yeah, I guess we'll get started. This is navigating the gateway API maze. >> Yeah, thank you for coming once again. I'm Becca. I work for the Google cloud. I mainly work on the GK gateway infrastructure and I'm also the release manager uh for the gateway API project. >> And I'm Christine. I am a software engineer at ISON at Cisco. I do some Selium stuff and some gateway API stuff. So yeah, so first off, probably for some of the beginners. All right. Um we're going to set some of the context a little bit of what why we're here at this point. So if you're not familiar, the ingress has been a stable core API out of Kubernetes and it was easy to use. You know, it was really great for HTTP traffic.

It was really easy to just declare something and then you got traffic coming into your cluster from outside. But there was some difficulties with that too. You also had no portability because everyone with the features it kind of got complex um because h the ingress API was so simple but then was as Kubernetes got more uh integrated in everyday life. Uh then it got more complex as we saw it. Um different features also led to different annotations and so declaring everything inside the annotations was a headache and a half. And then lastly one ingress object and many people touching the same object. It kind of led to some confusion. You know sometimes someone wants traffic to route to one way and then someone else did something else and then it's all broken. So that led to the development of gateway API which was I think around CubeCon San Diego. So a while ago and this was like the next generation load balancing API and furthermore the cherry on top ingress engineext was recently archived as of two days ago.

Yeah, still fresh. Um so this is now making the move to gateway API even more it makes more sense now. So this is the classic picture of gateway API. Um so yes next generation load balancing of L4 and L7. So not just HTTP route and now because it's been stable for a while there's now rich ecosystem supporting your migration to gateway API from ingress. It's also one of the most collaborative uh API designs in Kubernetes history. There's a lot of
