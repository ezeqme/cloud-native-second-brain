---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Hossein Salahi", "Liquid Reply"]
sched_url: https://kccncchn2025.sched.com/event/1x5k2/composable-platforms-modular-platform-engineering-with-kratix-and-backstage-hossein-salahi-liquid-reply
youtube_search_url: https://www.youtube.com/results?search_query=Composable+Platforms%3A+Modular+Platform+Engineering+With+Kratix+and+Backstage+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Composable Platforms: Modular Platform Engineering With Kratix and Backstage - Hossein Salahi, Liquid Reply

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: China / Hong Kong
- Speakers: Hossein Salahi, Liquid Reply
- Schedule: https://kccncchn2025.sched.com/event/1x5k2/composable-platforms-modular-platform-engineering-with-kratix-and-backstage-hossein-salahi-liquid-reply
- Busca YouTube: https://www.youtube.com/results?search_query=Composable+Platforms%3A+Modular+Platform+Engineering+With+Kratix+and+Backstage+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Composable Platforms: Modular Platform Engineering With Kratix and Backstage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5k2/composable-platforms-modular-platform-engineering-with-kratix-and-backstage-hossein-salahi-liquid-reply
- YouTube search: https://www.youtube.com/results?search_query=Composable+Platforms%3A+Modular+Platform+Engineering+With+Kratix+and+Backstage+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Cvib3yHxMik
- YouTube title: Composable Platforms: Modular Platform Engineering With Kratix and Backstage - Hossein Salahi
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/composable-platforms-modular-platform-engineering-with-kratix-and-back/Cvib3yHxMik.txt
- Transcript chars: 25997
- Keywords: platform, backstage, promise, instance, create, engineering, developers, focusing, cratics, developer, resources, already, cluster, deploy, platforms, capabilities, resource, concept

### Resumo baseado na transcript

Thank you everyone for joining me and u today we are going to talk about creating a composable and modular platform. We will talk about in depth what is about but um it's another platform engineering talk focusing on developer experience. They do and they I mean they design they build manage services in our companies based on on-prem infrastructure or cloud infrastructure. One team is focusing on cyber security, the other team is focusing on monitoring, infrastructure, database, DVAs etc. This is the way doesn't matter which API is it Kubernetes API is it API that you wrote by yourself. So this is uh one of the reference architectures uh from the platform engineering community.

### Excerpt da transcript

Thank you everyone for joining me and u today we are going to talk about creating a composable and modular platform. We will talk about in depth what is about but um it's another platform engineering talk focusing on developer experience. If you just uh watch the the previous talk we're going to have lots of overlapping topics. I will try to speed up a bit but why def experience? Uh it has been uh the main talking point of last few years. Uh why it matters, why it's important because it's all about how we uh enable developers to use our platforms. We don't build platforms a platform engineer for fun. Yeah, don't get me wrong, we build platform because we love it, but we build it for developers to deploy their applications recently deploy their AI models and etc. So it's about improving them to boost their productivity and uh to also improve the software development life cycle and shorten the time to the market. Uh shortly about myself uh my name is Hussein Salah. I'm a consultant in my daily job.

I work uh as a tech lead and uh yeah last few years I've been contributing to the open open source community and that's what I do. uh as a hobby next to my job. So today we are going to take a look at what are the current challenges in cloud native uh ecosystem and what developers are facing these days uh based on the current uh created platforms. We will quickly recap what we know about platform engineering and internal developer platforms. We will take a look at how community took a step to create reference implementation for IDPS. If we'll take a look at two main projects in this area. One is focusing on how to build capabilities background uh backend services uh by the platform engineer. The other one is focusing more on the making those services those uh backend uh processes more visible to the to the uh end user via backstage. And we will take a look how we can mix these two powerful uh projects to make an a framework that helps both platform engineers and both developers to achieve uh a more reliable, maintainable and reusable platforms.

Last but not least, we will have a demo. So let's take a look at what we know from the past from the history. This is typical DevOps model we know from our companies from our organization we are working for. So at the right side we have admin teams. They do and they I mean they design they build manage services in our companies based on on-prem infrastructure or cloud infrastructure. They use infrastructure as code or oth
