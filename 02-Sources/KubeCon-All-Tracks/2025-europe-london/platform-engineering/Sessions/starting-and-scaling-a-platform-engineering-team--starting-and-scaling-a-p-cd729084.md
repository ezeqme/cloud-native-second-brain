---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Camille Fournier", "Independent", "Ian Nowland", "Junction Labs"]
sched_url: https://kccnceu2025.sched.com/event/1txG8/starting-and-scaling-a-platform-engineering-team-camille-fournier-independent-ian-nowland-junction-labs
youtube_search_url: https://www.youtube.com/results?search_query=Starting+and+Scaling+a+Platform+Engineering+Team+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Starting and Scaling a Platform Engineering Team - Camille Fournier, Independent & Ian Nowland, Junction Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Camille Fournier, Independent, Ian Nowland, Junction Labs
- Schedule: https://kccnceu2025.sched.com/event/1txG8/starting-and-scaling-a-platform-engineering-team-camille-fournier-independent-ian-nowland-junction-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Starting+and+Scaling+a+Platform+Engineering+Team+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Starting and Scaling a Platform Engineering Team.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txG8/starting-and-scaling-a-platform-engineering-team-camille-fournier-independent-ian-nowland-junction-labs
- YouTube search: https://www.youtube.com/results?search_query=Starting+and+Scaling+a+Platform+Engineering+Team+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9lPp-6nJ8bI
- YouTube title: Starting and Scaling a Platform Engineering Team - Camille Fournier & Ian Nowland
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/starting-and-scaling-a-platform-engineering-team/9lPp-6nJ8bI.txt
- Transcript chars: 35988
- Keywords: platform, actually, product, application, engineering, software, engineers, company, customers, infrastructure, business, getting, important, stakeholders, together, platforms, operating, developers

### Resumo baseado na transcript

Okay, we've got a lot to talk about, so I'm just going to go ahead and jump in. I'm here with my co-author Ian Noland and we're here to talk about our book on platform engineering and specifically going through some of the some of the highlights on starting and scaling a platform team. And when you're a small company and you're a small team, this isn't so much of a problem. But as you start to scale and you have more applications and you have more glue code and you have more choices that you've made in different ways across the underlying infrastructure and you have maybe some pieces that you're you were supporting in sort you need to upgrade Kubernetes, you need to upgrade EKS and all of a sudden every application team is sputtering and scrambling, you need to do security patches, right? And so the time to start a platform engineering team is not when you've just started your company, but when you've scaled to the point where you're actually having problems with your glue, having problems with your shared shared infrastructure that isn't really being strategically managed.

### Excerpt da transcript

Check. Check. All right, there we go. Holy crap. Hey guys. Wow, nice crowd. Okay, we've got a lot to talk about, so I'm just going to go ahead and jump in. I know a few of you are still coming in. And uh there are a few empty seats here and there. So, uh you know, just uh let people let people in as you can. Uh so, good morning everyone. Very nice to see you all. My name is Camille Fornier. I'm here with my co-author Ian Noland and we're here to talk about our book on platform engineering and specifically going through some of the some of the highlights on starting and scaling a platform team. Uh just to give you a sense of the agenda for today, uh I'm going to kick us off and just talk about some basics. How should you think about when to start a platform team? How should you think about the types of people you want to have on that team? And then I'm going to really speedrun through a few things about scaling these teams and how that goes wrong and how the sort of execution process for platform engineering can go wrong.

Then I'm going to kick it over to Ian who is going to give you a case study on platform and uh you know his his uh experience sort of taking a team that he managed at data dog and actually turning it up and scaling it successfully. So, uh, CNCF is 9 years old. Let's be clear. I don't know what this 10y year thing is about. Kubernetes might be 10 years old, but CNCF is nine years old, and I have email evidence to prove it. Um, and in the nine years, we've had this incredible boom in the ecosystem, which is awesome, right? That's great. There's a reason that we've had this incredible ecosystem boom. It's so much easier to, you know, start new companies these days because you can get whatever kinds of sort of infrastructure support you need, whatever kinds of products you need. You can easily provision stuff in the cloud and just getting started is so so much easier than it was even 10 years ago, which is awesome. Um, and so you know, you're you're a new startup, you're a new green field application, you want to do something, you have your application, you throw some YAML and other things together, and you throw it in the cloud, and you're great.

Um, and in the process, of course, you create this glue code, this integration code, one-off automation, configuration, administrative tools, this, you know, this stuff that kind of binds the application to all of the underlying building blocks you've chosen to run it. Fine. Natural. No problem. Um
