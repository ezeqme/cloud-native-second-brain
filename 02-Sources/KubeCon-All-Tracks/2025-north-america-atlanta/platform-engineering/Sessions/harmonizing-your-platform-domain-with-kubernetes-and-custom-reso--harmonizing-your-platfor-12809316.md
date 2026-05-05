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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Sebastien Blanc", "Port"]
sched_url: https://kccncna2025.sched.com/event/27Fa6/harmonizing-your-platform-domain-with-kubernetes-and-custom-resource-definitions-sebastien-blanc-port
youtube_search_url: https://www.youtube.com/results?search_query=Harmonizing+Your+Platform+Domain+With+Kubernetes+and+Custom+Resource+Definitions+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Harmonizing Your Platform Domain With Kubernetes and Custom Resource Definitions - Sebastien Blanc, Port

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Sebastien Blanc, Port
- Schedule: https://kccncna2025.sched.com/event/27Fa6/harmonizing-your-platform-domain-with-kubernetes-and-custom-resource-definitions-sebastien-blanc-port
- Busca YouTube: https://www.youtube.com/results?search_query=Harmonizing+Your+Platform+Domain+With+Kubernetes+and+Custom+Resource+Definitions+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Harmonizing Your Platform Domain With Kubernetes and Custom Resource Definitions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fa6/harmonizing-your-platform-domain-with-kubernetes-and-custom-resource-definitions-sebastien-blanc-port
- YouTube search: https://www.youtube.com/results?search_query=Harmonizing+Your+Platform+Domain+With+Kubernetes+and+Custom+Resource+Definitions+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=T_sMX_hxS8k
- YouTube title: Harmonizing Your Platform Domain With Kubernetes and Custom Resource Definitions - Sebastien Blanc
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/harmonizing-your-platform-domain-with-kubernetes-and-custom-resource-d/T_sMX_hxS8k.txt
- Transcript chars: 25015
- Keywords: platform, prompt, developers, custom, define, resource, engineering, operators, create, developer, domain, controller, seconds, self-service, cognitive, portal, course, prompts

### Resumo baseado na transcript

I know it's a bit hard after lunch, but I I will try to keep this entertaining. So, today I will talk about and I just realized it's a pretty long title, but harmonizing your platform domain with Kubernetes and custom resource definitions. learn maybe a bit how containers work how maybe cubectl works maybe they are doing some argo CD stuff and maybe they have some security shift left so that they also have to care about so a lot of cognitive load was throw at developers. Uh three weeks ago I was at fast flowcon in London really cool conference and there was a keynote by Raal Wanakot and it was about connective load and I love this slide it says cognitive load cannot be destroyed but it can be designed okay and that resonate with me because what I'm going to show you the way how you design your domain model for your platform it's in fact designing your connectity float so look it up uh I I think the talk is available on um I don't know maybe a Kubernetes deployment it has a label that matches maybe a Jira project and it makes sense for your platform for your developers to have this view consolidated.

### Excerpt da transcript

Hi everyone. How are you doing? >> Yeah. Okay. Enjoying the conference so far? >> Yeah. Okay. I know it's a bit hard after lunch, but I I will try to keep this entertaining. So, today I will talk about and I just realized it's a pretty long title, but harmonizing your platform domain with Kubernetes and custom resource definitions. Okay, as will become clear in a few seconds. Um, let's go. That's funny. This thing is sliding down, but I can see the time. uh a few words about myself and then we will dive into uh the meat of this talk. So I'm Sebie. Um I'm half French, half Dutch. That's why I have this weird accent. Um I'm a Java developer. Sorry for that. I won't show any Java code today. Um I'm a developer advocate. So my job is to make developers happy. And that's what I I will try to do uh this afternoon. Um I'm currently a developer relation engineer at port. Port we are an agentic engineering platform. If you don't know we know what it is. Come to the booth have a discussion with us. Um I have another slide about that later.

And beside that um I love the game HalfLife. It's the best game ever. And I love cats. I have five cats, two kids, one wife. Let's go. Okay. Um, so we we need to talk a bit about platform engineering. Okay. And we could spend the whole day trying to find a good definition of what exactly is platform engineering. I because I have only 28 minutes left. I decided to keep it short. Um, platform engineering is about empowering developers and developers is a bit restrictive. It could be anyone consuming your platform. Okay. Could be yours, your um managers, your your CTOs. Okay. Um but still empowering developers. What does that really really means? Uh because that sounds really nice, really powerful, empowering developers. But concretely, what does that mean? Well, this one really important thing implementing platform engineering in your organization is about absorbing the cognitive load of developers. When I started as a developer in 2004, I was a Java developer and the only thing I had to care about was writing my Java classes and uh committing that to CVS.

Yes, that was still a thing and yeah and then it was going in production once a year on web serere and that was okay but since then developers has to know so many things uh have so many so much connective load have to learn maybe a bit how containers work how maybe cubectl works maybe they are doing some argo CD stuff and maybe they have some security shift left so that they als
