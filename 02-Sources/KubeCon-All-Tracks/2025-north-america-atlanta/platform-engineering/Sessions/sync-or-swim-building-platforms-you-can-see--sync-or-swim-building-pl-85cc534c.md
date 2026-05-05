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
themes: ["AI ML", "Platform Engineering"]
speakers: ["Heather Lee", "Mike Cutsail", "Apple"]
sched_url: https://kccncna2025.sched.com/event/27FY4/sync-or-swim-building-platforms-you-can-see-heather-lee-mike-cutsail-apple
youtube_search_url: https://www.youtube.com/results?search_query=Sync+or+Swim%3A+Building+Platforms+You+Can+See+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sync or Swim: Building Platforms You Can See - Heather Lee & Mike Cutsail, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Heather Lee, Mike Cutsail, Apple
- Schedule: https://kccncna2025.sched.com/event/27FY4/sync-or-swim-building-platforms-you-can-see-heather-lee-mike-cutsail-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Sync+or+Swim%3A+Building+Platforms+You+Can+See+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sync or Swim: Building Platforms You Can See.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FY4/sync-or-swim-building-platforms-you-can-see-heather-lee-mike-cutsail-apple
- YouTube search: https://www.youtube.com/results?search_query=Sync+or+Swim%3A+Building+Platforms+You+Can+See+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g70y40Qk7bs
- YouTube title: Sync or Swim: Building Platforms You Can See - Heather Lee & Mike Cutsail, Apple
- Match score: 0.815
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sync-or-swim-building-platforms-you-can-see/g70y40Qk7bs.txt
- Transcript chars: 25060
- Keywords: platform, resources, cluster, argo, metrics, crossplane, observability, function, actually, traces, claims, composition, trace, infrastructure, dashboard, resource, managed, changes

### Resumo baseado na transcript

You can see >> we have apparently uh the diehard CubeCon, Cloud Native Con crowd here. Uh we actually were curious though about what our distribution here was. Um and then we'll go and walk through some demos to illustrate how we might address these issues from both the platform and user perspective and for the platform operator. Now we'll give a brief overview of the components we use to build out the demo platform. Crossplane extends Kubernetes to manage any infrastructure through APIs. Managed resources are onetoone mappings of actual infrastructure as Kubernetes objects.

### Excerpt da transcript

Hello everyone. Welcome to Sync or Swim building platforms. You can see >> we have apparently uh the diehard CubeCon, Cloud Native Con crowd here. 5:45. Uh we're really excited. Uh we actually were curious though about what our distribution here was. So if you could do a little audience participation survey, how many platform engineers in the room? Okay, good representation. How about uh end users of platforms? All right. Uh we have content for both audiences. We're actually hoping to make the platform end user experience better. And certainly uh platform engineering is hard enough when it's hard to see what's happening in the platform. So uh I'll tell us tell you a little bit about us. Uh my I'm Mike Cutsale. I'm a software engineer at Apple. I've worked on infrastructure and connectivity solutions for about 10 years at Apple. And Heather. >> Hi everyone. Nice to meet you. Um, I'm on the same team as Mike working on infrastructure, but prior to working on infrastructure, I was an application engineer. So, I care a lot about building platforms that you can see.

And also, by the way, thank you everyone for coming at 5:45 p.m. to see our talk. So, what are we hoping that you'll take away from this talk today? Uh, first, we want to give you a shared understanding of the observability challenges that platform teams face. We'll describe some of the unique plat problems that emerge when you're building platforms for developers. We'll be talking about making those platforms visible to two core audiences, platform engineers and platform end users. Second, we're going to show you the actual observability signals that you can produce from a real platform stack using a mini version of a production stack. And third, we'll share best practices for composing these instrumentation patterns together. The goal isn't visibility for visibility's sake. It's about rapidly assessing platform health when something goes wrong and only surfacing the data that matters for the right audience. By the end of this talk, you should be able to go back to your platform and start applying some of these techniques.

So, let's start by talking about the agenda. Uh this is what we'll be covering today. First, we'll walk through our tech stack. uh we used to build the demo we'll be showing today. Next, we'll discuss the issues we might see arise from using this kind of platform. Um and then we'll go and walk through some demos to illustrate how we might address these issues from both the plat
