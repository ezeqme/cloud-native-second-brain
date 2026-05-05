---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Ayato Tokubi", "Sohan Kunkerkar", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27Nnx/cri-o-thriving-in-a-changing-world-one-container-at-a-time-ayato-tokubi-sohan-kunkerkar-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=CRI-O%3A+Thriving+in+a+Changing+World%2C+One+Container+at+a+Time+CNCF+KubeCon+2025
slides: []
status: parsed
---

# CRI-O: Thriving in a Changing World, One Container at a Time - Ayato Tokubi & Sohan Kunkerkar, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Ayato Tokubi, Sohan Kunkerkar, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27Nnx/cri-o-thriving-in-a-changing-world-one-container-at-a-time-ayato-tokubi-sohan-kunkerkar-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=CRI-O%3A+Thriving+in+a+Changing+World%2C+One+Container+at+a+Time+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre CRI-O: Thriving in a Changing World, One Container at a Time.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nnx/cri-o-thriving-in-a-changing-world-one-container-at-a-time-ayato-tokubi-sohan-kunkerkar-red-hat
- YouTube search: https://www.youtube.com/results?search_query=CRI-O%3A+Thriving+in+a+Changing+World%2C+One+Container+at+a+Time+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OjIZ-TH-4FA
- YouTube title: CRI-O: Thriving in a Changing World, One Container at a Time - Ayato Tokubi & Sohan Kunkerkar
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/cri-o-thriving-in-a-changing-world-one-container-at-a-time/OjIZ-TH-4FA.txt
- Transcript chars: 21296
- Keywords: container, actually, runtime, lessons, around, workloads, recently, feature, testing, change, credentials, future, upstream, features, containers, difference, cublet, artifacts

### Resumo baseado na transcript

I know it's a first session post lunch so I might expect few drowsy faces but don't worry I'll make sure to keep this session engaging. We have some interesting sessions and we have some interesting lessons and stories to talk about during the past one year of crow cryo development. If not, I'm going to talk about the introduction followed by the lessons that we learned over the past one year in the cryo development. is going to cover with the help of demo and towards the end we're going to talk about the future road map and having closing remarks and we'll open up for questions. For those who are not aware about cryo, cryo is a container runtime specifically designed for Kubernetes. It basically compliance with Kubernetes container runtime interface where you can see the acronym CRI and O stands for open container.

### Excerpt da transcript

Good afternoon everyone. Thank you so much for joining us today. I know it's a first session post lunch so I might expect few drowsy faces but don't worry I'll make sure to keep this session engaging. We have some interesting sessions and we have some interesting lessons and stories to talk about during the past one year of crow cryo development. As you might have seen and this is our day one at CubeCon. There are a couple of AI talks and you know AI is everywhere. So there's a different excitement on how AI is actually building things around Kubernetes. Let that be AI workloads, AI uh demos, AI tools and um the dust is settling down and we are seeing uh the real production workloads uh in in production. [clears throat] But at the same time we want to make sure that uh the business critical workloads are running fine and um they they have uh certain threshold and that's where the cryos philosophy is very simple one container at a time where we want to make sure that um things are running fine and at the same time we are also also supporting the growing needs of the business where you know the future things that we have.

So with this I want to introduce myself. I'm San Kerkar. I work at Red Hat as a senior software engineer. I'm one of the cryo maintainers and uh involved in the upstream signal initiatives. I recently started working on Q. It's a job manager for Kubernetes and which also intersects with AI initiative. So with me we have >> yeah uh I'm Ayatkobi. I'm also a software engineer in Red Hat and I'm also a reviewer in cryo. >> All right, thanks Aru. All right, so I'll quickly walk you through what we're going to cover today. Uh I know most of you are already familiar with cryo. If not, I'm going to talk about the introduction followed by the lessons that we learned over the past one year in the cryo development. Then we recently inducted one project in cryo community called cryo credential provider. We'll have some information about that and then we'll talk about some of the upstream signal initiatives that we are taking into consideration and the features we are building around that and then comes the most awaited feature that OCI volume uh image that AD is going to cover with the help of demo and towards the end we're going to talk about the future road map and having closing remarks and we'll open up for questions.

Sounds good. Perfect. Um can I get a quick show of hands? How many of you are aware about cryo? Perfect. For those who are not awa
