---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Karan Thukral", "Harvey Xia", "Reddit"]
sched_url: https://kccncna2024.sched.com/event/1i7nY/evolving-reddits-infrastructure-via-principled-platform-abstractions-karan-thukral-harvey-xia-reddit
youtube_search_url: https://www.youtube.com/results?search_query=Evolving+Reddit%E2%80%99s+Infrastructure+via+Principled+Platform+Abstractions+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Evolving Reddit’s Infrastructure via Principled Platform Abstractions - Karan Thukral & Harvey Xia, Reddit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Karan Thukral, Harvey Xia, Reddit
- Schedule: https://kccncna2024.sched.com/event/1i7nY/evolving-reddits-infrastructure-via-principled-platform-abstractions-karan-thukral-harvey-xia-reddit
- Busca YouTube: https://www.youtube.com/results?search_query=Evolving+Reddit%E2%80%99s+Infrastructure+via+Principled+Platform+Abstractions+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Evolving Reddit’s Infrastructure via Principled Platform Abstractions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nY/evolving-reddits-infrastructure-via-principled-platform-abstractions-karan-thukral-harvey-xia-reddit
- YouTube search: https://www.youtube.com/results?search_query=Evolving+Reddit%E2%80%99s+Infrastructure+via+Principled+Platform+Abstractions+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ruto5Sak-jI
- YouTube title: Evolving Reddit’s Infrastructure via Principled Platform Abstractions - Karan Thukral & Harvey Xia
- Match score: 0.925
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/evolving-reddits-infrastructure-via-principled-platform-abstractions/ruto5Sak-jI.txt
- Transcript chars: 42870
- Keywords: cluster, clusters, infrastructure, platform, engineers, automation, control, reddit, extremely, engineer, spaces, reason, abstractions, resources, question, underlying, software, federation

### Resumo baseado na transcript

hello everyone uh thank you so much for joining us today uh I hope everyone's been having a great cubec con so far uh my name is Karen tal I work on the compute infrastructure team at Reddit and my name is Harvey Shaw and I also work on the compute infrastructure team uh before I get into the talk I just want to know the slides have been uploaded so in case anybody wants to follow along that way too so today we're going to dive into a retrospective

### Excerpt da transcript

hello everyone uh thank you so much for joining us today uh I hope everyone's been having a great cubec con so far uh my name is Karen tal I work on the compute infrastructure team at Reddit and my name is Harvey Shaw and I also work on the compute infrastructure team uh before I get into the talk I just want to know the slides have been uploaded so in case anybody wants to follow along that way too so today we're going to dive into a retrospective about how Reddit infrastructure has evolved over the past few years by particularly leaning into um platform abstractions and automation backed by a kubernetes control plane a quick overview for the agenda for today we're going to start this off by talking about the state of Reddit infrastructure back in 2022 which prompted most of this investment we're going to then dive into the foundational principles that we use to build our platform what we learned from it what hopefully you can take away and kind of where we're headed we should have time for questions towards the end of it but in case we don't have time both Harvey and I will hang around in the hallway in case anybody wants to like chat so before I get into the kind of the meat of the talk I want to pitch a thesis statement so um it toes just help connect the content together we believe that when companies reach a certain maturity they need platform abstractions to grow efficiently especially as they grow sorry operate efficiently especially as they grow and Reddit was at this inflection point in 2022 so throughout 2022 it was a big change for reddit reddit was growing quite significantly internally as an organization and externally as a product we're working towards an IPO uh and starting to expand our serving stack to be multi-regional with the end goal of being Global expansion the global expansion was both for better resiliency and reliability but also to improve the user experience for our International users um the we were also investing pretty heavily into our ads in ml stack and continue to do so today which is a pretty common theme across the rest of the tech industry as well and this came with an own set of scaling challenges we ended 2022 with about a 7 to1 ratio of application Engineers to infrastructure engineers and we started 2022 and ended the year with about 20 kubernetes clusters all largely unique but all in the same cloud in same region in order to understand the pitfalls of our infrastructure or Legacy infrastructure I want to use the
