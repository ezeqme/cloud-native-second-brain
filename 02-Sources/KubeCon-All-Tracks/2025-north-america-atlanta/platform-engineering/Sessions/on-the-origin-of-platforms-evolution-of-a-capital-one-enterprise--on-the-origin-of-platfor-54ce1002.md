---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Bradley Whitfield", "Jacob Walden", "Capital One"]
sched_url: https://kccncna2025.sched.com/event/27FbV/on-the-origin-of-platforms-evolution-of-a-capital-one-enterprise-platform-bradley-whitfield-jacob-walden-capital-one
youtube_search_url: https://www.youtube.com/results?search_query=On+the+Origin+of+Platforms%3A+Evolution+of+a+Capital+One+Enterprise+Platform+CNCF+KubeCon+2025
slides: []
status: parsed
---

# On the Origin of Platforms: Evolution of a Capital One Enterprise Platform - Bradley Whitfield & Jacob Walden, Capital One

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Bradley Whitfield, Jacob Walden, Capital One
- Schedule: https://kccncna2025.sched.com/event/27FbV/on-the-origin-of-platforms-evolution-of-a-capital-one-enterprise-platform-bradley-whitfield-jacob-walden-capital-one
- Busca YouTube: https://www.youtube.com/results?search_query=On+the+Origin+of+Platforms%3A+Evolution+of+a+Capital+One+Enterprise+Platform+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre On the Origin of Platforms: Evolution of a Capital One Enterprise Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FbV/on-the-origin-of-platforms-evolution-of-a-capital-one-enterprise-platform-bradley-whitfield-jacob-walden-capital-one
- YouTube search: https://www.youtube.com/results?search_query=On+the+Origin+of+Platforms%3A+Evolution+of+a+Capital+One+Enterprise+Platform+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BY-mQH9VKAo
- YouTube title: On the Origin of Platforms: Evolution of a Capital One Enterpris... Bradley Whitfield & Jacob Walden
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/on-the-origin-of-platforms-evolution-of-a-capital-one-enterprise-platf/BY-mQH9VKAo.txt
- Transcript chars: 33475
- Keywords: platform, started, clusters, cluster, network, support, little, platforms, tenants, ultimately, application, evolution, management, control, pressures, external, actually, pretty

### Resumo baseado na transcript

Uh first I want to say thanks to KubeCon for giving us this opportunity today but also thanks thank you to all of you for coming out to see our talk. I am a distinguished engineer in our platform engineering excellence space. this this tree or this platform um it it was built to solve a specific problem and had a quick and iterative feedback loop and early so it adapted to its environment and grew much more stronger through organic adoption. uh as we started to grow the documentation that we decided not to not to create meant that the tenant teams then had to interact with us for every problem that they had. We knew that there were opportunities to optimize in our current stance, but we knew we were going to Kubernetes. [laughter] Um, after those two incidents, for the next couple weeks, your tenants probably think everything is a platform problem, right?

### Excerpt da transcript

Uh first I want to say thanks to KubeCon for giving us this opportunity today but also thanks thank you to all of you for coming out to see our talk. Uh my name is Brad Whitfield. I am a distinguished engineer in our platform engineering excellence space. Uh and I'm Jake Walden. I'm a technical product owner within our engineering excellence organization at Capital 1 and I [clears throat] lead a large team that supports a very large multi-tenant uh compute platform built on top of Kubernetes. Um, you know, we've been building platforms since 2018 and today we want to talk about the natural evolution of platforms using our platform as an example. Today you'll hear about the environmental pressures you can expect to find in any platform's journey and the adaptations required to survive. When we think about platform evolution, we think of artificial and natural selection. Artificial selection is kind of like that tree that you see here on the left. It's recently been planted, but it's its trunk is straight, but if there were a strong wind to come through, it might not get right over without those supports.

We compare that to an enterprise platform built out of declaration. It might be built directly to exact specifications, but it hasn't been hardened by the adaptations of its environment. Your workload may even have to adapt to the platform to run there. take that in conjunction with a natural selection, right? The the tree there on the right. Um, this tree has been subjected to natural pressures over a long period of time. It's adapted to its environment. Sure, it's growing a little bit more slowly. It's not as picturesque, but its roots are very deep and resilient. Um, and we compare that to a platform that started in a small corner of your organization, right? this this tree or this platform um it it was built to solve a specific problem and had a quick and iterative feedback loop and early so it adapted to its environment and grew much more stronger through organic adoption. So we're a little biased because Dragon platform was built uh in in much the same way. Uh I've already said it but our the name of our internal platform is called Dragon.

Uh it's an it's a multi-tenant compute platform that we originally built to support just microservices but have since expanded to support advanced use cases with a namespace as a service tendency model. We've even even begun managing resources outside the cluster by leveraging controllers. During this talk we'll t
