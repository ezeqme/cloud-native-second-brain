---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Cici Huang", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2qF/declarative-everything-cici-huang-google
youtube_search_url: https://www.youtube.com/results?search_query=Declarative+Everything+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Declarative Everything - Cici Huang, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Chicago
- Speakers: Cici Huang, Google
- Schedule: https://kccncna2023.sched.com/event/1R2qF/declarative-everything-cici-huang-google
- Busca YouTube: https://www.youtube.com/results?search_query=Declarative+Everything+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Declarative Everything.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qF/declarative-everything-cici-huang-google
- YouTube search: https://www.youtube.com/results?search_query=Declarative+Everything+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rFaWmd7Y7i0
- YouTube title: Declarative Everything - Cici Huang, Google
- Match score: 0.79
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/declarative-everything/rFaWmd7Y7i0.txt
- Transcript chars: 28781
- Keywords: validation, declarative, policy, constraints, resource, mentioned, native, earlier, called, effort, familiar, validations, another, everyone, release, thanks, working, upstream

### Resumo baseado na transcript

hi everyone thank you for being here today and uh let's just get the talk started first a little bit about myself uh my name is CC hang and I'm currently working at Google as a software engineer and uh I have been contributing directly to kuity Upstream for a couple years and cross multiple s for those who are not familiar with kuity Upstream Community s is short for um special interest group and I started at the City Club writer and W the contributor award there and then

### Excerpt da transcript

hi everyone thank you for being here today and uh let's just get the talk started first a little bit about myself uh my name is CC hang and I'm currently working at Google as a software engineer and uh I have been contributing directly to kuity Upstream for a couple years and cross multiple s for those who are not familiar with kuity Upstream Community s is short for um special interest group and I started at the City Club writer and W the contributor award there and then I I released kuity 127 as the uh release manager which is the previous release and I'm also a contributor in Sig API Machinery with the focus on the extensible uh features and recently uh I'm leading the S related work there and which we're going to talk about little bit in our next um slides maybe so the topic is declarative everything and uh what's going to be covered today so we are first begin with the declarative nature of communities and uh uh then talk about the uh notable me missing pieces inside declarative apis and talking about all the improvements we did and plan to do and then the future plan at the end so let's start with the declar nature of communities but first let's begin with the very basic concept of declarative versus imperative I know most of you might already familiar with the concept but in short words declarative is when you see what you want while on imperative is when you see how to get what you want so let's take a look at example of a costal sampling station I just assume everyone love the free food there so s would love to make sure there are always six samples on the tree and for doing it uh imperatively uh we maybe periodically check the number of the samples on the tree and if the number doesn't match what we want we make adjustments for example if it's empty we just make six samples and put them on the tree if it's more we just take off the extra while the declarative way would be to State the desired state which is um seven having like six one samples on the tree and uh you can rely on system to do the right things for you and you don't need to worry about how the system ensures the desired state to maintain throughout a time so how it can achieve the Inc is you just specify your desired state with a configuration file like this everyone familiar with yarm and after submitted to communities Community would perform all the sample monitoring and adjustment for you in a control Loop which we also call it a Reconciliation Loop so what's the the benefit of th
