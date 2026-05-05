---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Yaron Schneider", "Diagrid"]
sched_url: https://kccncna2025.sched.com/event/27FXd/resilient-by-design-building-durable-ai-agents-on-kubernetes-yaron-schneider-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Resilient+by+Design%3A+Building+Durable+AI+Agents+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Resilient by Design: Building Durable AI Agents on Kubernetes - Yaron Schneider, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Yaron Schneider, Diagrid
- Schedule: https://kccncna2025.sched.com/event/27FXd/resilient-by-design-building-durable-ai-agents-on-kubernetes-yaron-schneider-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Resilient+by+Design%3A+Building+Durable+AI+Agents+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Resilient by Design: Building Durable AI Agents on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXd/resilient-by-design-building-durable-ai-agents-on-kubernetes-yaron-schneider-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Resilient+by+Design%3A+Building+Durable+AI+Agents+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FApGdPJlJA4
- YouTube title: Resilient by Design: Building Durable AI Agents on Kubernetes - Yaron Schneider, Diagrid
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/resilient-by-design-building-durable-ai-agents-on-kubernetes/FApGdPJlJA4.txt
- Transcript chars: 31796
- Keywords: agents, dapper, basically, workflow, actually, running, agentic, systems, workflows, connect, automate, prompt, allows, observability, important, research, multiple, coming

### Resumo baseado na transcript

I'm the CTO and co-founder of a company called Diagrid that I started in January of 22. Uh both of them I created uh together with a gentleman here, Mark, you can raise your hand. I mean some of them are solving really good problems and they graduate but the projects are not getting archived as fast as they're coming in. Um Kubernetes all about automating containers and container runtimes, automating Linux croups, automating just ps in the Linux kernel. Um IP tables and routes and everything you know from the networking API in Kubernetes. We give it a problem and it gives us back a response, but you know, it does nothing to automate.

### Excerpt da transcript

Hello everyone. Thank you for being here. My name is Iron Schneider. I'm the CTO and co-founder of a company called Diagrid that I started in January of 22. I am the co-creator of the Dapper project as well as Kea. Uh both of them I created uh together with a gentleman here, Mark, you can raise your hand. Um while while we were both at Microsoft and yeah, some time has passed since then. And I'm going to start off with this very ominous warning that we see here. And be careful what you wish for. You just might get it. You probably have heard this phrase in multiple movies, podcasts, whatever during your life. Um, this is very timely for me because I just had my birthday two days ago. So, I did continue wishing for no YAML but did not get it. But really, what we're going to be talking about today is what happens when you wish for something and when reality really catches up and allows you to get the tech that basically makes those wishes come true. So what do I mean by that? I will make the claim that all of us here and the entire DevOps movement and application engineering and software engineering um are basically inside of this very hall because we wanted to automate everything.

Not necessarily because we're lazy. Maybe that too, but because we really want to make things efficient and not just that our organizations, the one we work for will become very efficient if we're able to automate everything. And I will make the case that any technology within the CNCF is all about automation. And yeah, that has worked fairly well for us, hasn't it? We've automated stuff and then came up with other tools to automate the stuff that we automated to automate the stuff that we automated. And it's going to be a never- ending cycle just continuing until all of eternity it seems because since projects are continuing to pour in and for good reason they are. I mean some of them are solving really good problems and they graduate but the projects are not getting archived as fast as they're coming in. So this landscape is basically going to grow a whole lot more and it grows every year. So you know you don't take my word for it. Let's take a few examples. Um Kubernetes all about automating containers and container runtimes, automating Linux croups, automating just ps in the Linux kernel.

Um IP tables and routes and everything you know from the networking API in Kubernetes. All of those services automated by things like Envoy, automated by service meshes like STTO and linkd
