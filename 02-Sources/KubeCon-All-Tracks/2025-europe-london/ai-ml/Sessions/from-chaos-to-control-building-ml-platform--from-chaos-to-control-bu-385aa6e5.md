---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Platform Engineering"]
speakers: ["George Markhulia", "Steve Larkin", "Volvo Cars"]
sched_url: https://kccnceu2025.sched.com/event/1tx9h/from-chaos-to-control-building-ml-platform-george-markhulia-steve-larkin-volvo-cars
youtube_search_url: https://www.youtube.com/results?search_query=From+Chaos+To+Control%3A+Building+ML+Platform+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Chaos To Control: Building ML Platform - George Markhulia & Steve Larkin, Volvo Cars

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: George Markhulia, Steve Larkin, Volvo Cars
- Schedule: https://kccnceu2025.sched.com/event/1tx9h/from-chaos-to-control-building-ml-platform-george-markhulia-steve-larkin-volvo-cars
- Busca YouTube: https://www.youtube.com/results?search_query=From+Chaos+To+Control%3A+Building+ML+Platform+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Chaos To Control: Building ML Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9h/from-chaos-to-control-building-ml-platform-george-markhulia-steve-larkin-volvo-cars
- YouTube search: https://www.youtube.com/results?search_query=From+Chaos+To+Control%3A+Building+ML+Platform+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fnt3f8sWJLA
- YouTube title: From Chaos To Control: Building ML Platform - George Markhulia & Steve Larkin, Volvo Cars
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-chaos-to-control-building-ml-platform/fnt3f8sWJLA.txt
- Transcript chars: 28247
- Keywords: platform, production, cubeflow, components, support, working, common, create, projects, little, process, functionality, notebook, running, workloads, provide, already, without

### Resumo baseado na transcript

Uh today we're going to talk about Abacus, which is the platform we've built internally at Volvo. So today anyone just within a couple of minutes can onboard to ML platform spin up notebook server start validating the idea and uh without you know approvals without any waiting times without the man in the middle and uh since we've built it on This gives an overview of the type of scale at which we're working in our company. People were working either individually or in small teams, often solving the same problem over and over again. We've led people into common practices without being too rigid and we are able to solve common problems once such as the integration into the company's network while um following the prescribed security standards. The first mile which involves on boarding to the platform and creating new projects during day-to-day usage which is either producing insights or training ML models and then the last mile in which people can take their trained ML model into production and then continuously monitor its performance.

### Excerpt da transcript

Hello. Can you guys hear us? Yeah. All right. Great. Yeah. Hi everyone. My name is George. I'm engineering manager in ML platform team at Volc Cars. This is my colleague Steve. Hello. Uh today we're going to talk about Abacus, which is the platform we've built internally at Volvo. So today anyone just within a couple of minutes can onboard to ML platform spin up notebook server start validating the idea and uh without you know approvals without any waiting times without the man in the middle and uh since we've built it on top of Kubernetes and cloud native stack we thought this would be a perfect venue to share our learnings with you and u I'll hand it over to Steve to talk a little bit more about about the platform. Okay, thanks George. So this is our technology stack. Um the platform itself, Abacus is the top layer here and these are the components that we're going to talk more about today. However, before we start, we'd like to acknowledge the other developer platforms at Volvo Cars on which we've built.

Most notably, as a small team, we benefit greatly from the common enterprise container platform. This is a common codebase which deploys a number of Volvo cars Kubernetes clusters running a myriad of the company's workloads. This allows us to focus on our primary concern which is ML. As you can see, we're fond of open source and cloudnative technologies. And Abacus is built on the Qflow ecosystem. Uh we've added other products here to either complement Qflow or to integrate with the corporate network at Volvo. So let's set some context first by looking at some numbers. This gives an overview of the type of scale at which we're working in our company. The highlights here are that we have approximately 200 monthly active users. We have been running production workloads for around three years now. including some at the start on a non-production cluster which wasn't great. But the figures that we are most proud of here are those around the community. So we use Slack for both announcements and for support.

We believe in transparency and so we solve our support issues out in the open and it's the engineers who build the platform who are talking to the users. So we don't have any first or second line support. Um this is really good because it creates a bond between the engineers and between the users. So we see that some users they even help out with the support requests of others. We also have 48 contributors to our our inner sourced repo and we promote tha
