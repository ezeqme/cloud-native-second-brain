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
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Jim Bugwadia", "Charles-Edouard Brétéché", "Nirmata"]
sched_url: https://kccncna2025.sched.com/event/27fXo/kyverno-everywhere-simplifying-unified-policy-as-code-jim-bugwadia-charles-edouard-breteche-nirmata
youtube_search_url: https://www.youtube.com/results?search_query=Kyverno+Everywhere%3A+Simplifying+Unified+Policy+as+Code+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kyverno Everywhere: Simplifying Unified Policy as Code - Jim Bugwadia & Charles-Edouard Brétéché, Nirmata

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Jim Bugwadia, Charles-Edouard Brétéché, Nirmata
- Schedule: https://kccncna2025.sched.com/event/27fXo/kyverno-everywhere-simplifying-unified-policy-as-code-jim-bugwadia-charles-edouard-breteche-nirmata
- Busca YouTube: https://www.youtube.com/results?search_query=Kyverno+Everywhere%3A+Simplifying+Unified+Policy+as+Code+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kyverno Everywhere: Simplifying Unified Policy as Code.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27fXo/kyverno-everywhere-simplifying-unified-policy-as-code-jim-bugwadia-charles-edouard-breteche-nirmata
- YouTube search: https://www.youtube.com/results?search_query=Kyverno+Everywhere%3A+Simplifying+Unified+Policy+as+Code+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N5Lw9Mj_uW8
- YouTube title: Kyverno Everywhere: Simplifying Unified Policy as Code - Jim Bugwadia & Charles-Edouard Brétéché
- Match score: 0.821
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kyverno-everywhere-simplifying-unified-policy-as-code/N5Lw9Mj_uW8.txt
- Transcript chars: 23267
- Keywords: policy, policies, kivero, admission, validating, envoy, course, started, cluster, authorization, resources, request, finally, server, security, controllers, controller, engine

### Resumo baseado na transcript

And I know that sounds like a mouthful, but today what we want to do is go over a little bit about the history of the project, why we started Kerno, why this matters for Kubernetes, and more importantly, what's the future of policy and governance for Kubernetes, as well as other platform engineering concerns. So just quick introductions, I'm Jim Beuia, co-founder, CEO at Nermata. Now of course like as we were mentioning with Kubernetes you have different roles you have different concerns all in the same YAML configurations and policies really bring together a lot of these roles right so why Kivero there's options like Kivero started maybe a The language matters and as Kubernetes admins, a lot of us have we learn, you know, Kubernetes constructs. So what we wanted to do was make policies very native to Kubernetes, make it very frictionless and seamless for administrators or developers or even security teams. So one of the main things even in hallway conversations and talking to folks that I've heard is although there's other admission controllers your security tool might have an admission controller maybe there's other options in the space kivero makes it really really simple for

### Excerpt da transcript

Kivero's mission is to simplify Kubernetes policy and governance. And I know that sounds like a mouthful, but today what we want to do is go over a little bit about the history of the project, why we started Kerno, why this matters for Kubernetes, and more importantly, what's the future of policy and governance for Kubernetes, as well as other platform engineering concerns. So just quick introductions, I'm Jim Beuia, co-founder, CEO at Nermata. We're one of the you know main contributors. We also created Kivero and are very active in the community. >> And uh I'm Char. I joined the Kano organization as a Kano maintainer three years ago and I work at Neata with the creators of Keano. So thanks Jim. >> Awesome. All right. So let's start with why do we need policies to begin with right? So one of the things which I find very interesting about Kubernetes is if you look at the history of computing right it'll last like even going back 30 or so years. We talked a lot about DevOps and DevSec Ops and other things but Kubernetes is one of the first platforms that really brings together developers, operators and security teams.

You actually have YAML manifest whether you like YAML or not. You have configurations which are super detailed very you know specific in terms of every aspects of concerns for each of these roles. So the question always becomes how do you now manage policies or how do you manage you know uh across all of these roles and how do you share information in an efficient manner. Now obviously we could share things you know like by conversation or by tickets or other means of communication but what we know best is you know configuration. So of course like creating policies as configuration or policy as code also starts making a lot of sense. So that's really what kivero was intended for. It's you know I kind of think of it policies in general just as a way of communicating or defining ways that we you know agree to a certain set of rules. Now of course like as we were mentioning with Kubernetes you have different roles you have different concerns all in the same YAML configurations and policies really bring together a lot of these roles right so why Kivero there's options like Kivero started maybe a couple of years after other policy engines in the space like open policy agent and others that you might know and you know we thought long and hard before we created Kerno we spoke to a lot of folks and what we found is that although almost everybody unde
