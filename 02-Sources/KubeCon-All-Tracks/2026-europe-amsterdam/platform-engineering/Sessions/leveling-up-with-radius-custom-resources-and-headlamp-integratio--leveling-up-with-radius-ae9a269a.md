---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Nuno Guedes", "Millennium bcp", "Will Tsai", "Microsoft"]
sched_url: https://kccnceu2026.sched.com/event/2CVzX/leveling-up-with-radius-custom-resources-and-headlamp-integration-for-real-world-workloads-nuno-guedes-millennium-bcp-will-tsai-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Leveling+up+with+Radius%3A+Custom+Resources+and+Headlamp+Integration+for+Real-World+Workloads+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Leveling up with Radius: Custom Resources and Headlamp Integration for Real-World Workloads - Nuno Guedes, Millennium bcp & Will Tsai, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nuno Guedes, Millennium bcp, Will Tsai, Microsoft
- Schedule: https://kccnceu2026.sched.com/event/2CVzX/leveling-up-with-radius-custom-resources-and-headlamp-integration-for-real-world-workloads-nuno-guedes-millennium-bcp-will-tsai-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Leveling+up+with+Radius%3A+Custom+Resources+and+Headlamp+Integration+for+Real-World+Workloads+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Leveling up with Radius: Custom Resources and Headlamp Integration for Real-World Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzX/leveling-up-with-radius-custom-resources-and-headlamp-integration-for-real-world-workloads-nuno-guedes-millennium-bcp-will-tsai-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Leveling+up+with+Radius%3A+Custom+Resources+and+Headlamp+Integration+for+Real-World+Workloads+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MTFkMRngf3M
- YouTube title: Leveling up with Radius: Custom Resources and Headlamp Integration for R... Nuno Guedes & Will Tsai
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/leveling-up-with-radius-custom-resources-and-headlamp-integration-for/MTFkMRngf3M.txt
- Transcript chars: 20083
- Keywords: radius, resource, application, infrastructure, platform, implementations, deploy, environment, applications, resources, environments, instance, headlamp, developers, terraform, interface, operators, deployment

### Resumo baseado na transcript

I'm head of public cloud at Millennium BCP which is a bank in Portugal. I'm a principal product manager on the Microsoft uh Azure open source incubations team and really happy to be here and talking to you guys. And infrastructure recipes in Radius are akin to the concrete implementations of the respective resource types where the operators would encapsulate all of the infrastructure requirements such as security and cost best practices uh into the uh infrastructure recipes and uh give these over to um the developers to use. But before we get to that, uh we'll we can take a look at a quick demo that I'll show. If you're familiar with Radius and you've, you know, watched some Radius talks in the past, you might be have seen a variation of this demo before, but today we'll kind of deploy the whole shebang, right? So here's a demo and you'll see that here we have a sample demo application which consists of a front-end container, a reddis cache and an AI model to power the chatbot.

### Excerpt da transcript

Thanks everyone for being here. My name is Nunu. I'm head of public cloud at Millennium BCP which is a bank in Portugal. And will my name is Will. I'm a principal product manager on the Microsoft uh Azure open source incubations team and really happy to be here and talking to you guys. So we'll jump in then. Before uh we get started, I'll kind of go through Radius and um give you an overview of Radius and then hand it over to Nuno who will talk about the more exciting stuff uh that they're doing with Radius at Millennium VCP. But before I jump in, I'll give you an a little bit of background on where I'm from and the the team I work in at Azure. Our open source incubations team, we sit in the Azure office of the CTO. Our charter is to work across the company and the open-source community to solve problems that benefit the industry at large, not just Microsoft or Azure customers, but the industry all up. And to do this, shipping open source code is our main priority. As a part of that, we partner closely with the CNCF to provide open governance for our projects and to help us build these vibrant, innovative communities around each project.

So, of course, today I'm talking about uh Radius specifically, but I hope you have a chance to check out the other uh projects that come out of our group as well. So, what is Radius? You can think about it as kind of like an application platform that allows you to to define portable applications that can be deployed across different platforms and cloud providers. And the way it works is sort of we think about it in these four pillars of functionality for radius. You can think of the radius resource types as the abstract interfaces that the developers work with when they are putting together their applications. They shouldn't be worried about infrastructure concerns and infrastructure decisions during the development phase when they're building their applications. On the other hand, the operators think about infrastructure, right? And infrastructure recipes in Radius are akin to the concrete implementations of the respective resource types where the operators would encapsulate all of the infrastructure requirements such as security and cost best practices uh into the uh infrastructure recipes and uh give these over to um the developers to use.

Right? But uh the main thing is that this kind of setup enables a clear separation of concerns between the developers and the operators. So you can think about radius enabling you t
